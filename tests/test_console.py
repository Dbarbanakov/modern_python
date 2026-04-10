# tests/test_console.py
"""Test cases for the console module."""

from unittest.mock import Mock

from click.testing import CliRunner
import requests

from hypermodern_python import console


def test_main_succeeds(runner: CliRunner, mock_requests_get: Mock) -> None:
    """It exits with a status code of zero."""
    result = runner.invoke(console.main)
    assert result.exit_code == 0


def test_main_prints_title(runner: CliRunner, mock_requests_get: Mock) -> None:
    """It prints the title of the Wikipedia page."""
    result = runner.invoke(console.main)
    assert "delectus" in result.output


def test_main_invokes_requests_get(runner: CliRunner, mock_requests_get: Mock) -> None:
    """It invokes requests.get."""
    runner.invoke(console.main)
    assert mock_requests_get.called


def test_main_uses_todos_endpoint(runner: CliRunner, mock_requests_get: Mock) -> None:
    """It uses the todos endpoint by default."""
    runner.invoke(console.main)
    args, _ = mock_requests_get.call_args
    assert "todos" in args[0]


def test_main_uses_posts_endpoint(runner: CliRunner, mock_api_data: Mock) -> None:
    """It uses the posts endpoint."""
    runner.invoke(console.main, ["--endpoint=posts"])
    mock_api_data.assert_called_with(endpoint="posts")


def test_main_fails_on_request_error(
    runner: CliRunner, mock_requests_get: Mock
) -> None:
    """It exits with a non-zero status code if the request fails."""
    mock_requests_get.side_effect = Exception("Boom")
    result = runner.invoke(console.main)
    assert result.exit_code == 1


def test_main_prints_message_on_request_error(
    runner: CliRunner, mock_requests_get: Mock
) -> None:
    """It prints an error message if the request fails."""
    mock_requests_get.side_effect = requests.RequestException
    result = runner.invoke(console.main)
    assert "Error" in result.output
