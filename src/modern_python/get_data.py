# src/hypermodern-python/get_data.py
import requests


API_URL = 'https://jsonplaceholder.typicode.com/todos'



def api_data():
    with requests.get(API_URL) as response:
        response.raise_for_status()
        return response.json()