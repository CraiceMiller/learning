import { useState } from "react";
import React from "react";
import {ComboBox, Radio,List,Input } from "../../components/choices"; 



export default function App() {
    const animes: string[] = ["nazo no kanojo x", "nichijou", "re-zero", "komi-san", "city", "full-metal alchemist", "Akino Sora"];
    const [Color, setColor] = useState<string>("none")
    const [text, setText] = useState<string>();
    const [Anime, setAnime] = useState<string>("");
    const [chose, setChose] = useState<string>("")
    const changeHandler = (event: React.ChangeEvent<HTMLInputElement>) => {
        setColor(event.currentTarget.value)
    }
    const textHandler = (event: React.ChangeEvent<HTMLTextAreaElement>) => {
        setText(event.currentTarget.value)
    }

    const animeHandler = (event: React.ChangeEvent<HTMLSelectElement>) => {
        setAnime(event.currentTarget.value)
    }

    const choiceHandler = (event: React.ChangeEvent<HTMLInputElement>) => {
        setChose(event.currentTarget.value)
    }


    return (
        <div style={{ display: "flex", flexDirection: "column" }} >

            <h1>On Change event </h1>
            <div style={{ backgroundColor: Color, height: "50px", width: "50px" }} ></div>
            <p>Current Color:   <big>{Color}</big> </p>
            <Input labelName="Type a color: "  onChange={changeHandler} value={Color} type="text" placeholder="Write a Color" />
            <textarea value={text} placeholder="write your comment" onChange={textHandler} />
            <p>Comment: {text} </p>


            <ComboBox  options={animes}  value={Anime} onChange={animeHandler} />
            <p>You chose this anime:  {Anime}</p>

            <p>Which one you are going to pick? </p>
            <Radio name="a" options={["Ram","Rem"] } value={chose} onChange={choiceHandler} />
            <p>So, you choose {chose}... </p>
            <List values={animes} />



        </div>
    )
}