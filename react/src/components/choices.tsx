import type {InputProps,ComboBoxProps,RadioProps,listProps,ToggleProps, FormProps} from "../utils/typing.ts";  
import React,{ useState } from "react";
export type {InputProps,ComboBoxProps,RadioProps,listProps,ToggleProps, FormProps} ; 

//REDNDER LIST 
/**
 * A generic component for rendering a list of items as either an ordered or unordered list.
 * * @component
 * @template Item - The type of the values in the array, which must extend React.Key (string or number).
 * @param {listProps<Item>} props - The component props.
 * @param {Item[]} props.values - The array of items to display. Each item is used as the content of an <li> and its key.
 * @param {boolean} [props.order=false] - Whether to render an ordered list (<ol>) or an unordered list (<ul>).
 * @returns {React.JSX.Element} A div containing either an <ol> or a <ul> element.
 * within the classNmae "Render-List"
 */
export function List<Item extends React.ReactNode>(props:listProps<Item>):React.JSX.Element{

    const listItems:React.JSX.Element[]= props.values.map<React.JSX.Element>((value,index ) => 
        <li
        key={index as React.Key}
        onClick={ props.valueClicked}
        >
            {value  }
        </li> 
    ); 



    return (
        <div id={props.id} className='Render-List' >
            {props.order ?<ol>{listItems}</ol>:<ul>{listItems}</ul> }

        </div>

    )
    
}



//{labelName,placeholder,type,className,name,value,onChange}
/**Class Name "Input" */
export function Input(props:InputProps){
    let direction:'left' | 'right' = props.labelDirection || 'left' ;
    const Label = <label >{props.labelName}</label> ; 
    const CurrentInput = 
                        <input 
                        type={props.type}
                        placeholder={props.placeholder}
                        name={props.name}
                        value={props.value}
                        onChange={props.onChange}
                        id={props.id}
                        disabled={props.disabled}
                        />
    
    return (
        <div className={props.className ||  "Input"} >
            {direction === 'left' ? <>{Label}{CurrentInput}</> : <>{CurrentInput}{Label}</> }
        </div>
    )


}
//26/10/2025
/**Class Name "Form" */
export function Form(props:FormProps):React.JSX.Element{
    const [value,setValue] = useState<string>(""); 
 
    const formHandler = (event:React.FormEvent)=>{
        event.preventDefault() ; 
        props.onSend(value)
        setValue(prev => prev = "" ); 
    }
    const changeHandler = (event:React.ChangeEvent<HTMLInputElement>)=>{
        let v:string = event.currentTarget.value ; 
        setValue(prev => prev = v ); 
    }

    return (
        <form name={props.name} onSubmit={formHandler} id={props.id} className={props.className || 'Form' } >
            <input
            className={props.className}
            placeholder={props.placeholder}
            type={props.type}
            value={value}
            required={props.required}
            onChange={changeHandler}
            />

            <button
            className={"Button"}
            type="submit"
            >
            {props.text}
            </button>

        </form>
    )
}

/**Class Name "ComboBox", React.memo 9/11/2025 */
export const  ComboBox =React.memo ((props: ComboBoxProps) =>{
    console.log('The ComboBox component was re-render :| ');
    
    const listValues = props.options.map(element => <option value={element} key={element} >{element}</option>)
    return (
        <div  id = {props.id} >
            <select
            className={props.className || "ComboBox"}
            value={props.value}
            onChange={props.onChange} >
                {listValues}
            </select>
        </div>
    )
})
/**Class Name "Radio" */
export function Radio(props: RadioProps) {

    const radiosOptions = props.options.map(element => {
        return(
            <div className={props.className || "Radio" }>
                <label >
                    <input
                    key={element}
                    type="radio"
                    value={element} 
                    name={props.name}
                    //onc checked and onChange work as one
                    //due if checked ? then it will run the onChange propperty
                    checked = {props.value === element}
                    onChange={props.onChange}
                    title={props.title}
                    />
                    {element}

                </label>
            </div>
           
 
        )
     }
    )
    return (
        <div id = {props.id}>
            {radiosOptions}
        </div>
    )
}

/**Class Name "Toggle" */
export function Toggle(props:ToggleProps):React.JSX.Element{
    return(
        <div className={props.className ||  'Toggle'} id={props.id}>
            <details >
                <summary>{props.head} </summary>
                {props.Content}
            </details>

        </div>
    )
}

/**Class Name "Details", "Summary", "Hidden" */
export function DivToggle(props:ToggleProps):React.JSX.Element{
    let [isHidden, setIsHidden ] = useState<boolean>(true);
    const hiddenHandler = (event:React.MouseEvent<HTMLDivElement>):void=>{
        setIsHidden(prev => prev = !prev ) ;
    }
    
    return (

        <div  className={props.className ||  'Details'}>
            <div onClick={hiddenHandler} className='Summary'>{props.head} </div>

            <div hidden={isHidden}  className='Hidden'>
                {props.Content}
            </div>
                
        </div>

    )
}
