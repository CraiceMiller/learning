import React from "react";
import { BrowserRouter, Routes, Route, Link } from "react-router-dom";
import type {BrowserRouterProps} from "react-router-dom";
import type {Location,RoutesProps,LinkProps } from "react-router-dom" ; 

import type { NavBarProps,RouteData} from  "@utils/typing"; 


interface L extends LinkProps , React.RefAttributes<HTMLAnchorElement>{
    children:React.ReactNode ; 
}
export const CreatLink = ({to,key,children, className,...rest}:L )=>(
    <Link 
    to={to}
    key={to.toString()}
    className={className}
    {...rest}
    >
        {children}
    </Link>

)

/**
 * Renders the navigational links using react-router-dom's <Link> component.
 *
 * @component
 * @param {NavBarProps} props - The props object containing routing information and styling.
 * @returns {React.JSX.Element} The rendered <nav> element with links.
 * within the className "Navigation-Bar"
 * @update 14/11/2025 at 9:00 hrs
 */
export const NavigationBar = ({information,className,id, ...rest }:NavBarProps)=>{
    const links:React.JSX.Element[] = information.map(value=>
        <li >
             <CreatLink
            className={`Navigation-Link ` }
            to={{pathname:value.to}}
            key={value.to} 
            >
                {value.text}
            </CreatLink> 
        </li>
    ) ; 

    return (
        <nav {...rest}  id={id} className={`Navigation-Bar ${className || ''}` } >
            <ul className={` Navigation-Bar ${className || ''} `} >
                 {links}
            </ul>
        </nav>
    )
}


export function CreateRoute({path,Element}:{path:string,Element:React.JSX.ElementType} ){
    return (
        <Route key={path} children path={path}  element={<Element />} /> 
    )
}

/**export const CreateRoute =  ({to,element} :RouteData )=>(
    <Route key={to} children path={to}  element={<element />} /> 
)
*/

/**
 * 
 * Renders the <Routes> structure for the application based on the provided route data.
 * This component maps the RouteData array into <Route> components.
 *
 * @update 25/11/2025
 * @component
 * @param {NavBarProps} props - The props object containing the route definitions.
 * @returns {React.JSX.Element} The rendered <Routes> wrapper with dynamic <Route> elements.
 * within the className "Navigation-Routes" in order to modifiete whenever you want
 */
export function NavigationRoutes({information,location,className,id, ...rest }:NavBarProps   ){
    //this function only provide us all the link that our website will have

    function CreateRoute (value: RouteData)
    {
        return (
            <Route key={value.to}  path={value.to}  element={<value.element/>}/>
        )
    } 

    //This array will storage all the Routes(with paht and the elemetn when re-render)
    const linked_routes:React.JSX.Element[]= information.map(value =>
    {
        //chercahry
        //web -> Routes
        //this subfucntion will help me to create all
       
        //if the parameter value has "subChild", the value becmoes the fathers
        let father = value ; 
        if (father.SubChild !== undefined)
        {
            const subArray:React.JSX.Element[] = father.SubChild.map(subValue=>
            {
                //const nestedPath:string = subValue.to.startsWith(father.to) ? subValue.to :`${father.to}${subValue.to} ` ; 
                return (
                <Route key={subValue.to}  path={subValue.to}  element={<subValue.element/>}/>)
            })
            
            return (
                <Route key={value.to}  path={value.to}  element={<value.element/>}>
                    {subArray}
                </Route>
            )
        }
        /**
         * attempt 25 11 2025
         <father>
            <child>
            <child>
                <subchild >
            <child>
         */

        return (
            <Route key={value.to}  path={value.to}  element={<value.element/>}/>

        )
    } 
    ) ; 

    return (
        <>
                <Routes   location={location || ''}  >
                    {linked_routes}
                </Routes>
        </>
    )
}




/**todo: here i need to create that navigationContiner can handler all the logic and wrap
 * the links at hands 
 */

export function NavigationContainer({ basename, children }: BrowserRouterProps):React.JSX.Element 
{
    return (
        <BrowserRouter basename={basename || '/'}>
            {children}
        </BrowserRouter>
    )

}



