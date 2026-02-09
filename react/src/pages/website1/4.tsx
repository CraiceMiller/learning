import Bar from "../../components/searchBar";
import {useState} from "react";
import Button from "../../components/buttons";


export default function App(){

    const [message, changeMessage] = useState<string>("Hello i am just a paragraph :3")

    return (
        <>
        <Bar
        onSearch={(v)=>changeMessage(v)}
        placeholder="I am a small search"
        barStyle={{
            height:"30px",
            width:"250px",
            borderRadius: "0px",
        }}
        />

    <Bar
    onSearch={(v)=>changeMessage(v)}
    placeholder="Hello i am the defaul search bar :)"
    />

        <Bar
            onSearch={(v)=>changeMessage(v)}
            placeholder="I am a big search"
            barStyle={{
                height:"30px",
                width:"600px",
            }}
        />

       
        <button >I am a normal button ... </button>

        <Button text="I am a component button " />


        <p>{message}</p>
        </>



    )
}

