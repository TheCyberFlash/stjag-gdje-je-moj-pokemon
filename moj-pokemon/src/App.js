import React, { useEffect } from 'react';
import './App.css';
import PokemonCard from './components/PokemonCard';
import { usePokemon } from './context/PokemonContext';

const AppContent = () => {
    const { pokemonData, fetchRandomPokemon } = usePokemon();
    console.log(pokemonData);

    useEffect(() => {
        fetchRandomPokemon();
    }, [fetchRandomPokemon]);

    const handleReload = () => {
        fetchRandomPokemon();
    };

    return (
        <div className="app-container">
            {pokemonData ? (
                <PokemonCard pokemon={pokemonData} />
            ) : (
                <button 
                    onClick={handleReload} 
                    className="reload-button"
                >
                    GDJE JE MOJ
                    <br />
                    POKEMON
                </button>
            )}

            {pokemonData && (
                <button 
                    onClick={handleReload} 
                    className="reload-button"
                >
                    Idemo opet!
                </button>
            )}          
        </div>
    );
};

const App = () => {
    return (
            <AppContent />
    );
};

export default App;
