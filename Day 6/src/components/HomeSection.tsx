import React from "react";
import ScrollToTop from "./ScrolltoTop";
import ScrollToBottom from "./ScrolltoBottom";
import "../styles/home.css"

const HomeSection: React.FC = () => {
  return (
    <main>
      <ScrollToTop />
      <ScrollToBottom />
    <section className="min-h-screen flex flex-col justify-center items-center text-center  text-white px-4 sm:px-6 md:px-10">
      <h1 id ="hometext" className="text-5xl  text-blue-600 font-extrabold mb-4">
        Hi, I’m XYZ. Deligthful greetings(●'◡'●)
      </h1>
      <p id ="hometext" className="text-lg text-blue-600 max-w-2xl">
        some text Lorem ipsum dolor sit amet consectetur adipisicing elit.
        Maiores a fuga minus velit veniam consequuntur tempore quas. Ducimus
        fugit illo ex maiores dolore voluptas placeat dicta eos sed. Ipsa, a.
      </p>
    </section>
    </main>
  );
};

export default HomeSection;
