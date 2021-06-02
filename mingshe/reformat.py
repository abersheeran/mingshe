import sys
from ast import parse

if sys.version_info < (3, 9):
    from astunparse import unparse
else:
    from ast import unparse


def reformat(code: str) -> str:
    return unparse(parse(code))
