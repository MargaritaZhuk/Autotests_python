import requests

URL = 'https://api.pokemonbattle.ru/v2/'
TRAINER_ID = '22593'
HEADERS = {'trainer_token' : '4165f2caeb000055f1b10e380fb69b82', 'Content-Type' : 'application/json'}

body_create = {
    "name": "One",
    "photo_id": 3
}

create_response = requests.post(url = f'{URL}pokemons', headers = HEADERS, json = body_create)
print(create_response.json()['id'])

pokemon_id = create_response.json()['id']

body_change = {
    "pokemon_id": pokemon_id,
    "name": "New Name",
    "photo_id": 2
}

body_catch = {
    "pokemon_id": pokemon_id
}

change_response = requests.put (url = f'{URL}pokemons', headers = HEADERS, json = body_change)
print(change_response.text)

catch_response = requests.post (url = f'{URL}trainers/add_pokeball', headers = HEADERS, json = body_catch)
print(catch_response.text)