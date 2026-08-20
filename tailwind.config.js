/** @type {import('tailwindcss').Config} */
export default {
  content: ['./index.html', './src/**/*.{js,ts,jsx,tsx}'],
  theme: {
    extend: {
      colors: {
        rebel: {
          50: '#f8f7ff',
          100: '#f0edff',
          200: '#ddd4ff',
          300: '#c9b1ff',
          400: '#ae7fff',
          500: '#8e4cff',
          600: '#7a28ff',
          700: '#6f0aff',
          800: '#5f00e6',
          900: '#4a00b3',
        },
      },
      animation: {
        'fade-in': 'fadeIn 0.3s ease-in',
        'slide-up': 'slideUp 0.3s ease-out',
      },
      keyframes: {
        fadeIn: {
          '0%': { opacity: '0' },
          '100%': { opacity: '1' },
        },
        slideUp: {
          '0%': { transform: 'translateY(10px)', opacity: '0' },
          '100%': { transform: 'translateY(0)', opacity: '1' },
        },
      },
    },
  },
  darkMode: 'class',
  plugins: [],
}
