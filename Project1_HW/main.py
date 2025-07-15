import requests

URL = 'https://api.pokemonbattle.ru/v2'
token = 'YOUR_TOKEN'
header = {'Content-Type': 'application/json', 'trainer_token' : token}


################ Быстрый нокаут (убрать ''' и добавить на всё остальное)

'''body_knockout_pokemon = {
        "pokemon_id": "355632"  ## Ввести актуальный ID живого
    }
knockout_response = requests.post(url=f'{URL}/pokemons/knockout', headers=header, json=body_knockout_pokemon
    )
print("\n=== Ответ на knockout ===")
print("Status:", knockout_response.status_code, knockout_response.reason)
print("Body:", knockout_response.json())'''

#######################################

# Создаем покемона
body_create_pokemon = {
    "name": "Podebitel",
    "photo_id": -1
}

response_create_pokemon = requests.post(url = f'{URL}/pokemons', headers = header, json = body_create_pokemon)

print("\n=== Ответ на создание покемона ===")
print("Status:", response_create_pokemon.status_code, response_create_pokemon.reason)
print("Body:", response_create_pokemon.json())

if response_create_pokemon.status_code == 201:
    pokemon_id = response_create_pokemon.json()['id']  # Получаем ID из ответа
    print(f"\nPokemon ID: {pokemon_id}")

# Изменяем покемона
body_change_pokemon = {
    "pokemon_id": str(pokemon_id), ### Автоматически подставляем ID из переменной выше
    "name": "Podebitel Snake",
    "photo_id": -1
}

response_change_pokemon = requests.put(url = f'{URL}/pokemons', headers = header, json = body_change_pokemon)
print("\n=== Ответ на изменение покемона ===")
print("Status:", response_change_pokemon.status_code, response_change_pokemon.reason)
print("Body:", response_change_pokemon.json())

# Ловим покемона
body_catch_pokemon = {
    "pokemon_id": str(pokemon_id)
}

response_catch_pokemon = requests.post(url = f'{URL}/trainers/add_pokeball', headers = header, json = body_catch_pokemon)
print("\n=== Ответ на поимку покемона ===")
print("Status:", response_catch_pokemon.status_code, response_catch_pokemon.reason)
print("Body:", response_catch_pokemon.json())
