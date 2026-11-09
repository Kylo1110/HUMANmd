"""Behavior and installed-distribution checks; outputs stay in tmp_path."""

from importlib import resources
from pathlib import Path
import io
import os
import re
import socket
import subprocess
import sys
import tarfile
import zipfile

import pytest

from humanmd.cli import TEMPLATES, main
from humanmd import cli

ROOT = Path(__file__).resolve().parents[1]


def test_default(tmp_path, monkeypatch, capsys):
    monkeypatch.chdir(tmp_path)
    assert main(["init"]) == 0
    assert (tmp_path / "HUMAN.md").read_text(encoding="utf-8") == resources.files("humanmd").joinpath("templates/minimal.md").read_text(encoding="utf-8")
    assert "Created HUMAN.md (minimal)" in capsys.readouterr().out
    assert list(tmp_path.iterdir()) == [tmp_path / "HUMAN.md"]


@pytest.mark.parametrize("terminal,no_color,term,encoding,columns", [
    (True, False, "xterm-256color", "utf-8", 80),
    (True, True, "xterm-256color", "utf-8", 80),
    (False, False, "xterm-256color", "utf-8", 80),
    (True, False, "dumb", "utf-8", 80),
    (True, False, "xterm-256color", "ascii", 80),
    (True, False, "xterm-256color", "utf-8", 32),
])
def test_terminal_output(tmp_path, monkeypatch, terminal, no_color, term, encoding, columns):
    class Output(io.StringIO):
        @property
        def encoding(self):
            return encoding

        def isatty(self):
            return terminal

    output = Output()
    monkeypatch.setattr(sys, "stdout", output)
    monkeypatch.setenv("TERM", term)
    monkeypatch.setenv("WT_SESSION", "test")
    monkeypatch.delenv("NO_COLOR", raising=False)
    if no_color:
        monkeypatch.setenv("NO_COLOR", "1")
    monkeypatch.setattr(cli.shutil, "get_terminal_size", lambda: os.terminal_size((columns, 24)))
    target = tmp_path / "café"
    target.mkdir()
    assert main(["init", "--path", str(target)]) == 0
    rendered = output.getvalue()
    assert ("\033[" in rendered) == (terminal and not no_color and term != "dumb")
    # Strip color before checking wrapping and the content of the next steps.
    plain = re.sub(r"\x1b\[[0-9;]*m", "", rendered)
    assert max(map(len, plain.splitlines())) <= columns
    assert "BEFORE YOU BUILD" in plain
    assert "03  Ask your agent" in plain
    assert str(target / "HUMAN.md").encode(encoding, errors="backslashreplace").decode(encoding).replace(" ", "") in "".join(plain.split())
    plain.encode(encoding)
    if encoding == "ascii" or not terminal or term == "dumb":
        assert "✓" not in plain and "╭" not in plain


@pytest.mark.parametrize("template", TEMPLATES)
def test_templates(tmp_path, template):
    assert main(["init", "-t", template, "--path", str(tmp_path)]) == 0
    content = (tmp_path / "HUMAN.md").read_text(encoding="utf-8")
    assert "## Decision Log" in content
    assert "— Initial Intent" in content


@pytest.mark.parametrize("relative", [True, False])
def test_custom_path(tmp_path, monkeypatch, relative):
    project = tmp_path / "café project"
    project.mkdir()
    monkeypatch.chdir(tmp_path)
    assert main(["init", "--path", project.name if relative else str(project)]) == 0
    assert (project / "HUMAN.md").is_file()


def test_expand_user(tmp_path, monkeypatch):
    monkeypatch.setenv("HOME", str(tmp_path))
    monkeypatch.setenv("USERPROFILE", str(tmp_path))
    assert main(["init", "--path", "~"]) == 0
    assert (tmp_path / "HUMAN.md").exists()


@pytest.mark.parametrize("kind", ["file", "directory", "symlink", "dangling"])
def test_existing_protection(tmp_path, kind, capsys):
    target = tmp_path / "HUMAN.md"
    other = tmp_path / "original.md"
    if kind == "file":
        target.write_bytes(b"Human-owned reasoning\xff")
    elif kind == "directory":
        target.mkdir()
    else:
        if kind == "symlink":
            other.write_text("Human intent", encoding="utf-8")
        try:
            target.symlink_to(other)
        except OSError as error:
            if os.name == "nt" and getattr(error, "winerror", None) == 1314:
                pytest.skip("Windows runner lacks the privilege to create symlinks")
            raise
    assert main(["init", "--path", str(tmp_path)]) == 1
    output = capsys.readouterr()
    assert "HUMAN.md already exists.\nNothing was changed." in output.err
    assert output.out == ""
    if kind == "file":
        assert target.read_bytes() == b"Human-owned reasoning\xff"
    elif kind == "directory":
        assert target.is_dir()
    else:
        assert target.is_symlink()
        if kind == "symlink":
            assert other.read_text(encoding="utf-8") == "Human intent"
        else:
            assert not other.exists()


@pytest.mark.parametrize("is_file", [True, False])
def test_invalid_directory(tmp_path, is_file, capsys):
    target = tmp_path / "missing"
    if is_file:
        target.write_text("keep me", encoding="utf-8")
    assert main(["init", "--path", str(target)]) == 1
    assert "not a directory" in capsys.readouterr().err
    assert target.is_file() if is_file else not target.exists()


def test_invalid_template(tmp_path, capsys):
    with pytest.raises(SystemExit) as error:
        main(["init", "-t", "invalid", "--path", str(tmp_path)])
    assert error.value.code == 2
    message = capsys.readouterr().err
    assert all(name in message for name in TEMPLATES)
    assert not (tmp_path / "HUMAN.md").exists()


def test_competing_creation(tmp_path, monkeypatch):
    original = Path.open
    target = tmp_path / "HUMAN.md"

    def competing_writer(path, mode="r", *args, **kwargs):
        if mode == "x":
            with original(path, "w", encoding="utf-8") as stream:
                stream.write("Another human's intent")
        return original(path, mode, *args, **kwargs)

    monkeypatch.setattr(Path, "open", competing_writer)
    assert main(["init", "--path", str(tmp_path)]) == 1
    assert target.read_text(encoding="utf-8") == "Another human's intent"


@pytest.mark.parametrize("error", [PermissionError("denied"), OSError("disk failure")])
def test_filesystem_error(tmp_path, monkeypatch, capsys, error):
    original = Path.open

    def fail_write(path, mode="r", *args, **kwargs):
        if mode == "x":
            raise error
        return original(path, mode, *args, **kwargs)

    monkeypatch.setattr(Path, "open", fail_write)
    assert main(["init", "--path", str(tmp_path)]) == 1
    message = capsys.readouterr().err
    assert str(error) in message
    assert "Traceback" not in message


def test_offline(tmp_path, monkeypatch):
    def denied(*args, **kwargs):
        raise AssertionError("Network access attempted")

    monkeypatch.setattr(socket, "socket", denied)
    monkeypatch.setattr(socket, "getaddrinfo", denied)
    assert main(["init", "--path", str(tmp_path)]) == 0


def test_listing(capsys):
    assert main(["templates"]) == 0
    output = capsys.readouterr().out
    assert all(name in output and description in output for name, description in TEMPLATES.items())


@pytest.mark.parametrize("args", [["--help"], ["init", "--help"], ["--version"]])
def test_help_and_version(args, capsys):
    with pytest.raises(SystemExit) as error:
        main(args)
    assert error.value.code == 0
    output = capsys.readouterr().out
    assert "0.1.0" in output if args == ["--version"] else "usage:" in output


def test_no_command(capsys):
    assert main([]) == 0
    assert "usage:" in capsys.readouterr().out


def run(*args, cwd, env=None):
    try:
        return subprocess.run(args, cwd=cwd, env=env, check=True, capture_output=True, text=True)
    except subprocess.CalledProcessError as error:
        pytest.fail(f"Command failed: {args!r}\n{error.stdout}\n{error.stderr}", pytrace=False)


def test_distributions_and_installed_entry_points(tmp_path):
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    assert readme.count('src="docs/assets/') == 3
    packaged_readme = readme.replace(
        'src="docs/assets/',
        'src="https://raw.githubusercontent.com/Kylo1110/HUMANmd/main/docs/assets/',
    )
    artifacts = tmp_path / "dist"
    run(sys.executable, "-m", "build", "--no-isolation", "--outdir", str(artifacts), cwd=ROOT)
    wheel, = artifacts.glob("*.whl")
    sdist, = artifacts.glob("*.tar.gz")
    with zipfile.ZipFile(wheel) as archive:
        metadata, = (name for name in archive.namelist() if name.endswith(".dist-info/METADATA"))
        assert archive.read(metadata).decode("utf-8").split("\n\n", 1)[1] == packaged_readme
        for template in TEMPLATES:
            assert f"humanmd/templates/{template}.md" in archive.namelist()
    with tarfile.open(sdist) as archive:
        assert any(name.endswith("/hatch_build.py") for name in archive.getnames())
        for template in TEMPLATES:
            assert any(name.endswith(f"/src/humanmd/templates/{template}.md") for name in archive.getnames())
        archive.extractall(tmp_path / "source", filter="data") if sys.version_info >= (3, 12) else archive.extractall(tmp_path / "source")
    source, = (tmp_path / "source").iterdir()
    rebuilt = tmp_path / "rebuilt"
    run(sys.executable, "-m", "build", "--wheel", "--no-isolation", "--outdir", str(rebuilt), cwd=source)
    with zipfile.ZipFile(next(rebuilt.glob("*.whl"))) as archive:
        metadata, = (name for name in archive.namelist() if name.endswith(".dist-info/METADATA"))
        assert archive.read(metadata).decode("utf-8").split("\n\n", 1)[1] == packaged_readme
        assert all(f"humanmd/templates/{name}.md" in archive.namelist() for name in TEMPLATES)
    environment = tmp_path / "venv"
    scripts = environment / ("Scripts" if os.name == "nt" else "bin")
    python = scripts / ("python.exe" if os.name == "nt" else "python")
    cli = scripts / ("humanmd.exe" if os.name == "nt" else "humanmd")
    clean_env = {key: value for key, value in os.environ.items() if key not in {"PYTHONPATH", "PYTHONHOME"}}
    # Let uv handle standalone interpreter layouts without ensurepip or copying
    # an executable away from its runtime libraries.
    run("uv", "venv", "--python", sys.executable, str(environment), cwd=tmp_path, env=clean_env)
    run("uv", "pip", "install", "--python", str(python), "--no-index", "--no-deps", str(wheel), cwd=tmp_path, env=clean_env)
    assert run(str(cli), "--version", cwd=tmp_path, env=clean_env).stdout.strip() == "0.1.0"
    assert "research" in run(str(cli), "templates", cwd=tmp_path, env=clean_env).stdout
    for name in TEMPLATES:
        target = tmp_path / name
        target.mkdir()
        run(str(cli), "init", "-t", name, cwd=target, env=clean_env)
        assert (target / "HUMAN.md").read_text(encoding="utf-8").startswith("# HUMAN.md")
    module_target = tmp_path / "module"
    module_target.mkdir()
    run(str(python), "-m", "humanmd", "init", cwd=module_target, env=clean_env)
    # Execute the installed package with network primitives disabled.
    offline_target = tmp_path / "offline"
    offline_target.mkdir()
    script = "import socket; socket.socket=lambda *a, **k: (_ for _ in ()).throw(AssertionError('network')); socket.getaddrinfo=socket.socket; from humanmd.cli import main; raise SystemExit(main(['init']))"
    run(str(python), "-c", script, cwd=offline_target, env=clean_env)
    assert (offline_target / "HUMAN.md").exists()
