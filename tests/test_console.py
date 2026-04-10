# tests/test_console.py
from unittest.mock import Mock

from click.testing import CliRunner
import requests

from modern_python import console


def test_main_uses_posts_endpoint(runner: CliRunner, mock_api_data: Mock) -> None:
    runner.invoke(console.main, ["--endpoint=posts"])
    mock_api_data.assert_called_with(end_point="posts")


def test_main_succeeds(runner: CliRunner, mock_requests_get: Mock) -> None:
    result = runner.invoke(console.main)
    assert result.exit_code == 0


def test_main_prints_title(runner: CliRunner, mock_requests_get: Mock) -> None:
    result = runner.invoke(console.main)
    assert "delectus" in result.output


def test_main_invokes_requests_get(runner: CliRunner, mock_requests_get: Mock) -> None:
    runner.invoke(console.main)
    assert mock_requests_get.called


def test_main_uses_json_placeholder_api(
    runner: CliRunner, mock_requests_get: Mock
) -> None:
    runner.invoke(console.main)
    args, _ = mock_requests_get.call_args
    assert "jsonplaceholder" in args[0]


def test_main_fails_on_request_error(
    runner: CliRunner, mock_requests_get: Mock
) -> None:
    mock_requests_get.side_effect = Exception("Boom")
    result = runner.invoke(console.main)
    assert result.exit_code == 1


def test_main_prints_message_on_request_error(
    runner: CliRunner, mock_requests_get: Mock
) -> None:
    mock_requests_get.side_effect = requests.RequestException
    result = runner.invoke(console.main)
    assert "Error" in result.output
