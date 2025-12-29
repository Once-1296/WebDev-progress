import { useEffect, useState } from "react";
import { FaAngleDoubleDown } from "react-icons/fa";
import useWindowDimensions from './getWindowDims';
import "../styles/scrollbuttons.css"

const ScrollToBottom = () => {
  const [showScrollBottomButton, setShowScrollBottomButton] = useState(false);
  const { height } = useWindowDimensions();

  useEffect(() => {
    const onScroll = () => {
      const shouldShow = window.scrollY < document.body.scrollHeight - height ;
      setShowScrollBottomButton(shouldShow);
    };

    window.addEventListener("scroll", onScroll);

    return () => window.removeEventListener("scroll", onScroll);
  }, []);

  // useEffect(() => {
  //   console.log("showScrollBottomButton:", showScrollBottomButton);
  // }, [showScrollBottomButton]);

  const scrollBottom = () => {
    window.scrollTo({ top: document.body.scrollHeight, behavior: "smooth" });
  };

  return (
    <>
      {showScrollBottomButton && (
        <FaAngleDoubleDown
          className="bottom-btn"
          onClick={scrollBottom}
        />
      )}
    </>
  );
};

export default ScrollToBottom;
