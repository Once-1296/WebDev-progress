import React from "react";

const Footer: React.FC = () => {
  return (
    <footer className="mt-auto py-6 sm:py-8 bg-gray-800 text-gray-300 text-center px-4">
      <p className="text-sm sm:text-base">
        &copy; {new Date().getFullYear()}{" "}
        <span className="font-semibold">Awwab Wadekar</span>. All rights
        reserved.
      </p>
      <p className="text-xs sm:text-sm mt-2 text-gray-400">
        Built with <span className="font-medium text-gray-200">React</span>,{" "}
        <span className="font-medium text-gray-200">Tailwind CSS</span>, and{" "}
        <span className="font-medium text-gray-200">TypeScript</span>.
      </p>
    </footer>
  );
};
export default Footer;
