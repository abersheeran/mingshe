import ast
import argparse
import builtins
import logging
import re
import sys
from pathlib import Path

from .__version__ import __version__
from .core import compile
from .importlib import install_meta


def main():
    argparser = argparse.ArgumentParser(description=f"MíngShé {__version__}")
    argparser.add_argument("file", help="The .she file", nargs="?")
    argparser.add_argument(
        "--python",
        help="Python version. e.g. 3.7",
        default=".".join(map(str, sys.version_info[:2])),
    )
    argparser.add_argument(
        "--compile", dest="compile", action="store_true", help="Only compile"
    )
    argparser.add_argument(
        "-c", dest="cmd", action="store_true", help="Run a short command"
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

    if verbose:
        logging.getLogger("mingshe").setLevel(logging.DEBUG)
        logging.basicConfig()

    python = tuple(map(int, re.fullmatch(r"(\d+)\.(\d+)", args.python).groups()))

    global_vars = {"__name__": "__main__"}

    write_to_py = lambda x: sys.stdout.write(x)

    if not args.cmd:
        if args.file is None:
            mingshe_code = sys.stdin.readable() and sys.stdin.read()
            filename = "<stdin>"
        else:
            _filepath = Path(args.file)
            mingshe_code = _filepath.read_text(encoding="utf8")
            filename = _filepath.absolute().__str__()
            write_to_py = _filepath.with_suffix(".py").absolute().write_text
        global_vars["__file__"] = filename
    else:
        mingshe_code = args.file
        filename = "<string>"

    ast_obj = compile(
        mingshe_code,
        filename=filename,
        verbose_tokenizer=verbose_tokenizer,
        verbose_parser=verbose_parser,
        py_version=python,
    )

    if args.compile:
        py_text = ast.unparse(ast_obj)
        write_to_py(py_text, encoding="utf8")
    else:
        sys.path.insert(0, str(Path(".").absolute()))
        install_meta(".she")  # 无论 .pth 是否加载均可解析 .she 文件
        builtins.exec(builtins.compile(ast_obj, filename, "exec"), global_vars)
