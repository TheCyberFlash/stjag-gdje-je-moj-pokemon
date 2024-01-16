import React, {useRef, useEffect } from "react";

const SoundEffect = ({ src, play }) => {
    const audioRef = useRef();

    useEffect(() => {
        if (play) {
            audioRef.current.play();
        }
    }, [play]);
    
    return (
        <audio ref={audioRef} src={src} />
    );
}

export default SoundEffect;