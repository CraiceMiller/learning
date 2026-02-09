import React from "react" ; 
import { useLocalStorage,  useBodyClassList} from "./storages" ; 

/**
 * Manages the application's dark mode state using local storage for persistence 
 * and controls the application of the 'dark' CSS class to the document body.
 * * This hook relies on the 'class' strategy for Tailwind CSS dark mode.
 * @since 17/11/2025
 * * @returns {[boolean, (value: React.SetStateAction<boolean>) => void]} A tuple containing:
 * [0] The current dark mode status (boolean).
 * [1] A function to toggle the dark mode status.
 */
export function useDarkMode():[boolean,(value: React.SetStateAction<boolean>) => boolean]
{
    /**Here I use the useLocalStorage hook i previous coded, with a boolean as a value */
    const [enabled,setEanabled] = useLocalStorage<boolean>('dark-theme') ; 
   // const [enabled,setEanabled] = React.useState<boolean>(false) ; 
    const isEnabled:boolean =enabled === undefined ?false : enabled ; 

    React.useEffect(()=>
    {
        const className:string = 'dark'; 
        const body = useBodyClassList() ; 
        isEnabled ? body('add', className):body('remove', className) ; 

        /** 
        const bodyClass: DOMTokenList = window.document.body.classList ; 
        try 
        {
            isEnabled ? bodyClass.add(className) : bodyClass.remove(className) ;
        }
        catch(error )
        {
           console.error(error) ; 
        }*/
    },[enabled,isEnabled] ) ; 
    return [enabled,setEanabled]

}
