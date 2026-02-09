import React , {useState} from "react"; 
import SearchImg from '/search.png'; 
import Button from "./buttons"; 
import type {SearchBarProps,Prettify} from "../utils/typing"; 

/**
 * @component
 * @description Implements a Controlled Component search input that manages its own state, 
 * submits the final value via a callback, and resets the input after search.
 * * @param {SearchBarProps} props - The props object for the SearchBar component.
 * @param {(value: string) => void} props.onSearch - Callback function executed on form submission, receives the input value.
 * @param {string} [props.placeholder="Search anything you want"] - Placeholder text for the input field.
 * @param {React.CSSProperties} [props.inputStyle] - Custom inline CSS styles for the internal <input> element.
 * @param {string} [props.id] - Standard HTML id for the outer <form> element.
 * @param {React.CSSProperties} [props.barStyle] - Custom inline CSS styles for the main container (<form>).
 * @param {string} [props.image] - The URL for the search icon image.
 * * @returns {JSX.Element} A stylized search bar form containing an image, input, and button; This form also have the className. "Search-Bar 
 */
export default function SearchBar({ 
                                    onSearch,
                                    placeholder="Search anything you want",
                                    id, 
                                    inputStyle, 
                                    barStyle , 
                                    image
                            }:Prettify<SearchBarProps>){
    //IN LINE STYLE:  
    //#####################################################################################
     const INPUT_STYLE:React.CSSProperties = {...{
        backgroundColor: "transparent",
        width:"100%",
        height:"50%",
        padding: "7.5px  ", 
        borderRadius: "15px",
        border:"transparent",
        fontSize: "18px",
        color:"white",
        fontFamily:"Monserrat",
    }, ...inputStyle }

    Object.defineProperties

    let BAR_STYLE: React.CSSProperties = {...{
        border: "1px solid transparent",
        display: "flex",
        justifyContent: "space-around",
        flexDirection: "row" as const,
        gap: "2vw",
        backgroundColor: "#333",
        padding: "7.5px  ",
        width: "500px",
        borderRadius: "100px",
        fontFamily: "Monserrat",
    }, ...barStyle}

    
   //HOOKS
    //#####################################################################################
    const [text, textChanger] = useState<string>("")


    //FUNCTION 
    //#####################################################################################
    const handleChange = (event:React.ChangeEvent<HTMLInputElement>):void=>{
        
        const currentValue = event.target.value ; 
        textChanger(currentValue);
          
    }

    const handleSubmit = (event:React.FormEvent)=>{
        event.preventDefault();

        if (!text)return 

        textChanger(""); 
        onSearch(text); 
    }

    //This one just return us  the search bar HtmlInputElemt
    //#####################################################################################
    return(
        <>
        <form onSubmit={handleSubmit} style={BAR_STYLE} className="Search-Bar" id={id}>

                <div style={{height:"100%"}}> 
                    <img
                    src={image ||  SearchImg}
                    height="35px"
                    /> 
                    
                </div>

                <div>
                <input
                    style={INPUT_STYLE}
                    type="text"
                    value={text}
                    onChange={handleChange}
                    placeholder={placeholder}
                />
                </div>


                <div>
                <Button
                command={()=>undefined}
                type={"submit"}
                text={"Search"}
                title="Click to search"
                />
                </div>

        </form>
            
        </>
        
    )
}
