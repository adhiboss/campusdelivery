/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        cdh: {
          maroon: '#8B1E2F',
          dark: '#5A121E',
          light: '#F8F9FA'
        }
      }
    },
  },
  plugins: [],
}
