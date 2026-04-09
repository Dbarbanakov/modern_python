# src/hypermodern-python/get_data.py
from typing import Any

import click
import requests

API_URL: str = "https://jsonplaceholder.typicode.com/{end_point}"


def api_data(end_point: str = "todos") -> Any:
    url = API_URL.format(end_point=end_point)

    try:
        with requests.get(url, timeout=10) as response:
            response.raise_for_status()
            return response.json()
    except requests.RequestException as error:
        message = str(error)
        raise click.ClickException(message) from error
