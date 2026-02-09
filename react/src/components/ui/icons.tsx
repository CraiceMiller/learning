import type {Component} from "@utils/typing" ; 
import { FaSun,FaMoon} from "react-icons/fa" ; 
import React from "react" ; 
import {useDarkMode} from "@hooks/themes"


/**
 * A presentation component that displays either a Sun or Moon icon based on 
 * the current dark mode status and allows the user to toggle the theme when clicked.
 * @since 17/11/2025, Monday at 16:00 hrs
 * * @returns {React.JSX.Element} A span element containing the appropriate theme icon.
 */
export function ThemeIcon():Component
{
    /**This only change true or false, nothing more, and display the span elemtn with an icon */
    const [darkTheme,setDarkTheme ] = useDarkMode() ; 
    const handleMode = React.useCallback(()=>setDarkTheme(!darkTheme),[darkTheme]) ; 
    return (
        <span onClick={handleMode} >
            {darkTheme ?
            (<FaSun size={35} className='darkmode-icon' />): 
            (<FaMoon size={35} className='darkmode-icon' />) 
            }
        </span>
    )
}