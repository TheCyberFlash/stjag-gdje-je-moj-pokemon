import React from 'react';
import Confetti from 'react-confetti';
import useWindowSize from 'react-use/lib/useWindowSize';

const ConfettiComponent = ({ active }) => {

    const { width, height } = useWindowSize();

  return (
    <div className="confetti-container">
        <Confetti
            width={width}
            height={height}
            numberOfPieces={active ? 200 : 0}
        />
    </div>
  );
};

export default ConfettiComponent;
