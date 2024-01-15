import requests
import json
import csv
import os

def fetch_pokemon_data(name):
    # Construct the URL for the PokeAPI based on the Pokemon name
    url = 'https://pokeapi.co/api/v2/pokemon/' + name
    # Make a GET request to the PokeAPI
    response = requests.get(url)
    
    if response.status_code == 200:
        # If the response status is successful, extract and return Pokemon data
        return extract_pokemon_data(response.json())
    else:
        # If the response status is not successful, print an error message and return None
        print(f"Failed to fetch data for {name} from PokeAPI. Status code: {response.status_code}")
        return None
    
def extract_pokemon_data(response_json):
    # Extract relevant information from the JSON response and return as a dictionary
    pokemon_data = {
        "id": response_json["id"],
        "name": response_json["name"],
        "sprites": response_json["sprites"]["other"]["home"]["front_default"],
        "types": [type["type"]["name"] for type in response_json["types"]],
    }
    # Print a message indicating the extracted Pokemon data
    print(f"Extracted Pokemon data: {pokemon_data}")
    return pokemon_data

def update_pokemon_data(pokemon_list):
    # Check if pokemon.json exists and has data; if not, initialize an empty dictionary
    if os.path.exists("pokemon.json") and os.path.getsize("pokemon.json") > 0:
        with open("pokemon.json", "r") as file:
            data = json.load(file)
    else:
        data = {}

    # Update the Pokemon data dictionary with new data
    for pokemon in pokemon_list:
        data[pokemon["name"]] = pokemon

    # Write the updated data back to pokemon.json
    with open("pokemon.json", "w") as file:
        json.dump(data, file, indent=2)
    # Print a message indicating the update and then sort the data
    print("Updated Pokemon data in pokemon.json")
    sort_pokemon_json()

def sort_pokemon_json():
    # Read the data from pokemon.json, sort it by 'id', and rewrite it
    with open("pokemon.json", "r") as file:
        data = json.load(file)

    sorted_data = dict(sorted(data.items(), key=lambda x: x[1]["id"]))

    with open("pokemon.json", "w") as file:
        json.dump(sorted_data, file, indent=2)
    # Print a message indicating the sorting
    print("Sorted pokemon.json by 'id'")

# Read Pokemon names from moj-pokemon.csv
with open("moj-pokemon.csv", newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    # Convert names to lowercase and create a list of dictionaries
    pokemon_list = [{"name": row["name"].lower()} for row in reader]

# Process each Pokemon in the list
for pokemon in pokemon_list:
    # Check if pokemon.json exists and has data; if yes, display existing data for the Pokemon
    if os.path.exists("pokemon.json") and os.path.getsize("pokemon.json") > 0:
        with open("pokemon.json", "r") as file:
            existing_data = json.load(file)
            print(f"Existing data for {pokemon['name']}: {existing_data.get(pokemon['name'], 'Not found')}")
    else:
        # If pokemon.json is empty or not present, initialize an empty dictionary
        existing_data = {}
        print("pokemon.json is empty or not present.")

    # If the Pokemon is not in the existing data, fetch and update its data
    if pokemon["name"] not in existing_data:
        print(f"Fetching data for {pokemon['name']} from PokeAPI...")
        pokemon_data = fetch_pokemon_data(pokemon["name"])

        if pokemon_data:
            # If data is fetched successfully, update the Pokemon data in pokemon.json
            print(f"Updating Pokemon data for {pokemon['name']} in pokemon.json")
            update_pokemon_data([pokemon_data])

# Print a message indicating the completion of Pokemon data update
print("Pokemon data update complete.")
