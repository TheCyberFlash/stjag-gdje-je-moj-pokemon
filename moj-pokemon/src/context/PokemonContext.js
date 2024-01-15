import { createContext, useContext, useState } from "react";

const PokemonContext = createContext();

export const PokemonProvider = ({ children }) => {
    const [pokemonData, setPokemonData] = useState(null);

    const fetchRandomPokemon = async () => {
        try {
            const response = await fetch('http://thecyberflash.pythonanywhere.com/get_random_pokemon');
            const data = await response.json();

            setPokemonData(data);
        } catch (error) {
            console.error('Error fetching Pokemon data:', error);
        }
    };

    return (
        <PokemonContext.Provider value={{ pokemonData, fetchRandomPokemon }}>
            {children}
        </PokemonContext.Provider>
    );
};

export const usePokemon = () => {
    const context = useContext(PokemonContext);
    if (!context) {
        throw new Error(
            "usePokemon must be used within a PokemonProvider"
        );
    }
    return context;
};
