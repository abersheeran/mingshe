import builtins
import code
from typing import Any, Mapping, Optional

from .core import compile


def compile_command(source, filename="<input>", symbol="single"):
    try:
        source = compile(source, filename, symbol={"single": "interactive", "exec": "file"}.get(symbol, symbol))
    except SyntaxError:
        pass
    finally:
        return builtins.compile(source, filename, mode=symbol)


class Repl(code.InteractiveConsole):
    """
    MíngShé REPL
    """
    def __init__(self, locals: Optional[Mapping[str, Any]] = None, filename: str = "<console>") -> None:
        super().__init__(locals=locals, filename=filename)
        self.compile.compiler = compile_command


if __name__ == "__main__":
    repl = Repl()
    repl.interact()
