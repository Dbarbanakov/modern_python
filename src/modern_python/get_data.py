# src/hypermodern-python/get_data.py
from dataclasses import dataclass

import click
import desert
import marshmallow
import requests

API_URL: str = "https://jsonplaceholder.typicode.com/{end_point}"


@dataclass
class Data:
    title: str
    id: int


schema = desert.schema(Data, meta={"unknown": marshmallow.EXCLUDE})


def api_data(end_point: str) -> Data:
    url = API_URL.format(end_point=end_point)

    try:
        with requests.get(url, timeout=10) as response:
            response.raise_for_status()
            data = response.json()[0]
            return schema.load(data)
    except (requests.RequestException, marshmallow.ValidationError) as error:
        message = str(error)
        raise click.ClickException(message) from error
