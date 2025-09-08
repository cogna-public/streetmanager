from streetmanager.work.swagger_client.configuration import Configuration as WorkConfig
from streetmanager.lookup.swagger_client.configuration import Configuration as LookupConfig


def test_configuration_defaults_and_override():
    # Work API configuration
    wc = WorkConfig()
    assert isinstance(wc.host, str)
    assert "github.io" in wc.host

    # Override host should stick
    new_host = "https://example.com/api"
    wc.host = new_host
    assert wc.host == new_host

    # Lookup API configuration
    lc = LookupConfig()
    assert isinstance(lc.host, str)
    assert "github.io" in lc.host


def test_debug_logging_toggles():
    cfg = WorkConfig()
    # default should be False
    assert cfg.debug is False
    cfg.debug = True
    assert cfg.debug is True
    cfg.debug = False
    assert cfg.debug is False

