"""Smoke tests confirming the package and its modules import correctly."""

import importlib

import pytest

import markov

MODULES = ["tokenise", "model", "smoothing", "toy_chain", "cli"]


def test_version_is_defined() -> None:
    assert isinstance(markov.__version__, str)
    assert markov.__version__.count(".") == 2


@pytest.mark.parametrize("module", MODULES)
def test_module_imports(module: str) -> None:
    assert importlib.import_module(f"markov.{module}") is not None
