# src/hypermodern_python/get_data.py
"""Client for the JSON Placeholder REST API, version 1."""

from dataclasses import dataclass

import click
import desert
import marshmallow
import requests

API_URL: str = "https://jsonplaceholder.typicode.com/{endpoint}"


@dataclass
class Data:
    """Data resource.

    Attributes:
        title: The title of the post or to-do.
        id: User Identifier.
    """

    title: str
    id: int


schema = desert.schema(Data, meta={"unknown": marshmallow.EXCLUDE})


def api_data(endpoint: str) -> Data:
    """Return a data from an API end point.

    Performs a GET request to the /page/endpoint.

    Args:
        endpoint: The JSON Placeholder API endpoint. By default, "todos".

    Returns:
        Data resource.

    Raises:
        ClickException: The HTTP request failed or the HTTP response
            contained an invalid body.

    Example:
        >>> from hypermodern_python import get_data
        >>> data = get_data.api_data("todos")
        >>> bool(data.title)
        True
    """
    url = API_URL.format(endpoint=endpoint)

    try:
        with requests.get(url, timeout=10) as response:
            response.raise_for_status()
            data = response.json()[0]
            return schema.load(data)
    except (requests.RequestException, marshmallow.ValidationError) as error:
        message = str(error)
        raise click.ClickException(message) from error
