import React from "react";
import ScrollToTop from "./ScrolltoTop";
import ScrollToBottom from "./ScrolltoBottom";
import "../styles/about.css"

const AboutSection: React.FC = () => {
  return (
    <main>
        <ScrollToTop />
        <ScrollToBottom />
        <section
          id="about"
          className="container mx-auto px-4 sm:px-6 md:px-10 py-10 sm:py-12"
        >
          <h2
            id="about_head"
            className="text-2xl sm:text-3xl font-semibold mb-8 text-center"
          >
            About Me😎
          </h2>

          <div className="max-w-4xl mx-auto space-y-10">
            
            {/* Background */}
            <div id="about_bg" className="about">
              <h3 className="text-lg sm:text-xl font-bold mb-2">Background</h3>
              <p className="text-sm sm:text-base leading-relaxed">
⠸⣷⣦⠤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣠⣤⠀⠀⠀
⠀⠙⣿⡄⠈⠑⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠔⠊⠉⣿⡿⠁⠀⠀⠀
⠀⠀⠈⠣⡀⠀⠀⠑⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠊⠁⠀⠀⣰⠟⠀⠀⠀⣀⣀
⠀⠀⠀⠀⠈⠢⣄⠀⡈⠒⠊⠉⠁⠀⠈⠉⠑⠚⠀⠀⣀⠔⢊⣠⠤⠒⠊⠉⠀⡜
⠀⠀⠀⠀⠀⠀⠀⡽⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠩⡔⠊⠁⠀⠀⠀⠀⠀⠀⠇
⠀⠀⠀⠀⠀⠀⠀⡇⢠⡤⢄⠀⠀⠀⠀⠀⡠⢤⣄⠀⡇⠀⠀⠀⠀⠀⠀⠀⢰⠀
⠀⠀⠀⠀⠀⠀⢀⠇⠹⠿⠟⠀⠀⠤⠀⠀⠻⠿⠟⠀⣇⠀⠀⡀⠠⠄⠒⠊⠁⠀
⠀⠀⠀⠀⠀⠀⢸⣿⣿⡆⠀⠰⠤⠖⠦⠴⠀⢀⣶⣿⣿⠀⠙⢄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢻⣿⠃⠀⠀⠀⠀⠀⠀⠀⠈⠿⡿⠛⢄⠀⠀⠱⣄⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢸⠈⠓⠦⠀⣀⣀⣀⠀⡠⠴⠊⠹⡞⣁⠤⠒⠉⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣠⠃⠀⠀⠀⠀⡌⠉⠉⡤⠀⠀⠀⠀⢻⠿⠆⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠰⠁⡀⠀⠀⠀⠀⢸⠀⢰⠃⠀⠀⠀⢠⠀⢣⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢶⣗⠧⡀⢳⠀⠀⠀⠀⢸⣀⣸⠀⠀⠀⢀⡜⠀⣸⢤⣶⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠈⠻⣿⣦⣈⣧⡀⠀⠀⢸⣿⣿⠀⠀⢀⣼⡀⣨⣿⡿⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠈⠻⠿⠿⠓⠄⠤⠘⠉⠙⠤⢀⠾⠿⣿⠟⠋  

              </p>
            </div>

            {/* Education */}
            <div id="about_tm" className="about">
              <div className="relative before:content-[''] before:absolute before:left-2 before:top-0 before:w-0.5 before:h-full before:bg-gray-300 pl-6">
                <section id="education" className="py-4 sm:py-8">
                  <h3 className="text-xl sm:text-2xl font-semibold mb-6">
                    Education
                  </h3>

                  <div className="space-y-6 text-gray-700 text-sm sm:text-base">
                    {/* stuff 1 */}
                    <div className="border-l-4 border-blue-600 pl-4">
                      <h4 className="font-bold">
                        YO<sup>YO</sup> HO HO
                      </h4>
                      <p>some fire</p>
                      <p className="italic">style</p>
                      <p className="mt-1">
                        Score <span className="font-semibold">67</span> —{" "}
                        <span className="text-gray-600">Ohio 420</span>
                      </p>
                    </div>

                    {/* stuff 2 */}
                    <div className="border-l-4 border-green-600 pl-4">
                      <h4 className="font-bold">
                        COME<sup>ON</sup> IK ZO
                      </h4>
                      <p>fill shi</p>
                      <p className="italic">timeline ehhh</p>
                      <p className="mt-1">
                        HE'S OVER <span className="font-semibold">9000%</span> —{" "}
                        <span className="text-gray-600">AHHHH </span>
                      </p>
                      <p className="text-gray-500 text-xs sm:text-sm">
                        (ZA WARUDO)
                      </p>
                    </div>

                    {/* stuff 3 */}
                    <div className="border-l-4 border-purple-600 pl-4">
                      <h4 className="font-bold">TRICK MASTER</h4>
                      <p>THE HUNTERS WORLD CHUNIN EXAM</p>
                      <p className="italic">
                        cREATIVITY—{" "}
                        <span className="text-gray-600">
                          -4.9 billion ~ now
                        </span>
                      </p>
                      <p className="mt-1">
                        YEAH ME TIRED
                        <span className="font-semibold">6.74206934</span>
                      </p>
                    </div>
                  </div>
                </section>
              </div>
            </div>
            {/* additional stuff */}
            <div id="about_hb" className="about">
              <h3 className="text-lg sm:text-xl font-bold mb-2">Hobbies</h3>
              <p className="text-sm sm:text-base leading-relaxed">
                Janet Yellen is Biden’s employee-of-the-year. In a year when the
                US government was facing a near-record budget deficit while
                long-term interest rates were blowing out, Yellen devised an
                ingenious way to secure trillions of dollars in funding for the
                government without breaking the US long-term debt market. This
                issue describes Yellen’s Trillion-Dollar Magic Trick.
              </p>
            </div>
             <div id="about_hb" className="about">
              <h3 className="text-lg sm:text-xl font-bold mb-2">Hobbies</h3>
              <p className="text-sm sm:text-base leading-relaxed">
                Janet Yellen is Biden’s employee-of-the-year. In a year when the
                US government was facing a near-record budget deficit while
                long-term interest rates were blowing out, Yellen devised an
                ingenious way to secure trillions of dollars in funding for the
                government without breaking the US long-term debt market. This
                issue describes Yellen’s Trillion-Dollar Magic Trick.
              </p>
            </div>
             <div id="about_hb" className="about">
              <h3 className="text-lg sm:text-xl font-bold mb-2">Hobbies</h3>
              <p className="text-sm sm:text-base leading-relaxed">
                Janet Yellen is Biden’s employee-of-the-year. In a year when the
                US government was facing a near-record budget deficit while
                long-term interest rates were blowing out, Yellen devised an
                ingenious way to secure trillions of dollars in funding for the
                government without breaking the US long-term debt market. This
                issue describes Yellen’s Trillion-Dollar Magic Trick.
              </p>
            </div>
          </div>
          
        </section>
    </main>
  );
};

export default AboutSection;
