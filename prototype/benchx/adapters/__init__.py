"""Harness adapters (harness-adapter.md). The contract is in `base`."""

from . import gbench

ADAPTERS = {gbench.NAME: gbench}


def get(name: str):
    """The adapter module registered under `name`, or None."""
    return ADAPTERS.get(name)
