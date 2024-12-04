import pytest
from Day3.PyTest_examples.code_pytest import fetch_data


@pytest.fixture(autouse=True)
def mock_requests_get(monkeypatch):
    def mock_get(url):
        return MockResponse("Mocked response")

    # Podmiana metody requests.get() na funkcję mockową
    monkeypatch.setattr("requests.get", mock_get)


class MockResponse:
    def __init__(self, text):
        self.text = text


def test_fetch_data():
    result = fetch_data()
    assert result == "Mocked response"


