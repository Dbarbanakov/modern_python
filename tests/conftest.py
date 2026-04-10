from unittest.mock import Mock

from click.testing import CliRunner
import pytest
from pytest_mock import MockFixture


@pytest.fixture
def runner() -> CliRunner:
    return CliRunner()


@pytest.fixture
def mock_requests_get(mocker: MockFixture) -> Mock:
    mock = mocker.patch("requests.get")
    mock.return_value.__enter__.return_value.json.return_value = [
        {"title": "delectus aut autem", "id": 1},
    ]
    return mock


@pytest.fixture
def mock_api_data(mocker: MockFixture) -> Mock:
    return mocker.patch("modern_python.get_data.api_data")
