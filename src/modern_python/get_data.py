# src/hypermodern-python/get_data.py
import click
import requests


API_URL = 'https://jsonplaceholder.typicode.com/todos'


def api_data():
    try:
        with requests.get(API_URL) as response:
            response.raise_for_status()
            return response.json()
    except requests.RequestException as error:
        message = str(error)
        raise click.ClickException(message)
