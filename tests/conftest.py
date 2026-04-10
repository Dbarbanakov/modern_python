import click.testing
import pytest


@pytest.fixture
def runner():
    return click.testing.CliRunner()


@pytest.fixture
def mock_requests_get(mocker):
    mock = mocker.patch("requests.get")
    mock.return_value.__enter__.return_value.json.return_value = [
        {"title": "delectus aut autem", "id": 1},
    ]
    return mock


@pytest.fixture
def mock_api_data(mocker):
    return mocker.patch("modern_python.get_data.api_data")
