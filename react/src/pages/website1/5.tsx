import * as React from 'react';
import { useState, useEffect} from 'react';
import B from "../../components/buttons"; 
import {List} from "../../components/choices"; 
import Search from "../../components/searchBar"; 
import {quickSort,binary,range,enumerate} from "../../utils/utils"; 

//CONDITION RENDER
type A={
    isLogging:boolean, 
    name?:string
}

function Message({isLogging,name="Guess"}:A){
    const a = <h2>Welcome {name}</h2> ; 
    const b =<h2>You are not log in </h2> 


    return (
        isLogging ? a:b 
    )
    
}






export default  function App(){

    const animes:string[] = ["nazo no kanojo x","nichijou", "re-zero","komi-san", "city","full-metal alchemist", "Akino Sora"];
    const fruits:string[] = ["apple","Banna","coconut","pair "]
    const [m,ChangeM] = useState(""); 
    const [animesList, ChangeAnimeList] = useState<string[]>(animes); 
    const searchAnime = (element:string)=>{
        let result: number =binary(quickSort(animes),element); 
        result !== -1 ? ChangeAnimeList([element]) : ChangeM("No anime found"); 

    }

    const resetList = ()=>{
        ChangeAnimeList(animes); 
        ChangeM(""); 

    }

    console.log(enumerate(animes)); 

    
    return (
        <>
        <h1>TITLE 1</h1>
        <p>Hello world</p>
        <nav style={{border:"2px white solid", padding:"15px"}} >
            <p>Bye world</p>
            <p>{new Date().getFullYear()}</p>
            <Search barStyle={{width:"250px", height:"20px"}} onSearch={searchAnime} />
            <Message isLogging={false} name={"Ashely"}/>
            <Message isLogging={true}/>
            <List values={animesList} order={false} />
            <B command={resetList} text='rest List' />
            <p>{m}</p>
            <List values={fruits}/>
            <List values={range(10)}/>




        </nav>
        </>
    )
}
