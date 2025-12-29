import { useState, useEffect } from 'react';

function getWindowDimensions() {
  const { innerHeight: height } = window;
  return { height };
}

export default function useWindowDimensions() {
  const [windowDimensions, setWindowDimensions] = useState(getWindowDimensions());

  useEffect(() => {
    function handleResize() {
      setWindowDimensions(getWindowDimensions());
    }

    // Add event listener to update dimensions on resize
    window.addEventListener('resize', handleResize);
    
    // Clean up the event listener when the component unmounts
    return () => window.removeEventListener('resize', handleResize);
  }, []); // Empty dependency array ensures the effect runs only once on mount

  return windowDimensions;
}
