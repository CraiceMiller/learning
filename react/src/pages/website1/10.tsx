import * as React from 'react';
import { useState } from 'react';
import {List} from "../../components/choices"; 
import Search from "../../components/searchBar"; 
import { range} from "../../utils/utils"; 


export default function App(){
    const animes:string[] = ["Clevates", "nazo no kanojo x","nichijou", "re-zero","komi-san", "city","full-metal alchemist", "Akino Sora"];

    const [animesList, ChangeAnimeList] = useState<string[]>(animes); 

    const addItem  = (event:string)=>{

        ChangeAnimeList((prev)=>{
            return [...prev, event]
        })
    }

    const remove = (event:React.MouseEvent<HTMLLIElement>)=>{
        console.log(event)
        const data = event.currentTarget.textContent ; 
                if (data === null) return  ;
        
        ChangeAnimeList(prev =>{
            return prev.filter( (value)=>{
                return value !== data ; 
            })
        })

    }

    return (
        <div>
            <h1>Update Array</h1>
            <List values={animesList} order={true} valueClicked={remove} />
            <Search onSearch={addItem} />
            <List values={range(2)} valueClicked={remove} />

        </div>
        
    )
}