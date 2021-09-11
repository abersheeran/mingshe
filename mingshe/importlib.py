from __future__ import annotations

import abc
import builtins
import importlib
import importlib.abc
import logging
import os
import sys
import types
from importlib.machinery import ModuleSpec
from pathlib import Path

from .core import compile

log = logging.getLogger(__name__)


class SingletonMetaFinder(abc.ABCMeta):  # inherit from abc.ABCMeta to deal metaclass conflict
    def __init__(cls, name, bases, namespace):
        cls.instances = {}

    def __call__(cls, suffix: str) -> ExtensionMetaFinder:
        if suffix not in cls.instances:
            cls.instances[suffix] = super().__call__(suffix)
        return cls.instances[suffix]


class ExtensionMetaFinder(importlib.abc.MetaPathFinder, metaclass=SingletonMetaFinder):
    def __init__(self, suffix: str):
        self.suffix = suffix

    def find_spec(self, module_name: str, path: str, target: str = None):
        if path is None:
            paths = [
                path for path in map(Path, sys.path) if path.exists() and path.is_dir()
            ]
        else:
            paths = list(map(Path, path))
        for try_path in paths:
            log.debug(f"Finding module {module_name} in {try_path}")
            last_module_name = module_name.rpartition(".")[2]
            for name in os.listdir(try_path):
                fullpath = try_path / name
                if (
                    fullpath.is_file()
                    and fullpath.name == last_module_name + self.suffix
                ):
                    log.debug(f"Found module '{module_name}' in {fullpath}")
                    loader = ExtensionModuleLoader(fullpath)
                    return ModuleSpec(module_name, loader, origin=fullpath)
                elif fullpath.is_dir() and fullpath.name == last_module_name:
                    log.debug(f"Found package '{module_name}' in {fullpath}")
                    loader = ExtensionPackageLoader(fullpath)
                    return ModuleSpec(
                        module_name, loader, origin=fullpath, is_package=True
                    )


class ExtensionModuleLoader(importlib.abc.SourceLoader):
    def __init__(self, filepath: Path) -> None:
        self.filepath = filepath

    def create_module(self, spec: ModuleSpec) -> types.ModuleType | None:
        module = super().create_module(spec)
        log.debug(f"Created module '{spec.name}'")
        return module

    def exec_module(self, module: types.ModuleType) -> None:
        setattr(module, "__file__", self.get_filename(module.__name__))
        builtins.exec(self.get_code(module.__spec__), module.__dict__)
        log.debug(f"Executed module '{module.__name__}'")

    def get_data(self, path: str) -> bytes:
        return Path(path).read_bytes()

    def get_filename(self, module_name: str) -> str:
        return str(self.filepath)

    def source_to_code(self, data: bytes, path: str = "<string>") -> types.CodeType:
        return builtins.compile(compile(data.decode("utf8"), path), path, "exec")


class ExtensionPackageLoader(ExtensionModuleLoader):
    def exec_module(self, module: types.ModuleType) -> None:
        setattr(
            module, "__path__", [os.path.dirname(self.get_filename(module.__name__))]
        )
        super().exec_module(module)

    def get_filename(self, module_name: str) -> str:
        return str(self.filepath / "__init__.she")


# Utility functions for installing/uninstalling the loader


def install_meta(suffix: str) -> None:
    finder = ExtensionMetaFinder(suffix)
    sys.meta_path.insert(0, finder)


def uninstall_meta(suffix: str) -> None:
    finder = ExtensionMetaFinder(suffix)
    sys.meta_path.remove(finder)
