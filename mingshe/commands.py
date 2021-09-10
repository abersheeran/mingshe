import ast
import argparse
import re
import sys
from pathlib import Path

from .__version__ import __version__
from .core import compile, exec


def main():
    argparser = argparse.ArgumentParser(description=f"MíngShé {__version__}")
    argparser.add_argument("filepath", type=Path, help="The .she file")
    argparser.add_argument("--python", help="Python version. e.g. 3.7", default=".".join(map(str, sys.version_info[:2])))
    argparser.add_argument(
        "--compile", dest="compile", action="store_true", help="Only compile"
    )
    argparser.add_argument(
        "-v",
        "--verbose",
        action="count",
        default=0,
        help="Repeat for more debug output. e.g. -vv -vvv -vvvv",
    )

    args = argparser.parse_args()
    verbose = args.verbose
    verbose_tokenizer = verbose >= 3
    verbose_parser = verbose == 2 or verbose >= 4

    python = tuple(map(int, re.fullmatch(r"(\d+)\.(\d+)", args.python).groups()))

    if args.compile:
        ast_obj = compile(
            args.filepath.read_text(encoding="utf8"),
            filename=args.filepath,
            verbose_tokenizer=verbose_tokenizer,
            verbose_parser=verbose_parser,
            py_version=python,
        )
        py_text = ast.unparse(ast_obj)
        py_path = args.filepath.with_suffix(".py").absolute()
        py_path.write_text(py_text, encoding="utf8")
    else:
        exec(args.filepath.read_text(encoding="utf8"), filename=args.filepath)
