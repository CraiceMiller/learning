import React, { type HtmlHTMLAttributes } from "react"; 
import type {Location } from "react-router-dom" ; 


//import type {InputHTMLAttributes} from "react"; 



//COMPONENTS PROPS ------------------------------------------>
/**
 * @description Type for buttons in tsx  files in order to write them correctlye
 */
export interface  ButtonProps extends React.ButtonHTMLAttributes<HTMLButtonElement>{
    text: string;
    command:(event:React.MouseEvent<HTMLButtonElement,MouseEvent>)=>void; 
    className?:string ; 
    withStyle?:boolean; 


} 

export type Component = React.JSX.Element ; 

export interface  InputProps extends React.InputHTMLAttributes<HTMLInputElement> {
    labelName:string, 
    labelDirection?:'left'|'right', 
    onChange?:(event:React.ChangeEvent<HTMLInputElement>)=>void, 
} 

export interface  FormProps extends React.InputHTMLAttributes<HTMLFormElement> {
    text:string,
    onSend:(value:string)=>void
} 


export type SearchBarProps  = {
    onSearch: (value:string) =>void , 
    placeholder?:string  , 
    inputStyle?: React.CSSProperties , 
    id?:string,
    barStyle?: React.CSSProperties, 
    image?:string ,
}

/**
 * @typedef {Object} listProps
 * @template Value
 * @property {Value[]} values - An array of values to be rendered as list items.
 * @property {boolean} [order=false] - If true, renders the list as an ordered list (<ol>); otherwise, renders an unordered list (<ul>).
 */
export interface listProps<Value > extends React.LiHTMLAttributes<HTMLLIElement> {
    values:Value[] , 
    order?:boolean, 
    valueClicked?:(event:React.MouseEvent<HTMLLIElement>)=>void,
}

/**
 * @typedef {Object} RouteData
 * @property {string} to - The URL path for the route (e.g., "/about").
 * @property {string} text - The text to display for the navigation link (e.g., "About Page").
 * @property {React.ElementType} Element - The React component to render when this route is active (e.g., Home).
 */
export type RouteData = {
    to:string, 
    text:React.ReactNode , 
    element:React.JSX.ElementType, 
    SubChild?:{
        to:string, 
        text:React.ReactNode, 
        element:React.JSX.ElementType, 
    }[]
} 
/**
 * @typedef {Object} NavBarProps
 * @property {RouteData[]} information - An array defining all navigation links and their corresponding route elements.
 * @property {string} [id] - Optional ID attribute for the navigation bar container.
 * @property {React.CSSProperties} [style] - Optional inline style object to apply to the <nav> element.
 */
export interface  NavBarProps extends Omit<React.HTMLAttributes<HTMLElement>,'className'> {
    information:RouteData[], 
    location?:Location|string; 
    className?:string, 
}


export interface ComboBoxProps<T = string> {
    options: T[],
    id?: string ,
    value: T,
    name?:string, 
    style?:React.CSSProperties, 
    onChange: ((event: React.ChangeEvent<HTMLSelectElement>) => void),
    className?:string, 
}


export interface RadioProps extends Omit<ComboBoxProps, "onChange">, Omit<React.InputHTMLAttributes<HTMLInputElement>,"value"> {
    onChange: ((event: React.ChangeEvent<HTMLInputElement>) => void),
    name:string,
}

export interface ToggleProps extends React.DetailsHTMLAttributes<HTMLDetailsElement> {
    head:string; 
    Content:React.ReactNode; 
}



export type BinaryObject={
    index:number, 
    array:any[],
    target:any,
    amount:number,
    ok: boolean,
    time:string
} ;


//Utils TYPES ------------------------------------------>
/**
 * @description I guess this is just a decorator
 * Generics allow us to create flexible and reusable code templates that can adapt to any data type while preserving type safety.

Unlike any, generics remember and enforce the type we provide, ensuring that TypeScript can detect errors and provide autocompletion.

They can be used in functions, types, interfaces, and classes, often with extends (to restrict) and = (to set defaults).
 */
export type Prettify<T> = {
    [K in keyof T]: T[K];
} &{};



export type Response = {
    ok:boolean , 
    message?:string , 
    method: 'POST'|'GET', 
    responseClass?: string, 
    encoded?:boolean , 
    status?:string, 
    body:string, 
    details?:{
        httpReason?:string, 
        httpCode: number, 
        code?:string
    }, 
    Headers?:{
        contentType:string
    }
}

export type PrimitiveValues = boolean | string| number |null | undefined  ; 



//PROJECTS TYPES ------------------------------------------>

export type User = {
    name: string;
    age: number;
} | {
    name: string,
    age: number,
    info:  {
        country: string
    } | {
        country: string,
        phone: number
    }
}

export type Student = {
    basic:{ 
        id:number,
        name:string, 
        lastName:string, 
        age:number, 
        gender:"male"|"female"
    }, 
    educational:{
        degree: "management bussines" | "chartered accountant" | "bachelor's degree in computer science", 
        year?: "first" | "second" | "third", 
        schoolCycle?:string 
    }

    details?:{
        country?:string, 
        phone:number,
        transportation?:"public"|"car" | "motocycle" | null, 
        languages?:string[], 
        hasJob?:boolean,
        dateBirth?: Date,
        parent?:{
            mother?:{
                name:string,
                address?:string, 
                email?:string,
                other?:{
                    extraInfo:string
                }

            }, 
            father?:{
                name:string,
                address?:string, 
                email?:string,
                other?:{
                    extraInfo:string
                }

            }, 
        }, 
        emergencyContact?:{
            name:string, 
            phone:number, 
            relationship:string, 
        }
    }
}




  
