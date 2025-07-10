/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        'telco-dark-blue': '#0A192F',
        'telco-light-blue': '#172A45',
        'telco-slate': '#8892b0',
        'telco-light-slate': '#a8b2d1',
        'telco-green': '#64ffda',
        'telco-white': '#ccd6f6',
      }
    },
  },
  plugins: [],
}
