"""Initialize HUMAN.md without generating or replacing human intent."""

import argparse
from importlib import metadata, resources
import os
from pathlib import Path
import shutil
import sys
import textwrap

TEMPLATES = {
    "minimal": "A short starting point for any project.",
    "research": "Questions, hypotheses, and evaluation criteria.",
    "software": "Problems, users, constraints, and success criteria.",
    "exploration": "Early ideas, assumptions, and experiments.",
}


def package_version():
    try:
        return metadata.version("humanmd")
    except metadata.PackageNotFoundError:
        return "unknown (install humanmd to read its package version)"


def print_success(target, template):
    """Present the next step without adding terminal controls to redirected output."""
    terminal = sys.stdout.isatty() and os.environ.get("TERM") != "dumb"
    color = terminal and "NO_COLOR" not in os.environ
    if os.name == "nt" and not os.environ.get("WT_SESSION"):
        color = False
    encoding = sys.stdout.encoding or "utf-8"
    try:
        "╭─╮│╰╯✓".encode(encoding)
        use_unicode = terminal
    except (UnicodeEncodeError, LookupError):
        use_unicode = False
    width = max(20, min(shutil.get_terminal_size().columns - 4, 72))

    def paint(value, style):
        return f"\033[{style}m{value}\033[0m" if color else value

    def write(value="", style=None):
        # Keep paths printable even when a terminal has a legacy encoding.
        value = value.encode(encoding, errors="backslashreplace").decode(encoding)
        if style and value:
            value = paint(value, style)
        print("  " + value if value else "")

    def wrapped(value, style=None):
        for line in textwrap.wrap(value, width=width):
            write(line, style)

    tagline = "Code is getting cheaper. Thinking isn't."
    write()
    if terminal and width >= 46:
        inner = width - 4
        left, horizontal, right, side, bottom_left, bottom_right = (
            ("╭", "─", "╮", "│", "╰", "╯") if use_unicode
            else ("+", "-", "+", "|", "+", "+")
        )
        write(left + horizontal * (width - 2) + right, "36")
        for label in ("HUMAN.md", tagline):
            write(side + " " + label.ljust(inner) + " " + side, "1;36")
        write(bottom_left + horizontal * (width - 2) + bottom_right, "36")
    else:
        write("HUMAN.md", "1;36")
        wrapped(tagline)
    write()
    wrapped(f"{'✓' if use_unicode else '+'} Created HUMAN.md ({template})", "1;32")
    wrapped(f"Location: {target}", "2")
    write()
    write("BEFORE YOU BUILD", "1")
    for step, instruction in enumerate((
        "Open HUMAN.md and write why this project exists.",
        "Define success, or what you want to learn.",
        "Ask your agent to read it before implementation.",
    ), start=1):
        lines = textwrap.wrap(instruction, width=width - 4)
        write(f"{step:02}  {lines[0]}", "36")
        for line in lines[1:]:
            write("    " + line)
    write()
    wrapped("AI can propose. Humans decide.", "2")
    write()


def initialize(path, template):
    """Create a template exclusively; leave existing directory entries intact."""
    try:
        directory = Path(path).expanduser().resolve()
        if not directory.is_dir():
            print(
                f"Error: target directory does not exist or is not a directory: {directory}",
                file=sys.stderr,
            )
            return 1
        if template not in TEMPLATES:
            print(
                f"Error: invalid template {template!r}. Choose from: {', '.join(TEMPLATES)}",
                file=sys.stderr,
            )
            return 1
        content = (
            resources.files("humanmd")
            .joinpath("templates")
            .joinpath(f"{template}.md")
            .read_text(encoding="utf-8")
        )
        target = directory / "HUMAN.md"
        # Windows can follow a dangling symlink even in exclusive-open mode,
        # and reports existing directories as permission errors. Inspect the
        # directory entry itself before opening; keep exclusive creation to
        # protect against another initializer creating a regular file meanwhile.
        try:
            target.lstat()
        except FileNotFoundError:
            pass
        else:
            raise FileExistsError
        with target.open("x", encoding="utf-8", newline="\n") as stream:
            stream.write(content)
    except FileExistsError:
        print("HUMAN.md already exists.\nNothing was changed.", file=sys.stderr)
        return 1
    except (OSError, RuntimeError) as error:
        print(f"Error: could not initialize HUMAN.md: {error}", file=sys.stderr)
        return 1
    print_success(target, template)
    return 0


def main(argv=None):
    parser = argparse.ArgumentParser(description="Give human intent a home. Initialize a HUMAN.md template offline.")
    parser.add_argument("--version", action="version", version=package_version())
    commands = parser.add_subparsers(dest="command")
    init = commands.add_parser("init", help="Create HUMAN.md without overwriting existing work.")
    init.add_argument("-t", "--template", choices=TEMPLATES, default="minimal", help="Template to use (default: minimal).")
    init.add_argument("--path", default=".", help="Existing target directory (default: current directory).")
    commands.add_parser("templates", help="List the four bundled templates.")
    args = parser.parse_args(argv)
    if args.command == "init":
        return initialize(args.path, args.template)
    if args.command == "templates":
        for name, description in TEMPLATES.items():
            print(f"{name:12} {description}")
        return 0
    parser.print_help()
    return 0
