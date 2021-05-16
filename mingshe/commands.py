import argparse
import subprocess
import sys
from pathlib import Path

from mingshe.utils import work_with_files

from .__version__ import __version__
from .core import compile


def main():
    parser = argparse.ArgumentParser(description=f"MíngShé {__version__}")
    parser.add_argument("filepath", type=Path, help="The .ms file")
    parser.add_argument(
        "--compile", dest="compile", action="store_true", help="Only compile"
    )

    args = parser.parse_args()
    py_path = args.filepath.with_suffix(".py").absolute()
    py_text = compile(args.filepath.read_text(encoding="utf8"))

    if args.compile:
        py_path.write_text(py_text, encoding="utf8")
    else:
        with work_with_files((py_path, py_text)):
            subprocess.check_call([sys.executable, str(py_path)])
