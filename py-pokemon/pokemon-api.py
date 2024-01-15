import subprocess
from flask import Flask, jsonify
import json
import random

app = Flask(__name__)

def update_pokemon_data():
    subprocess.run(["python", "fetch-pokemon.py"], check=True)

last_returned_pokemon = []

@app.route("/get_random_pokemon", methods=["GET"])
def get_random_pokemon():   

    global last_returned_pokemon
    
    with open("pokemon.json", "r") as file:
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

if __name__ == "__main__":
    update_pokemon_data()
    app.run(port=5000)