import React from "react"  ;
import {useCountDown} from "@hooks/clock"
export interface CountDownProps{
    onChange?:(currentSecond:number)=>void; 
    seconds:number; 
    onFinish?:()=>void; 
    className?:string; 
    id?:string; 


}

/**
 * @since 20/11/2025
 * @param param
 * @returns 
 */
export function CountDown({seconds,onFinish,onChange,className,id}: CountDownProps )
{
    const [time, clock] = useCountDown(seconds) ;
    React.useEffect(()=>{
        if (!onFinish && !onChange)return ; 
        onChange && onChange(clock.NUMBER ) ; 

        if(!clock.isCounting && onFinish !== undefined){
            onFinish() ; 
        }
  
    },[clock.NUMBER])

    
    return (
        <div className={`count-down ${className || ''} `} id={id}  >
            {time} 
        </div>
    )
}