import { useEffect, useState } from "react";
import { FaAngleDoubleUp } from "react-icons/fa";
import useWindowDimensions from './getWindowDims';
import "../styles/scrollbuttons.css"

const ScrollToTop = () => {
  const [showScrollTopButton, setShowScrollTopButton] = useState(false);
  const { height } = useWindowDimensions();
  useEffect(() => {
    const onScroll = () => {
      const shouldShow = 10*window.scrollY > height;
      setShowScrollTopButton(shouldShow);
    };

    window.addEventListener("scroll", onScroll);

    return () => window.removeEventListener("scroll", onScroll);
  }, []);

//   useEffect(() => {
//     console.log("showScrollTopButton:", showScrollTopButton);
//   }, [showScrollTopButton]);

  const scrollTop = () => {
    window.scrollTo({ top: 0, behavior: "smooth" });
  };

  return (
    <>
      {showScrollTopButton && (
        <FaAngleDoubleUp
          className="top-btn"
          onClick={scrollTop}
        />
      )}
    </>
  );
};

export default ScrollToTop;
