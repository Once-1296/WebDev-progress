import React, { useState } from "react";
import emailjs from "@emailjs/browser";

const Contact: React.FC = () => {
  const [form, setForm] = useState({ name: "", email: "", message: "" });
  const [status, setStatus] = useState<string | null>(null);

  const handleChange = (
    e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>
  ) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setStatus("sending");
    try {
      await emailjs.send(
        import.meta.env.VITE_EMAILJS_SERVICE_ID,
        import.meta.env.VITE_EMAILJS_TEMPLATE_ID,
        {
          user_name: form.name,
          user_email: form.email,
          user_message: form.message,
        },
        import.meta.env.VITE_EMAILJS_PUBLIC_KEY
      );
      setStatus("success");
      setForm({ name: "", email: "", message: "" });
    } catch (err) {
      console.error("❌ EmailJS Error:", err);
      setStatus("error");
    }
  };

  return (
    <main className="container mx-auto px-4 sm:px-6 py-8 sm:py-12">
      <h2
        id="con_head"
        className="text-2xl sm:text-3xl font-semibold mb-8 text-center"
      >
        Contact Me💬
      </h2>

      <div className="max-w-4xl mx-auto grid sm:grid-cols-2 gap-8">
        {/* Contact Info */}
        <div
          id="con_1"
          className="bg-gray-200 p-4 sm:p-6 border rounded-xl shadow hover:shadow-lg transition"
        >
          <h3 className="text-lg sm:text-xl font-bold mb-4">Get in Touch</h3>
          <ul className="space-y-2 text-sm sm:text-base">
            <li>
              📧 Email:{" "}
              <a
                target="_blank"
                href="mailto:awwab.wadekar@gmail.com"
                className="underline"
              >
                awwab.wadekar@gmail.com
              </a>
            </li>
            <li>📞 Phone: +91-9987965492</li>
            <li>
              💻 GitHub:{" "}
              <a
                target="_blank"
                href="https://github.com/Once-1296"
                className="underline"
              >
                github.com/Once-1296
              </a>
            </li>
            <li>
              🔗 LinkedIn:{" "}
              <a
                target="_blank"
                href="https://www.linkedin.com/in/awwab-wadekar-a42a65330/"
                className="underline"
              >
                linkedin.com/in/awwab-wadekar
              </a>
            </li>
          </ul>
        </div>

        {/* Contact Form */}
        <div
          id="con_2"
          className="bg-gray-200 p-4 sm:p-6 border rounded-xl shadow hover:shadow-lg transition"
        >
          <h3 className="text-lg sm:text-xl font-bold mb-4">Send a Message</h3>
          <form onSubmit={handleSubmit} className="space-y-4">
            <input
              type="text"
              name="name"
              placeholder="Your Name"
              value={form.name}
              onChange={handleChange}
              className="w-full p-2 rounded bg-white border border-gray-400 focus:outline-none"
            />
            <input
              type="email"
              name="email"
              placeholder="Your Email"
              value={form.email}
              onChange={handleChange}
              className="w-full p-2 rounded bg-white border border-gray-400 focus:outline-none"
            />
            <textarea
              name="message"
              placeholder="Your Message"
              value={form.message}
              onChange={handleChange}
              className="w-full p-2 rounded bg-white border border-gray-400 h-28 sm:h-32 focus:outline-none"
            />
            <button
              type="submit"
              disabled={status === "sending"}
              className="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700 transition text-sm sm:text-base"
            >
              {status === "sending" ? "Sending..." : "Send"}
            </button>
          </form>

          {status === "success" && (
            <p className="text-green-500 mt-3 text-sm sm:text-base">
              ✅ Message sent successfully!
            </p>
          )}
          {status === "error" && (
            <p className="text-red-500 mt-3 text-sm sm:text-base">
              ❌ Something went wrong. Please try again.
            </p>
          )}
        </div>
      </div>
    </main>
  );
};

export default Contact;
