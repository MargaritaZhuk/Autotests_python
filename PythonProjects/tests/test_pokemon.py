import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2/'
TRAINER_ID = '22593'
HEADERS = {'trainer_token' : '4165f2caeb000055f1b10e380fb69b82', 'Content-Type' : 'application/json'}

def test_status_code ():
    response = requests.get (url = f'{URL}trainers', headers = HEADERS)
    assert response.status_code == 200

def test_trainer_ID ():
    response = requests.get (url = f'{URL}trainers', headers = HEADERS, params = {'trainer_id' : TRAINER_ID})
    assert response.json()['data'][0]['trainer_name'] == 'Ember Dawn'