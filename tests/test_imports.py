import importlib


def test_package_imports():
    # Top-level package
    pkg = importlib.import_module("streetmanager")
    assert pkg is not None

    # A few key subpackages should be importable
    for sub in [
        "streetmanager.work",
        "streetmanager.lookup",
        "streetmanager.event",
        "streetmanager.export",
    ]:
        mod = importlib.import_module(sub)
        assert mod is not None, f"failed to import {sub}"


def test_client_modules_importable():
    # Import generated swagger client modules without executing network calls
    modules = [
        "streetmanager.work.swagger_client.configuration",
        "streetmanager.work.swagger_client.api.default_api",
        "streetmanager.lookup.swagger_client.configuration",
        "streetmanager.lookup.swagger_client.api.default_api",
    ]
    for m in modules:
        mod = importlib.import_module(m)
        assert mod is not None, f"failed to import {m}"

