import React from "react";

const PokemonCard = ({ pokemon }) => {

    var pokedexId = pokemon.id;
    var pokeSprites = pokemon.sprites;
    var pokeTypes = pokemon.types;

    const pokemonName = Object.keys(pokemon)[0];

    if (pokemonName) {
        const {id, sprites, types} = pokemon[pokemonName];

        pokedexId = id;
        pokeSprites = sprites;
        pokeTypes = types;
    }   

    

    return (
        <div className="pokemon-card">
            <img src={pokeSprites} alt={pokemonName} />

            <h2>{pokemonName}</h2>

            <p className="pokemon-info">Pokedex No. {pokedexId}</p>
            <p className="pokemon-info">Type: {pokeTypes.join(',')}</p>
        </div>
        );
    };

export default PokemonCard;