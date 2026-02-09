import React from "react" ; 
import {NavigationBar } from "@layouts/navBar" ; 
import {PAGES_CONTEXT } from "@pages/website2" ; 
import Button from "@components/buttons";
import {List}  from "@components/choices" ; 
import LOGO from "@assets/logo.png" ; 
import type {Component} from "@utils/typing" ; 
import { ThemeIcon} from "@components/ui/icons" ; //17/11/2025 monday
import {SideBarButton} from "@layouts/sideBar" ; // 25 11 2025 Tuesday 
import {Sources} from "@pages/website2" ; //26/11/2025
import  type { Topic } from "@pages/website2" ; 
import {Toggle} from "@components/choices" ; 


export function Header({className,toggleSidebar}:{className:string,toggleSidebar:React.RefObject<HTMLElement | null>} ):Component
{
    window.document.body.className = "dark:bg-gray-900" ; 

    const INFO = React.useContext(PAGES_CONTEXT ) ; 
    return (
        <header className={className} >
            <div className='row'>
                <SideBarButton sideBarRef={toggleSidebar} />

                <img src={LOGO}/>
                
                <div >
                    <h1> Webisite 2</h1>
                    <hr/>
                    <p><small>14/11/2025</small> </p>
                </div>
                
                <NavigationBar information={INFO} />
                
                <ThemeIcon />
                {/**<Button className="btn " command={()=>{}} text="Sing-in" />*/}
            </div>
        </header>
    )
}



type SubDivProps ={
    title:string ; 
    values:React.ReactNode[]; 

}
/**start 14/11/2025, update footer 26/11/2025 at 17:10hrs */

export function Footer ({className}:{className:string}) : Component
{
    /**This one only create a section with a tile in a list  */
    function SubDiv ({title,values}:SubDivProps ):Component
    {
        return (
            <section className="Footer-div" >
                <h4>{title}</h4>
                <List values={values} />
            </section>
        )
    }
    const Lnk = ({text,href}:{text:string,href:string})=> 
    <a href={href} target="_blank" ><p><b> {text}</b> </p></a> ; 


    let ALL_LINKS:React.JSX.Element[] = []; 

    const Source_Map =  new Map(Object.entries(Sources ) ) ; 


    for (const key of Object.keys(Sources))
    {
        let subDivArray :React.JSX.Element[] = []; 
        const Current_Topics:Topic | undefined  = Source_Map.get(key) ; 
        if (Current_Topics === undefined ) continue ; 
        const Topics_Map = new Map(Object.entries(Current_Topics ) ) ; 
        
        //getting the kesy
        for ( const topicKey of Object.keys(Current_Topics )) 
        {
            const urls:React.JSX.Element[] | undefined =Topics_Map.get( topicKey )?.map(v=>
                <Lnk text={ v.author } href={v.url} />
                ) ; 

            if(urls === undefined)continue ; 
            //The fnal step is to storage it into the array
            subDivArray.push(
            <SubDiv title={topicKey} values={urls} />
             )

        }

        ALL_LINKS.push(
            <Toggle Content={subDivArray} head={key} />
        )
    }
    /**
     Category: 
        Topic: 
            Details: 
                url
                date



    result : 
    Topic 
    - url 
    - url 
    - url 
    - url 

     * 
     */




    return (
        <footer className={className} >
            <div className="row">
                {ALL_LINKS}
            </div>
        </footer>
    )
}