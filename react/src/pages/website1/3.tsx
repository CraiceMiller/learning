import { useState } from 'react';
import Search from "../../components/searchBar.tsx"; 
import {toCapitalize, quickSort, binary} from "../../utils/utils.ts"; 
//import type {BinaryObject} from "../myjs/typing.ts"; 



const DataBase: string[] = [
    "Aarav", "Bianca", "Caleb", "Dahlia", "Elias", "Fiona", "Gael", "Hazel", "Ian", "Jasmine",
    "Kian", "Luna", "Milo", "Nora", "Owen", "Piper", "Quinn", "Riley", "Silas", "Tessa",
    "Ulysses", "Viola", "Wyatt", "Xyla", "Yusuf", "Zara", "Alaric", "Brynn", "Caspian", "Delilah",
    "Ezra", "Freya", "Gideon", "Harlow", "Indie", "Jude", "Kailani", "Leo", "Maia", "Nolan",
    "Octavia", "Pax", "Rhea", "Ronan", "Sage", "Skye", "Teagan", "Vance", "Willow", "Zane",
    "Amelia", "Brooks", "Clara", "Declan", "Elsie", "Finn", "Genevieve", "Holden", "Iris", "Julian",
    "Keira", "Liam", "Maren", "Nash", "Odette", "Phoenix", "Raquel", "Remy", "Savannah", "Theo",
    "Uma", "Victor", "Willa", "Xavier", "Yara", "Zachary", "Asher", "Blair", "Cora", "Damon",
    "Eden", "Felix", "Gianna", "Hayes", "Ivy", "Joel", "Kinsley", "Luca", "Meadow", "Neil",
    "Olive", "Prescott", "Quincy", "Rowan", "Sasha", "Sterling", "Thalia", "Vaughn", "Wren", "Zoe",
    "Hersy","Craice","Ashely","Miseru"
];

const names = quickSort(DataBase); 

function App() {
    const result = (value:string):boolean=>{
        //i created this function to sort and find the target :)
        //my function combined quickSort and binarySearch
        const found:number = binary(names,toCapitalize(value)); 
        return found !== -1 ;  
    
    }; 

    const [message, changeMessage] = useState<string>("Search an student :)");


  return (
    <div>
        <Search onSearch={(Name:string)=>{
            if(!Name){return ; }

            const found:string = result (Name)? `The studnet "${Name}" was found`:`That student "${Name}" is not here...`; 
            changeMessage(found)
        } }/>

        <p>{message} </p>
        
    </div>
    
  );
}

export default App;