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

    const capitalizedFirstLetter = pokemonName.charAt(0).toUpperCase() + pokemonName.slice(1);
    const capitalizedTypes = pokeTypes.map(type => type.charAt(0).toUpperCase() + type.slice(1));
    return (
        <div className="pokemon-card">
            <img src={pokeSprites} alt={capitalizedFirstLetter} />

            <h2>{capitalizedFirstLetter}</h2>

            <p className="pokemon-info">Pokedex No. {pokedexId}</p>
            <p className="pokemon-info">Type: {capitalizedTypes.join(', ')}</p>
        </div>
        );
    };

export default PokemonCard;