import subprocess
from flask import Flask, jsonify
from flask_cors import CORS
import json
import os
import random

app = Flask(__name__)
CORS(app)

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
        # Return an error message if there is an exception while reading pokemon.json
        return f"Error reading pokemon.json: {str(e)}"

def update_pokemon_data():
    try:
        script_path = os.path.abspath(__file__)
        # Run the fetch-pokemon.py script using subprocess
        subprocess.run(["python", os.path.join(os.path.dirname(script_path), "fetch-pokemon.py")], check=True)
    except Exception as e:
        # Print an error message if there is an exception while updating pokemon data
        print(f"Error updating pokemon data: {str(e)}")

last_returned_pokemon = []

@app.route("/get_random_pokemon", methods=["GET"])
def get_random_pokemon():
    # Call the function to update pokemon data before processing the request
    update_pokemon_data()

    global last_returned_pokemon

    try:
        script_path = os.path.abspath(__file__)
        file_path = os.path.join(os.path.dirname(script_path), "pokemon.json")

        # Check if pokemon.json exists
        if not os.path.exists(file_path):
            return jsonify({"error": "pokemon.json not found."}), 500

        with open(file_path, "r") as file:
            data = json.load(file)

        available_pokemon = [name for name in data.keys() if name not in last_returned_pokemon]

        # If no available Pokemon, reset the list
        if not available_pokemon:
            last_returned_pokemon.clear()
            available_pokemon = list(data.keys())

        random_pokemon_name = random.choice(available_pokemon)
        random_pokemon = data[random_pokemon_name]

        last_returned_pokemon.append(random_pokemon_name)
        last_returned_pokemon = last_returned_pokemon[-3:]

        # Return a JSON response with the randomly selected Pokemon
        return jsonify({random_pokemon_name: random_pokemon})

    except Exception as e:
        # Return an error message if there is an exception while getting random pokemon
        return jsonify({"error": f"Error getting random pokemon: {str(e)}"}), 500

if __name__ == "__main__":
    # Call the function to update pokemon data before running the Flask app
    update_pokemon_data()
    # Run the Flask app on port 5000
    app.run(port=5000)
