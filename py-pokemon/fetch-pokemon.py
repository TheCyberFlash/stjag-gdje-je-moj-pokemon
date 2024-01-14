import requests
import json
import csv
import os

def fetch_pokemon_data(name):
    url = 'https://pokeapi.co/api/v2/pokemon/' + name
    response = requests.get(url)
    
    if response.status_code == 200:
        return extract_pokemon_data(response.json())
    else:
        print(f"Failed to fetch data for {name} from PokeAPI. Status code: {response.status_code}")
        return None
    
def extract_pokemon_data(response_json):
    pokemon_data = {
        "id": response_json["id"],
        "name": response_json["name"],
        "sprites": response_json["sprites"]["other"]["home"]["front_default"],
        "types": [type["type"]["name"] for type in response_json["types"]],
    }
    return pokemon_data

def update_pokemon_data(pokemon_list):
    if os.path.exists("pokemon.json") and os.path.getsize("pokemon.json") > 0:
        with open("pokemon.json", "r") as file:
            data = json.load(file)
    else:
        data = {}

    for pokemon in pokemon_list:
        data[pokemon["name"]] = pokemon

    with open("pokemon.json", "w") as file:
        json.dump(data, file, indent=2)

with open("moj-pokemon.csv", newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    pokemon_list = [{"name": row["name"].lower()} for row in reader]

for pokemon in pokemon_list:
    if os.path.exists("pokemon.json") and os.path.getsize("pokemon.json") > 0:
        with open("pokemon.json", "r") as file:
            existing_data = json.load(file)
            print(f"Existing data for {pokemon['name']}: {existing_data.get(pokemon['name'], 'Not found')}")
    else:
        existing_data = {}
        print("pokemon.json is empty or not present.")

    if pokemon["name"] not in existing_data:
        print(f"Fetching data for {pokemon['name']} from PokeAPI...")
        pokemon_data = fetch_pokemon_data(pokemon["name"])

        if pokemon_data:
            print(f"Updating Pokemon data for {pokemon['name']} in pokemon.json")
            update_pokemon_data([pokemon_data])

print("Pokemon data update complete.")
