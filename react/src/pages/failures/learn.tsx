import print from "../../utils/utils.ts"; 
import {enumerate} from "../../utils/utils.ts"; 
import Header from "../../layouts/Header.tsx"; 
import { StrictMode } from 'react'; 
import { createRoot } from 'react-dom/client';
import './styles/index.css';  


const now= new Date().toString();
function App(){
    return (
        <> 
        <Header/>
        <p>{now}</p>
        <button>Click me  :)</button>
        </>
    )
}; 

 
console.log("Bye world"); 
//print("Waht am i doing here...")
print("I dunno what i am doing here...");
for (const i of enumerate(["Danie", "Hersy", "Craice", "Ashley"])){
    print(i); 
}; 
print("Everything is okay here, later to a lot of effor :3")
print("At least my module works :), but now my app... :(")




//This is the main cause will 
//import './index.css'
//import App from './App.tsx'

createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <App />
  </StrictMode>,
); 
