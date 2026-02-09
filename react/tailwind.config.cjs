const colors = require('tailwindcss/colors') ; 
// tailwind.config.js
module.exports = {
  // CRITICAL: Tell Tailwind where your components/pages are located
  mode:"jit", 
  content: [
    "./index.html",
    "./src/styles/**/*",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  purge: [
    "./index.html",
    "./src/styles/**/*",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  darkMode:'class' , 
  theme: {
    extend: {
      //color 16/11/2025
      colors:{
        first:"#EDE7DB", 
        second:"#E8DFD0 ", 
        third:"#663322 ", 
        fourth:"#422E30", 
        fifth:"#CC8356", 
        gray:colors.trueGray,

       
          // --- 1. NEUTRAL COLORS (Blacks, Grays, and Whites) ---
          //2/12/2025 Tuesday
          // Used for text, backgrounds, borders. Organized from darkest (900) to lightest (50).
        neutral: { 
            1000: '#000000', // Pure Black
            950: '#050505', 
            910: '#0E0E0E', 
            900: '#0A0A0A', 
            850: '#101115', 
            800: '#121212',
            750: '#171717',
            700: '#181822', // Darkest background/text color
            600: '#31323e', 
            500: '#4E576A', // Mid-Gray
            400: '#667085',
            300: '#A1A1A1', // Light Gray text
            200: '#c1c3d2', // Very Light Gray
            100: '#F1F7F6', // Off-White background
            50:  '#F7F4F3', // Near White
          },
  
          // --- 2. PRIMARY (Dark Blue/Indigo Theme) ---
        primary: { 
            900: '#0D1433',
            800: '#171F55',
            600: '#274272',
            400: '#6C90C3', // Lightest shade
          },
  
          // --- 3. ACCENT (Bright Green/Teal Theme) ---
          // Used for CTAs, success, and highlights.
        accent: { 
            900: '#030F0F',
            800: '#021A1A',
            700: '#042222',
            600: '#02624C',
            500: '#2CC395', // Main highlight color
            400: '#00DF82', // Brightest highlight color
            100: '#33666A', // Used for a softer accent background
          },
          
          // --- 4. SYSTEM/STATUS COLORS ---
        error: { 
            900: '#0D0103',
            700: '#41020D',
            500: '#79081A', // Main red color
          },
        success: { 
            700: '#3F6115',
            500: '#A0BD63',
            300: '#C7CE59', // Lightest success green
          },
          
          // --- 5. SPECIALTY COLORS ---
        gold: {
            700: '#B88A44',
            500: '#E0AA3E', // Main gold color
            100: '#F9F395',
          },
        silver: {
            700: '#707072',
            500: '#818286',
            300: '#D0D1D6',
            100: '#FCFCFE',
        },
        
        
          
          // --- 6. UNUSED/MISC COLORS ---
          // Placing unique shades under generic names if they don't fit a scale
        purple: {
            700: '#3A025B', 
            500: '#60519b', // Main purple
            550: "#5A2E98",
            300: '#A89BF2',

        },

        'salala-palett':{
          400: '#3F6115', 
        300:'#A0BD63',
        200:'#C7CE59' ,
        100:'#F9F8F2', 
        }, 
        'purple-palett':{
          400:'#181822' , 
          300:'#60519b ', 
          200:'#31323e' , 
          100:'#c1c3d2' ,
        }


      }, 
      //Font Family 28 / 11 / 2025, Friday at 17:00 hrs. 
      fontFamily: {
        bebas: ["Bebas Neue",'sans-serif'],
        poppins:["Poppins",'sans-serif'], 
        montserrat:["Montserrat",'sans-serif'],
        "open-sans":["Open Sans"], 
        "style-script":["Style Script", 'cursive'], 
        roboto:["Roboto"],
        lato:["Lato"], 
        quicksand: ["Quicksand"], 
        nunito:["Nunito"], 
        raleway:["Raleway"], 
        pacifico:["Pacifico", 'cursive'], 
        'science-gothic':["Science Gothic"], 
        "special-gothic-expanded-one":["Special Gothic Expanded One"], 
        "dela-gothic-one":["Dela Gothic One"], 
        literata:["Literata"], 
        "instrument-serif":["Instrument Serif"], 
        "dancing-script":["Dancing Script"], 



      },

    },
  },
  plugins: [],
}