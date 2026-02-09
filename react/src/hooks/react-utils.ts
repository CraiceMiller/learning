import React from 'react' ; 
import * as Query from '@tanstack/react-query' ;
export interface ErrorBoundaryProps {
    fallback: React.ReactNode; // The element to render when an error occurs
    children: React.ReactNode; // The content the ErrorBoundary wraps
}
/**@description This function will only print how many time a certain component
 * is re-render
 * @since 04/11/2025 
 * @returns the current Number of render in a certain component
 */
export function TrackRender(currentComponent:Function,debug:boolean = false):number{
    //This will remember the number
    const trackRenders:React.RefObject<number> = React.useRef<number>(0); 
    //This will run every time a component renders
    React.useEffect(()=>{
        trackRenders.current++; 
        console.log(`The component << ${currentComponent.name} >> was re-render !!! for ${trackRenders.current} Times`);
    }); 
    

    if (debug){
        React.useDebugValue(trackRenders) ; 
    }

    //and return the current render
    return trackRenders.current ; 
}
/**
 7/11/*2025
a  hook is just normal ts/hook

#We can use the React.useDebugValue() to help us in our 
custome hooks 

 */

export function useFetchDucks( ){
    const DUCK_URL:string ='/api/api/random'; 
    const [duck,setDuck] = React.useState<string>('') ; 
    async function getDuck(){
        const {url} = await fetch(DUCK_URL).then(
            response=>{
                return response.json()}
        )
        //console.log(url);
        setDuck(url) ; 
    }
    React.useEffect(()=>{
        getDuck() ; 
    },[]) ; 

    return {duck} ; 
}  

/**
 * @since 9/11/2025 
 * */
export class ErrorBoundary extends React.Component<ErrorBoundaryProps, { hasError: boolean }> {
    public state = {hasError:false} 
 

    static getDerivedStateFromError(){
        return {hasError:true} ; 
    }

    componentDidCatch(error:any,info:any){
        console.log(error,info);
        
    }

    render(){
        if (this.state.hasError){
            return this.props.fallback ; 
        }
        return this.props.children ; 
    }


}

/**
 ## Reference Code Lens 

 to activate the codeLens in vscode we need to go to the configuration 
 file -> Preference -> Setting 
 then search 
 "reference code lens" and active the option 
 "TypeScriopt > reference Code Lens"
 now search 
 "editor.codeLens" 
 and active 
 "Editor Code Lens"

 and this is it ..
 */

/**
 * @description this will only fecth the data in a server using the useQuery methos from the librarry Query
 * @param key the key to track the elemten in debuggin. and useMutation
 * @param url the url to fecth the data at hand
 * @since 11/11/2025 at 11: 11 hrs 
 * @returns Query.UseQueryResult with all the information 
 * @NOTE remember that this must be inside a <Query.QueryClientProvider client={queryClient}  > to work property
 * @MethodsNeeded 
   - Query.QueryClientProvider
   - Query.QueryClient 

*@example
    >>> const queryClient = new Query.QueryClient() ; 
//Ducks
function ShowDuckList():React.JSX.Element
{
    const {data,status, isLoading,isError}  = useGetData(['Ducks'], '/api/api/random') ; 
    console.log("Current Duck data ", data);
    if (isLoading)
    {
        return <p>Loading...</p>
    }
    if (isError)
    {
        return <p>Error!!!</p>
    }
    
    
    return (
        <div className='Box'>
            <img src={data.url} />
        </div>
    )

}

//Main app
export default function App(){
    return (
        <div> 
            <Query.QueryClientProvider client={queryClient}  >
                 <ShowDuckList /> 
            </Query.QueryClientProvider>
        </div>

       
    )
}
*/
export function useGetData(key:Query.QueryKey,url:string)
{
    const DATA= Query.useQuery({
        queryKey:key, 
        queryFn:async ()=>{
            const res = await fetch(url); 
            return res.json() ; 
        }
    }) ; 

    return DATA  ; 
}

//
export function useDraggable<K extends keyof HTMLElementTagNameMap>(selectors: K): void ;
export function useDraggable<K extends keyof SVGElementTagNameMap>(selectors: K): void ; 
export function useDraggable<K extends keyof MathMLElementTagNameMap>(selectors: K):void; 
export function useDraggable<K extends keyof HTMLElementDeprecatedTagNameMap>(selectors: K):void; 
export function useDraggable<E extends Element = Element>(selectors: string):void; 

/**
 * @description just an attempt on crate a drag hook like vedal and evil did in their video
 * @since 11/11/2025 at 17:00hrs
 * @param selectors 
 * @creditsTo YOUTUBE: vedal,Code with Ania Kubow, 
 * @returns 
 */
export function useDraggable<K extends keyof HTMLElementTagNameMap>(selectors: K): void
{
   React.useEffect(()=>{
    const ALL_VALUES:NodeListOf<HTMLElementTagNameMap[K]> = document.querySelectorAll(selectors) ; 

    if (ALL_VALUES.length <= 0)return ; 
    
    
    function Drag_Logic(value: HTMLElementTagNameMap[K] ):VoidFunction
    {
        let isDragging:boolean = false ; 
        let startX:number, startY:number; 

        function onDragStart():void
        { 
            isDragging = true; 
            console.log('The drag has start');
            startX = value.clientLeft ; 
            startY = value.clientTop ; 
            
            //adding listeting during the drag 
           //value.addEventListener('dragmove',OnDragMove) ; 
            value.addEventListener('dragend',onDragEnd) ; 
        
        }

        function OnDragMove(event:DragEvent ):void
        {
            if(!isDragging)return ; 
            console.log('The drag is moving right now ');
            let dx:number = event.clientX -   startX  ; 
            let dy:number = event.clientY - startY ; 
            value.style.left = `${dx}px`
            value.style.top = `${dy}px`
        }

        function onDragEnd():void
        {
            if(!isDragging)return ; 

            isDragging = false; 
            console.log('The drag has ends ...');

            //Cleanning all the event listener
            value.removeEventListener('dragend',onDragEnd)

        }

       

        value.addEventListener('dragstart',onDragStart) ; 

        return ()=>
        {
            value.removeEventListener('dragstart',onDragStart) ; 
        }
    }






    const ToRemove = Array.from(ALL_VALUES).map(Drag_Logic) ; 

    return ()=>{
        ToRemove.map(value=>{value()})
    }



   },[]); 
    
}

//
export function useDraggableEnter<K extends keyof HTMLElementTagNameMap>(selectors: K): void ;
export function useDraggableEnter<K extends keyof SVGElementTagNameMap>(selectors: K): void ; 
export function useDraggableEnter<K extends keyof MathMLElementTagNameMap>(selectors: K):void; 
export function useDraggableEnter<K extends keyof HTMLElementDeprecatedTagNameMap>(selectors: K):void; 
export function useDraggableEnter<E extends Element = Element>(selectors: string):void; 
/**
 * 
 * @param selectors 
 * @since 12/11/2025 at 17:30hrs
 */
export function useDraggableEnter<K extends keyof HTMLElementTagNameMap>(selectors: K): void
{
   React.useEffect(()=>{
    const ALL_VALUES:NodeListOf<HTMLElementTagNameMap[K]> = document.querySelectorAll(selectors) ; 

    if (ALL_VALUES.length <= 0)return ; 
    

    function Drag_Logic(value: HTMLElementTagNameMap[K] ):VoidFunction
    {
        

        function onDragEnter():void
        { 
           
            console.log('an elemtn enter ');
            
           
            //adding listeting during the drag 
           value.addEventListener('dragover',onDragOver) ; 
            value.addEventListener('dragend',onDragLeave) ; 
            value.addEventListener('drop',onDrop) ; 
            
        
        }

        function onDragOver():void
        {
            console.log('an elenemt is on my space >:(  ');

        }

        function onDragLeave():void
        {
            
            console.log('The elemetn leave my space :)  ...');

            //Cleanning all the event listener
            value.removeEventListener('dragover',onDragOver) ; 
            value.removeEventListener('dragend',onDragLeave) ; 
            value.removeEventListener('drop',onDrop) ; 

        }

        function onDrop():void
        {
            console.log('You drop an element here ----->  ');
            
            
        }

        value.addEventListener('dragenter',onDragEnter) ; 

        return ()=>
        {
            value.removeEventListener('dragenter',onDragEnter) ; 
        }
    }






    const ToRemove = Array.from(ALL_VALUES).map(Drag_Logic) ; 

    return ()=>{
        ToRemove.map(value=>{value()})
    }



   },[]); 
    
}
//11/11/2025 attempt from vedal 
function useDraggableAttempt1<K extends keyof HTMLElementTagNameMap>(selectors: K): void
{
    React.useEffect(()=>
    {
        //First i need to get the array of all 
        const Elements:NodeListOf<HTMLElementTagNameMap[K]> = document.querySelectorAll<K>(selectors); 
        //verifying if the array is have elemtns 
        if (Elements === null || Elements.length <= 0 || !Elements)return ; 
        //Creating the logic of how to drag an element 
        const Drag_Logic = (subElement:HTMLElementTagNameMap[K])=>
            {
                let isDragging = false; 
                let startX:number, startY:number, startLeft:number, startTop:number, velocityX:number, velocityY:number, lastTime:number, lastX:number, lastY:number;
                let prevPosition: string ; 
                function onMouseDown ():void
                {
                    //debugger ;
                    isDragging = true ; 
                    prevPosition = subElement.style.position ; 
                    subElement.style.position = 'absolute' ; 
                    //we are calculating the initials values; 
                    startTop = subElement.offsetTop ; 
                    startLeft = subElement.offsetLeft ; 
                    //add events when the mouse is moving 
                    document.addEventListener('pointermove',onMouseMove) ; 
                    document.addEventListener('pointerup', onMouseUp) ;    
                }

                function onMouseMove(event:MouseEvent):void
                {
                    if (!isDragging)return ; 
                    subElement.style.left = `${event.clientX - startLeft}px` ; 
                    subElement.style.top = `${event.clientY - startTop}px`  ; 
                    //console.log(startLeft,startTop);
                    
                }
                function onMouseUp(event:MouseEvent)
                {
                    if (!isDragging)return ; 
                    isDragging = false ; 
                    subElement.style.position = prevPosition ; 
                    //removing all the listener events 
                    document.removeEventListener('pointermove', onMouseMove) ; 
                    document.removeEventListener('pointerup', onMouseUp) ; 
                }

                subElement.addEventListener('pointerdown',onMouseDown) ; 
                return ()=>{subElement.removeEventListener('pointerdown',onMouseDown); }

        }
        //converting into an array and mapping all the elements into the lagic
        const Functions_To_Remove_Later = Array.from(Elements).map(Drag_Logic) ; 

        return ()=>{
                Functions_To_Remove_Later.forEach(fn=>fn()) ; 
            }
    },[])
}
