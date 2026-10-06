/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,jsx}",
  ],
  theme: {
    extend: {
      colors: {
        'farm-green': '#16a34a',
        'farm-dark': '#14532d',
        'farm-light': '#dcfce7',
        'farm-earth': '#78350f',
        'farm-sun': '#fbbf24',
      },
    },
  },
  plugins: [],
}
