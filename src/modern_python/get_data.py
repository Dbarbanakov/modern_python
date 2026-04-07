# src/hypermodern-python/get_data.py
import click
import requests


API_URL = 'https://jsonplaceholder.typicode.com/{end_point}'


def api_data(end_point='todos'):
    url = API_URL.format(end_point=end_point)

    try:
        with requests.get(url) as response:
            response.raise_for_status()
            return response.json()
    except requests.RequestException as error:
        message = str(error)
        raise click.ClickException(message)
