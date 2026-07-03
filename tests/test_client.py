"""Basic tests for the VAGO Cloud Python SDK."""

import pytest

from vago import VagoClient


def test_client_requires_token():
    with pytest.raises(ValueError):
        VagoClient(token="")


def test_client_stores_config():
    client = VagoClient(token="vago_agt_test", base_url="https://api.example.com")
    assert client._token == "vago_agt_test"
    assert client._base_url == "https://api.example.com"


def test_safe_json_parses_text():
    class FakeResponse:
        status_code = 200
        text = "not json"

        def json(self):
            raise ValueError("nope")

    result = VagoClient._safe_json(FakeResponse())
    assert result == {"raw": "not json"}
