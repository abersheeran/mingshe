import contextlib
import os
from typing import Tuple


@contextlib.contextmanager
def work_with_files(*files: Tuple[str, str]) -> None:
    try:
        for file, text in files:
            with open(file, "w+", encoding="utf8") as f:
                f.write(text)
        yield None
    finally:
        for file, _ in files:
            try:
                os.remove(file)
            except Exception:
                pass
