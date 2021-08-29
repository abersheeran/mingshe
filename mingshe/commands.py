import ast
import argparse
from pathlib import Path

from .__version__ import __version__
from .core import compile, exec


def main():
    argparser = argparse.ArgumentParser(description=f"MíngShé {__version__}")
    argparser.add_argument("filepath", type=Path, help="The .she file")
    argparser.add_argument(
        "--compile", dest="compile", action="store_true", help="Only compile"
    )
    argparser.add_argument(
        "-v",
        "--verbose",
        action="count",
        default=0,
        help="Print timing stats; repeat for more debug output",
    )

    args = argparser.parse_args()
    verbose = args.verbose
    verbose_tokenizer = verbose >= 3
    verbose_parser = verbose == 2 or verbose >= 4

    if args.compile:
        ast_obj = compile(
            args.filepath.read_text(encoding="utf8"),
            filename=args.filepath,
            verbose_tokenizer=verbose_tokenizer,
            verbose_parser=verbose_parser,
        )
        py_text = ast.unparse(ast_obj)
        py_path = args.filepath.with_suffix(".py").absolute()
        py_path.write_text(py_text, encoding="utf8")
    else:
        exec(args.filepath.read_text(encoding="utf8"), filename=args.filepath)
