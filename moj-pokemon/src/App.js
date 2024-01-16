import React, { useEffect } from 'react';
import './App.css';
import PokemonCard from './components/PokemonCard';
import { usePokemon } from './context/PokemonContext';

const AppContent = () => {
    const { pokemonData, fetchRandomPokemon, loading } = usePokemon();

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
                    className="reload-button-small reload-button"
                >
                    Idemo opet!
                </button>
            )}

            {loading && (
                <div className="spinner-container">
                    <div className="spinner">
                        <div></div>
                        <div></div>
                        <div></div>
                        <div></div>
                    </div>
                </div>)}          
        </div>
    );
};

const App = () => {
    return (
            <AppContent />
    );
};

export default App;
