import React from "react";

const PokemonCard = ({ pokemon }) => {
    return (
        <div className="pokemon-card">
            <img src={pokemon.sprites.front_default} alt={pokemon.name} />

            <h2>{pokemon.name}</h2>

            <p className="pokemon-info">Pokedex No. {pokemon.id}</p>
            <p className="pokemon-info">Type: {pokemon.types.join(',')}</p>
        </div>
        );
    };

export default PokemonCard;