import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
token = 'e5835c94879cc11ccea830c7425f3310'
header = {'Content-Type': 'application/json', 'trainer_token' : token}
my_trainer_id = '36698'

##############

def test_status_code():
    response = requests.get(url = f'{URL}/trainers')
    assert response.status_code == 200

def test_say_my_name():
    response_get = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : my_trainer_id})
    assert response_get.json()["data"][0]['trainer_name'] == 'Haimera'