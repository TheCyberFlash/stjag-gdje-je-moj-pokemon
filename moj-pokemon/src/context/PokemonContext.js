import { createContext, useContext, useState } from "react";

const PokemonContext = createContext();

export const PokemonProvider = ({ children }) => {
    const [pokemonData, setPokemonData] = useState(null);
    const [loading, setLoading] = useState(false);

    const fetchRandomPokemon = async () => {
        if (loading) return;

        try {
            setLoading(true);

            const response = await fetch('https://thecyberflash.pythonanywhere.com/get_random_pokemon');
            const data = await response.json();

            await new Promise(resolve => setTimeout(resolve, 2000));
            setLoading(false);

            setPokemonData(data);                       
        } catch (error) {
            console.error('Error fetching Pokemon data:', error);
        }
    };

    return (
        <PokemonContext.Provider value={{ pokemonData, fetchRandomPokemon, loading }}>
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
