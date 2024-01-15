import subprocess
from flask import Flask, jsonify
import json
import random

app = Flask(__name__)

def update_pokemon_data():
    subprocess.run(["python", "fetch-pokemon.py"], check=True)

@app.route("/get_random_pokemon", methods=["GET"])
def get_random_pokemon():
    # update_pokemon_data()

    with open("pokemon.json", "r") as file:
        data = json.load(file)

    random_pokemon_name = random.choice(list(data.keys()))
    random_pokemon = data[random_pokemon_name]

    return jsonify({random_pokemon_name: random_pokemon})

if __name__ == "__main__":
    update_pokemon_data()
    app.run(port=5000)