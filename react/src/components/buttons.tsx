//import React from "react"; 
import type {ButtonProps} from "../utils/typing.js";  


/**
 * @component
 * @description A customizable button primitive that merges default styles with styles 
 * provided by the 'style' prop.
 * * @param {ButtonProps} props - The props object for the Button component.
 * @param {string} [props.text="Button"] - The text displayed inside the button.
 * @param {()=>void} [props.command] - The function executed when the button is clicked.
 * @param {string} [props.title] - Tooltip text for the button.
 * @param {"button"|"submit"|"reset"} [props.type] - Standard HTML button type.
 * @param {React.CSSProperties} [props.style] - Custom inline CSS styles to override defaults.
 * @param {string} [props.id] - Standard HTML id attribute.
 * @param {string} [props.className="Button"] - Standard HTML class attribute.
 * * @returns {JSX.Element} A button element. with the className "Button"
 */
export default function Button(props:ButtonProps){
    const BUTTON_STYLE:React.CSSProperties = {
    ...{
        borderRadius: "20px",
        border: "1px solid transparent",
        padding: "10px",
        fontSize: "1em",
        fontWeight: "bold",
        width:"95%",
        height:"85%",
        fontFamily: "inherit",
        backgroundColor: "#1a1a1a",
        color:"#ffffff"
    },...props.style,}

    return(
        <div className={props.className}  > 
            <button
            style={props.withStyle ?BUTTON_STYLE:undefined}
            onClick={props.command}
            title={props.title}
            type={props.type}
            id={props.id}
            value={props.value}
            onDoubleClick={props.onDoubleClick}
            hidden={props.hidden}
            className={`Button ${props.className || ''} `}
            >
                <p>{props.text} </p>
            </button>
        </div >
    )
}

