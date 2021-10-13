import sys
from pathlib import Path

import pytest

from mingshe.importlib import install_meta, uninstall_meta


def test_importlib():
    path = str(Path(__file__).absolute().parent / "for_test_importlib")
    sys.path.insert(0, path)
    try:
        install_meta(".she")

        import a
        assert a.name == "a"

        import p
        assert p.name == "p"

        from t.b import name
        assert name == "t.b"

        uninstall_meta(".she")

        del sys.modules["a"]
        del sys.modules["p"]
        del sys.modules["t.b"]

        with pytest.raises(ImportError):
            import a

    finally:
        sys.path.remove(path)
