import {useState} from "react"; 
import Button from "../../components/buttons"

export default function App(){
    const [counter, setCounter] = useState<number>(0);
    let text = counter < 0 ? "You are writting negative numbers..":"Just a number :3"; 

    const Increase = ()=>{
        setCounter(prevCount => prevCount + 1) ; 

    }

    const Dencrease = ()=>{
        setCounter(prevCount => prevCount - 1) ; 

    }

    const Reset = ()=>{
        setCounter(prevCount => prevCount = 0) ; 

    }

    return(
        
        <>
        <div> 
        <header><h1>COUNTER</h1></header>
        <div>
            <p>Current numbers NO. {counter}</p>
            <p>{text}</p>

            <div id="bn" style={{display:"flex",justifyContent:"space-around"}} >
                <Button text={"Increase me "} command={Increase} title="This just add one " />
                <Button text={"Dincrease me "} command={Dencrease}/>
                <Button text={"Restart"} command={Reset}/>

            </div>

        </div>
        </div>
        </>
    ); 
}