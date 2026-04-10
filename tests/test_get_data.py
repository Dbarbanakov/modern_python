"""Test cases for the get_data module."""

from unittest.mock import Mock

from hypermodern_python import get_data


def test_api_data_returns_data(mock_requests_get: Mock) -> None:
    """It returns an object of type Data."""
    data = get_data.api_data(endpoint="posts")
    assert isinstance(data, get_data.Data)


# Test for Runtime type checking with Typeguard.
# def test_trigger_typeguard(mock_requests_get):
#     import json

#     end_point = json.loads('{ "end_point": 1 }')
#     get_data.api_data(end_point=end_point)
