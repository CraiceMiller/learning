import { defineConfig } from 'vite' ; 
import react from '@vitejs/plugin-react' ; 
//import * as Path from 'path' ; 
import tsconfigPaths from 'vite-tsconfig-paths';//This will update all my tsconfigure path 5/11/205
//import tailwindcss from '@tailwindcss/vite' ; //will update the tailwind config, 15/11/2025

// https://vite.dev/config/
export default defineConfig({
  plugins: [
    react({
      babel: {
        plugins: [['babel-plugin-react-compiler']],
      },
    }),
    tsconfigPaths(),
    //tailwindcss(),
  ],
  //3/11/2025
  server: {
    proxy: {
      // When the browser requests '/api', Vite forwards it to the Duck API
      '/api': {
        target: 'https://random-d.uk',
        changeOrigin: true, // This is essential for CORS
        rewrite: (path) => path.replace(/^\/api/, ''), // Removes '/api' from the actual request path
      },
      '/data':{
        target: 'https://random.dog', 
        changeOrigin:true,
        rewrite: (p)=>p.replace(/^\/api/,'' )

      }
    },
    //4-12-2025 Thursday
    //host:true, 

  },
  //05/11/2025 Alias Path 
  /**resolve:{
    alias:{
      '@myjs':Path.resolve(__dirname, './myjs'), 

    }
  }*/
})

