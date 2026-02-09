import * as React from 'react';
import {useState} from "react"; 
import Button from "../../components/buttons"; 
import SearchImg from '/search.png';

const Home = ()=>{



    const onClick = (event:React.ChangeEvent<HTMLButtonElement>)=>{

    }

    const onSumbit = (event:React.FormEvent):void=>{
        event.preventDefault()

    }


    return (
        <div>
            <h1>Hello world</h1>
            <p>This is just a simple text to say 'Hello world :3' </p>
            <button value={"Hello"} >This button....</button>
            <form onSubmit={onSumbit} >
                <input type="text" />
            </form>

        </div>
    )
}

const About = ()=>{


    return (
        <div>
            <h1>About this world</h1>
            <button>Click me :v</button>
        </div>
    )
}


export default function App(){
    const [text,setText] = useState<string>("Hello")
    const click = (event:React.MouseEvent<HTMLButtonElement, MouseEvent>)=>{
        console.log(event.currentTarget.value); 
        setText("Button clicked"); 
 
    }

    const doubleClick = (event:React.MouseEvent<HTMLButtonElement, MouseEvent>)=>{
        event.currentTarget.textContent = "Stop clicke me :v";
        console.log("Click twice "); 



    }

    const click2 = (event:React.MouseEvent<HTMLImageElement,MouseEvent>)=>{
        setText("Hello"); 
        event.currentTarget.style.display = "None"

    }




    return (

        <>
        <h1>CLICK EVENT: BUTTONS</h1>
        <p>{text}</p>
        <Button text='click me :3' command={click} doubleClick={doubleClick} value={"Hersy"}/>
        <Button text='click me :3' command={click} doubleClick={doubleClick} value={"Craice"}/>
        <Button text='click me :3' command={click} doubleClick={doubleClick} value={"Ashley"}/>
        <button value={"I am a button"}>Click me :)</button>
        <img src={SearchImg} onClick={click2}/>

        </>
    )
}



/**Page.prototype.addData(
    {
        to:"/", 
        text:"Home Page", 
        element:Home 
    }, 
    {
        to:"/about", 
        text:"About Page", 
        element:About
    }, 
); 
*/
//console.log(Page.prototype.getData()); 