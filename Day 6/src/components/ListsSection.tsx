import React from "react";
import ScrollToTop from "./ScrolltoTop";
import ScrollToBottom from "./ScrolltoBottom";
import "../styles/listpage.css"

const ListsSection: React.FC = () => {
  return (
    <main>
      <ScrollToTop />
      <ScrollToBottom />
      <section
        id="lists"
        className="container mx-auto px-4 sm:px-6 md:px-10 py-10 sm:py-12"
      >
        <h2 id="list_head" className="text-3xl font-semibold mb-8 text-center">
          List ahh shi
        </h2>

        <div className="max-w-5xl mx-auto grid md:grid-cols-2 gap-10">
          <div
            id="list_1"
            className="bg-gray-200 p-5 sm:p-6 rounded-xl shadow-sm border border-gray-200"
          >
            <h3 className="text-2xl font-bold mb-4">
              Gen 5 best nuzlocke mons
            </h3>
            <ul className="list-disc pl-5 space-y-2">
              <li>Excadrill</li>
              <li>Darmanitan</li>
              <li>Chandelure</li>
              <li>Haxorus</li>
              <li>Conkeldurr</li>
            </ul>
          </div>

          <div
            id="list_2"
            className="bg-gray-200 p-5 sm:p-6 rounded-xl shadow-sm border border-gray-200"
          >
            <h3 className="text-2xl font-bold mb-4">Pokemon regions</h3>
            <ul className="list-disc pl-5 space-y-2">
              <li>
                <b>1st</b> Sinnoh{" "}
              </li>
              <li>
                <b>2st</b> Unova
              </li>
            </ul>
          </div>
        </div>
      </section>
    </main>
  );
};

export default ListsSection;
