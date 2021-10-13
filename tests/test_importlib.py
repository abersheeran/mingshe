import sys
from pathlib import Path

from mingshe.importlib import install_meta, uninstall_meta


def test_importlib():
    install_meta(".she")

    path = str(Path(__file__).absolute().parent / "for_test_importlib")
    sys.path.insert(0, path)
    try:
        import a
        assert a.name == "a"

        import p
        assert p.name == "p"

        from t.b import name
        assert name == "t.b"

    finally:
        sys.path.remove(path)

        uninstall_meta(".she")
