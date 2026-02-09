import React from "react" ; 

/**
 * A custom React hook that synchronizes a state variable with the browser's 
 * Local Storage, ensuring data persistence across page refreshes and sessions.
 * @since 17/11/2025
 * * @template T The type of the value being stored (e.g., boolean, string, object).
 * @param {string} key - The unique key used to store and retrieve the data in Local Storage (e.g., 'dark-theme').
 * @param {T} [initialValue] - The default value to use if no data is found in Local Storage.
 * @returns {[T, React.Dispatch<React.SetStateAction<T>>]} A tuple containing the current stored value and a setter function (like standard useState).
 */
export function useLocalStorage<T> (key:string,initialValue?:T):[T,(value:React.SetStateAction<T>)=>boolean]
{
    /**for me the purpose of this hook is to storage whatever value in a window.Storage obecjt, 
     as a default the Storage object is empty...
     */

     //Here we are initializing the useState with the user value provided, could be a string,number,so on.
    const [storedValue,seStoredValue] = React.useState<T>(()=>
    {
        try 
        {
            const item:string | null = window.localStorage.getItem(key) ;
            return item ? JSON.parse(item) : initialValue ; 
        }
        catch(e)
        {
            console.error(e) ; 
            return initialValue ; 
        }
    }) ; 

    //This is our ecapsule function, that will remember all the values before, and it will
    //updated by the user
    //the purpose here is only to push,add,append, the storedValue into the Storage object from the window
    //here we update the useState and storage the value into the Storage object
    function setValue (value:React.SetStateAction<T>):boolean
    {// value:T | ((value:any)=>T)  || React.SetStateAction<T>
        //those one are the same
        try
        {
            const valueToStore:T = value instanceof Function ? value(storedValue) : value ; 
            seStoredValue( valueToStore ) ; 
            const jsonValue:string = JSON.stringify(valueToStore,undefined,4) ; 
            window.localStorage.setItem(key,jsonValue) ;
            return true;  
        }
        catch(e)
        {
            console.error(e) ; 
            return false ; 
        }
    }
    /**What i could seee was the Storage object only accpet a key,value string nothing more
     that why we use JSON.parse to convert the string to the specif object
     */
    return [storedValue,setValue]
}

type ClassListProp = 'add' | 'remove' ; 
/**
 * @description This hook wil only add, or remove a value from the
 * window.document.body.classList object ...
 * @since 19/11/2025
 * @returns 
 */
export function useBodyClassList(): (action: ClassListProp, ...tokens: string[]) => void
{
    const bodyClass: DOMTokenList = window.document.body.classList ; 


    function classListHandler(action:ClassListProp,...tokens: string[])
    {
        try 
        {
            switch (action)
            {
                case 'add': 
                bodyClass.add(...tokens); 
                return ; 
    
                case 'remove': 
                 bodyClass.remove(...tokens) ; 
                 return ; 
    
    
                default : 
                return ; 
            }

        }
        catch (e)
        {
            console.error(e) ; 
        }
       
    }

    //const [value,setValue] = React.useReducer(setReducer,) ; 

    return classListHandler  ; 
} 
