import subprocess
from flask import Flask, jsonify
import json
import os
import random

app = Flask(__name__)

@app.route("/")
def hello_world():
    # Get the absolute path to the current script
    script_path = os.path.abspath(__file__)

    # Construct the absolute path to pokemon.json
    file_path = os.path.join(os.path.dirname(script_path), "pokemon.json")

    # Check if the file exists
    if not os.path.exists(file_path):
        return "Error: pokemon.json not found."

    # Read the pokemon.json file
    try:
        with open(file_path, "r") as file:
            data = json.load(file)

        # Print the content for testing purposes
        print(data)

        # Return "Hello again..."
        return "Hello again..."

    except Exception as e:
        return f"Error reading pokemon.json: {str(e)}"

def update_pokemon_data():
    try:
        script_path = os.path.abspath(__file__)
        subprocess.run(["python", os.path.join(os.path.dirname(script_path), "fetch-pokemon.py")], check=True)
    except Exception as e:
        print(f"Error updating pokemon data: {str(e)}")

last_returned_pokemon = []

@app.route("/get_random_pokemon", methods=["GET"])
def get_random_pokemon():
    update_pokemon_data()

    global last_returned_pokemon

    try:
        script_path = os.path.abspath(__file__)
        file_path = os.path.join(os.path.dirname(script_path), "pokemon.json")

        if not os.path.exists(file_path):
            return jsonify({"error": "pokemon.json not found."}), 500

        with open(file_path, "r") as file:
            data = json.load(file)

        available_pokemon = [name for name in data.keys() if name not in last_returned_pokemon]

        if not available_pokemon:
            last_returned_pokemon.clear()
            available_pokemon = list(data.keys())

        random_pokemon_name = random.choice(available_pokemon)
        random_pokemon = data[random_pokemon_name]

        last_returned_pokemon.append(random_pokemon_name)
        last_returned_pokemon = last_returned_pokemon[-3:]

        return jsonify({random_pokemon_name: random_pokemon})

    except Exception as e:
        return jsonify({"error": f"Error getting random pokemon: {str(e)}"}), 500

if __name__ == "__main__":
    update_pokemon_data()
    app.run(port=5000)