import { StrictMode} from 'react' ; 
import { createRoot } from 'react-dom/client' ; 
import App from '@pages/website2' ; 
//import App from "./2"

 
createRoot(document.querySelector('#root')!).render(
  <StrictMode>
    <App/>
  </StrictMode>,
)

/**
webiste 2 structre start: 14/11/2025 at 13:00 hrs , Friday   ;
  src:
      -pages: 
          -website2: 
            1.tsx 
            2.tsx
        website2.tsx 
      -styles: 
        -StyleWebsite2: 
          props.css
        websiteStyle2.css
      -layouts: 
        -website2HF.tsx
    -main.tsx
  index.html

  ---------------------------------------------------

  website2.tsx  =>  main.tsx =>   index.html => Chrome 
  ---------------------------------------------------

 */

/**
 * material icon 
 * itelli code
 * super maven 
 */

//console.log("Bye world")