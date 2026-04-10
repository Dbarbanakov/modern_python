from unittest.mock import Mock

from click.testing import CliRunner

from modern_python import console, get_data


def test_posts_endpoint(runner: CliRunner, mock_requests_get: Mock) -> None:
    # get_data.api_data(end_point="posts")
    runner.invoke(console.main, ["--endpoint=posts"])
    args, _ = mock_requests_get.call_args
    assert "/posts" in args[0]


def test_todos_endpoint(runner: CliRunner, mock_requests_get: Mock) -> None:
    # get_data.api_data(end_point="todos")
    runner.invoke(console.main, ["--endpoint=todos"])
    args, _ = mock_requests_get.call_args
    assert "/todos" in args[0]


def test_api_data_returns_data(mock_requests_get: Mock) -> None:
    data = get_data.api_data(end_point="posts")
    assert isinstance(data, get_data.Data)


# Test for Runtime type checking with Typeguard.
# def test_trigger_typeguard(mock_requests_get):
#     import json

#     end_point = json.loads('{ "end_point": 1 }')
#     get_data.api_data(end_point=end_point)
