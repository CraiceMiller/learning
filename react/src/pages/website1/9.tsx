import * as React from 'react';
import { useState } from 'react';
import Button  from "../../components/buttons"; 
import { Input,ComboBox,Radio,List} from "../../components/choices"


function Group <T extends React.Key>(list:T[][] ){

    const allList:React.JSX.Element[] = list.map(e=> <List values={e} />)
    console.log(allList)


    return (
        <div style={{border:"8px solid white",display:"flex" }} >

        </div>
    )
}


//creating an object with a type
type Character = {
    name:string, 
    gender:string, 
    age:number, 
    hairColor:string, 
    profesion:string, 
}
const Hersy: Character = { 
    name:"Hersy", 
    gender:"Male", 
    age:18, 
    hairColor:"yellow", 
    profesion:"student"
}

//or a Map
const Craice = new Map()
.set("name","Craice")
.set("age",18)
.set("gender","Female")
.set("hairColor","blue")
.set("profession","Student") ; 






export default  function App(){

    const click = (event:React.MouseEvent<HTMLInputElement>)=>{
        event.currentTarget.value ; 

    }

    let clickTimes:number = 0; 
    const [gender,setGender] = useState<string>(""); 

    const [character,setCharacter] = useState<Character>({name:"",age:0,gender:"",hairColor:"",profesion:""}); 

    const [element, setElement] = useState<React.JSX.Element>(<p> Hello</p>  )
    
    const elementHandler = ()=>{
        setElement(<List values={["hersy","Craice"]}/> )
    }

    const nameHandler = (event:React.ChangeEvent<HTMLInputElement>):void=>{
        setCharacter({...character,name:event.currentTarget.value})
    }
    const ageHandler = (event:React.ChangeEvent<HTMLInputElement>):void=>{
        setCharacter({...character,age:Number(event.currentTarget.value)})
    }
    const genderHandler = (event:React.ChangeEvent<HTMLInputElement>):void=>{
        setCharacter({...character,gender:event.currentTarget.value})
    }
    const professionHandler = (event:React.ChangeEvent<HTMLSelectElement>):void=>{
        setCharacter({...character,profesion:event.currentTarget.value})
    }


    const hairHandler = (event:React.ChangeEvent<HTMLInputElement>):void=>{
        setCharacter({...character,hairColor:event.currentTarget.value})
    }


    return ( 
        <>
        <h1>Update Object </h1>
        <p>24/10/2025 </p>
        <p style={{color:character.hairColor}} >
        You name is {character?.name},
        a {character?.gender} {character?.profesion} with  {character?.age} years old. And  your hair is  {character?.hairColor}. 
        </p>

        <Input type="text" value={character?.name} onChange={nameHandler} />
        <Radio name='gender' options={["Male","Female"]} value={character.gender} onChange={genderHandler}  />
        <ComboBox onChange={professionHandler} options={["Student","Employee","Teacher"]} value={character.profesion}  />
        <Input type="number" value={character.age} onChange={ageHandler} />
        <Input type="text" value={character.hairColor} onChange={hairHandler} />
        
       
        </>

    )
}


