import React from "react";
import ScrollToTop from "./ScrolltoTop";
import ScrollToBottom from "./ScrolltoBottom";
import "../styles/new_page.css";

const SomeNewPage: React.FC = () => {
  // Define the type for the props if needed, or use React.FC for functional components
  interface CustomDivProps {
    count: number;
  }

  const RepeatCustomDiv: React.FC<CustomDivProps> = ({ count }) => {
    // Use Array(count).fill(0) to create an array of a specific length.
    // The second argument in map (index) is used for the key.
    const customDivs = Array(count)
      .fill(0)
      .map((_, index) => (
        // A unique key is essential for React list rendering
        <div key={index} className="custom-div-element">
          <div
            id="box"
            className="bg-gray-200 p-5 sm:p-6 rounded-xl shadow-sm border border-gray-200"
          >
            <h3 className="text-lg sm:text-xl font-bold mb-2">Sub Heading</h3>
            <p>
              Lorem ipsum dolor sit amet consectetur adipisicing elit. Quaerat,
              beatae id? Earum, molestiae officiis in, inventore obcaecati atque
              maiores mollitia expedita odit corrupti amet sunt accusamus
              exercitationem officia tenetur itaque.
            </p>
            <p>
              Lorem ipsum dolor sit amet consectetur adipisicing elit. Quaerat,
              beatae id? Earum, molestiae officiis in, inventore obcaecati atque
              maiores mollitia expedita odit corrupti amet sunt accusamus
              exercitationem officia tenetur itaque.
            </p>{" "}
            <p>
              Lorem ipsum dolor sit amet consectetur adipisicing elit. Quaerat,
              beatae id? Earum, molestiae officiis in, inventore obcaecati atque
              maiores mollitia expedita odit corrupti amet sunt accusamus
              exercitationem officia tenetur itaque.
            </p>{" "}
            <p>
              Lorem ipsum dolor sit amet consectetur adipisicing elit. Quaerat,
              beatae id? Earum, molestiae officiis in, inventore obcaecati atque
              maiores mollitia expedita odit corrupti amet sunt accusamus
              exercitationem officia tenetur itaque.
            </p>{" "}
            <p>
              Lorem ipsum dolor sit amet consectetur adipisicing elit. Quaerat,
              beatae id? Earum, molestiae officiis in, inventore obcaecati atque
              maiores mollitia expedita odit corrupti amet sunt accusamus
              exercitationem officia tenetur itaque.
            </p>{" "}
            <p>
              Lorem ipsum dolor sit amet consectetur adipisicing elit. Quaerat,
              beatae id? Earum, molestiae officiis in, inventore obcaecati atque
              maiores mollitia expedita odit corrupti amet sunt accusamus
              exercitationem officia tenetur itaque.
            </p>{" "}
            <p>
              Lorem ipsum dolor sit amet consectetur adipisicing elit. Quaerat,
              beatae id? Earum, molestiae officiis in, inventore obcaecati atque
              maiores mollitia expedita odit corrupti amet sunt accusamus
              exercitationem officia tenetur itaque.
            </p>{" "}
            <p>
              Lorem ipsum dolor sit amet consectetur adipisicing elit. Quaerat,
              beatae id? Earum, molestiae officiis in, inventore obcaecati atque
              maiores mollitia expedita odit corrupti amet sunt accusamus
              exercitationem officia tenetur itaque.
            </p>{" "}
            <p>
              Lorem ipsum dolor sit amet consectetur adipisicing elit. Quaerat,
              beatae id? Earum, molestiae officiis in, inventore obcaecati atque
              maiores mollitia expedita odit corrupti amet sunt accusamus
              exercitationem officia tenetur itaque.
            </p>{" "}
            <p>
              Lorem ipsum dolor sit amet consectetur adipisicing elit. Quaerat,
              beatae id? Earum, molestiae officiis in, inventore obcaecati atque
              maiores mollitia expedita odit corrupti amet sunt accusamus
              exercitationem officia tenetur itaque.
            </p>
          </div>
          <br></br>
          <br></br>
        </div>
      ));

    return <div className="container">{customDivs}</div>;
  };
  return (
    <main className="container mx-auto px-4 sm:px-6 py-8 sm:py-12">
      <ScrollToTop />
      <ScrollToBottom />
      <h2
        id="title_head"
        className="text-2xl sm:text-3xl font-semibold mb-8 text-center"
      >
        {" "}
        Title:{" "}
      </h2>
      <RepeatCustomDiv count={5} />
    </main>
  );
};

export default SomeNewPage;
