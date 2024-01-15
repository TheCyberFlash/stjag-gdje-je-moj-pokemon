import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import { PokemonProvider } from './context/PokemonContext';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
    <PokemonProvider>
        <App />
    </PokemonProvider>
);


