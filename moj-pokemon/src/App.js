import React, { useEffect, useState, useRef } from 'react';
import './App.css';
import PokemonCard from './components/PokemonCard';
import { usePokemon } from './context/PokemonContext';
import ConfettiComponent from './components/Confetti';
import useSound from 'use-sound';
import gruntBirthdayPartySound from './audio/grunt-birthday-party-sound-made-with-Voicemod-technology.mp3';

const AppContent = () => {
    const [confettiActive, setConfettiActive] = useState(false);
    const [playSound, setPlaySound] = useState(false);
    const { pokemonData, fetchRandomPokemon, loading } = usePokemon();
    const audioRef = useRef();

    const handleReload = () => {
        fetchRandomPokemon();
        triggerConfetti();        
    };

    const [play] = useSound(gruntBirthdayPartySound);

    const triggerConfetti = async () => {
        await new Promise(resolve => setTimeout(resolve, 2000));  
        play();      
        setConfettiActive(true);
        await new Promise(resolve => setTimeout(resolve, 5000));
        setConfettiActive(false);
    }


    return (
        <div className="app-container">
            <ConfettiComponent active={confettiActive} />
            
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
