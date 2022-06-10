import cdsapiserver


def test_version() -> None:
    assert cdsapiserver.__version__ != "999"
