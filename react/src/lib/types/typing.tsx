
//Swapy libray props 13/11/2025 
import * as Swapy from "swapy" ; 
import React from "react" ; 
export interface  SlotProps extends React.AllHTMLAttributes<HTMLDivElement>  {

    slotName:string; 
    itemIside?:boolean ; 
    itemProps?:ItemProps ; 
    children?:React.ReactNode; 
     
}

export interface  ItemProps extends React.AllHTMLAttributes<HTMLDivElement> {
    itemName:string;
    children?:React.ReactNode ; 
}
export interface useSwapyProps {
    config?: Partial<Swapy.Config>
    onSwapy?: Swapy.SwapEventHandler ;
    onSwapyStart?: Swapy.SwapStartEventHandler ; 
    onSwapBefore?:  Swapy.BeforeSwapHandler; 
    onSwapEnd?: Swapy.SwapEndEventHandler ; 
}

export interface SwapyContainerProps extends useSwapyProps,React.AllHTMLAttributes<HTMLDivElement> {
    children: React.ReactNode;
    className?: string;
}
