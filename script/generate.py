import subprocess
import pathlib

subprocess.check_call(
    "python -m pegen --output=../parser.py ../../mingshe.gram".split(" "),
    cwd=pathlib.Path(__file__).absolute().parent.parent / "mingshe" / "_vendor",
)
