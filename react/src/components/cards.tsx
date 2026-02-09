import * as React from 'react';
import type {Component} from "@utils/typing" ; 


export interface CardProps extends React.AllHTMLAttributes<HTMLDivElement>
{
    Title:string ; 
    Imgsrc:string ; 
    children?:React.ReactNode ; 
}

export function Card (props:CardProps):Component 
{
    return (
        <section className={`Card ${props.className || '' }`} >
            <img style={{height:"50%",width:"100%",overflow:"hidden"}}  className={`Card-Image`} src={props.Imgsrc}  /> 
            <span><h3> {props.Title} </h3> </span> 
            {props.children}
        </section>
    )
}