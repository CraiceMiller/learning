import  {
    use,
    createContext, 
} from 'react';
import type {
    Usable,
    Context,
} from 'react';

import { ErrorBoundary} from "@hooks/react-utils"; 

const TEXT = ()=>{
    return (
        <div className="block" >
            
            <h1 className="text-8xl" >Learning New Things </h1>
            <p><small>Thursday 4-12-2025  </small> </p>

            <dl>
                <dt></dt>
                <dd></dd>
            </dl>
        </div>
    )
}

//--------------------------------------------------------------------------------------------
function UseHookText ()
{
    return (
        <dl>
            <dt>The React hook <big>use</big>  </dt>
            <dd>this hook allows us to</dd>
        </dl>
    )
}

const url:string = "https://pokeapi.co/api/v2/pokemon/ditto"; 
function UseHook()
{
    //const data = use( fetch(url).then(r=>r.json()) )
    
    return (
        <section className="grid"  >
            <ErrorBoundary fallback={<div>Something goes wrong :(</div>} >
                <UseHookText/>
                
            </ErrorBoundary>
        </section>
    )
}


//--------------------------------------------------------------------------------------------




//--------------------------------------------------------------------------------------------



/**
 * @Ojective Learn 
 React:
    - hook use 
        -suspense componenet
TypeScriopt: 
    
    -typeGuards
    -infer
    -type
 */
function App()
{
    return (
        <main className="grid sm:grid-cols-[1fr,1fr] grid-cols-1   " >
          
            <div className="block sm:col-span-2 " >
                <h1 className="text-8xl" >Learning New Things </h1>
                <p><small>Thursday 4-12-2025  </small> </p>
            </div>

            <UseHook/> 
            <UseHook/> 
            
        </main>
    )
}
export default App ; 
