//React components
import {toast, ToastContainer} from "react-toastify"; 
import React, {useState,useEffect,useContext} from "react"; 
//My componnet 
//If I use an alias path and I wanna get a JSX.Element I explicity have to write .tsx at the end ; 
import {Form,Input,List,Toggle} from "@components/choices"; 
import Button from "../../components/buttons";
//Normal utils
import {range,all, checkFalsyPrimitiveValues } from "@utils/utils" ;
import {Stack,LinkedList} from "@utils/algorithms";
import type {Queue} from "@utils/algorithms"; 
//To specific files i need to explicity tell what kind of file is (ts, tsx)
import {TrackRender,useFetchDucks } from "@hooks/react-utils"; 
//----------------------------------------------------------------------------------------------------------------------------------->
/**
 * mutable: In programming, mutable refers to an object or data structure whose state or value can be changed after it has been created. This means you can modify its internal data, add or remove elements, or alter its properties without creating an entirely new object in memory.
Conversely, an immutable object cannot be changed after creation; any "modification" to an immutable object actually results in the creation of a new object with the desired changes, leaving the original object untouched.
 Todo 8/11/2025 : 
    useEffect: 
        what is destructor

    useContext: 
        what is the Consumer property


    useRef: 
        when i need to grab an elemetn from the DOM,this is the best

    useReducers: 
        it work similarty to useState 


 */


/**
 * 
 */

//import { } from  '../../../Learning_Python/python/mypython/__pycache__/' ; 
/**
 * 
react
├───myjs
|     |___utils.ts
├───node_modules
├───public
└───src
    ├───assets
    ├───components
    └───styles
    |  └───myMess
    |____main.tsx
    |_____app2.tsx
|
|____tsconfing.json
|____vite.config.ts
|_____index.html


 */



/**
 my boxes: 
 .Box
 .Sub-Box
 .contenet 
 .Mini-Box

 HTML separators: 
 div
 section 
 header
 footer
 nav 

 news: 
 aside
 article

 

 */
//Contexts
//----------------------------------------------------------------------------------------------------------------------------------->
const ReviewContext:React.Context<string> = React.createContext('null'); 
const THINGS_TO_DO:React.Context<string[]> = React.createContext(['']) ; 



//Components
//----------------------------------------------------------------------------------------------------------------------------------->
/**This box only update the ReiviwContent const by my Form component */
function Review({updater}:{updater: React.Dispatch<React.SetStateAction<string>>}):React.JSX.Element{
    const sendValue = (v:string)=>{
        if(!checkFalsyPrimitiveValues(v))return ; 
        updater(()=>  v )
        
    }
    const value:string = useContext(ReviewContext) ; 
    return(
        <div className="Box">
            <h3>Review</h3>
            <p>03/11/2025</p>
            <p>use State</p>
            <Form text="Send your request" onSend={sendValue} />
            <p>Sending your request: '{value}'</p>
        </div>
    )
}
/**This row only do a differente code when the ReviewContext is change */
function Review2():React.JSX.Element{
    const context:string = useContext(ReviewContext) ; 
    const stack:Stack = new Stack(); 
    useEffect(()=>{
        let width:number = window.innerWidth ; 
        const handler = ()=>{document.title = `Widht ${width}` };
        addEventListener('size',handler)
        return ()=>{
            removeEventListener('size',handler)
        };

    },[])

    useEffect(()=>{
        console.log("I am the function that will only display when the context change :)") ; 
        
        if (checkFalsyPrimitiveValues(context)){
            toast.success(`The Context change to ${context}` ) ; 
            stack.push(context) ; 
        } 
        
    },[context])


    return(
        <div  className="Box">
            <h3>Review</h3>
            <p>03/11/2025</p>
            <p>Use Effect</p>
            <p>The context change to {context} </p>
        </div>
    )
}
/**This only display the result from the Review1 */
function Review3():React.JSX.Element{
    const result:string = useContext(ReviewContext); 
    return(
        <div className="Box">
            <h3>Review</h3>
            <p>03/11/2025</p>
            <p>Use Context</p>
            <p>Reciving the result: {result} </p>
            
        </div>
    )
}


//To-Do
function DisplayList(){
    const thingsToDo:string[] = useContext(THINGS_TO_DO) ; 
    const handlerCheck = (event:React.MouseEvent<HTMLInputElement>)=>{
        const {checked} = event.currentTarget ;

    }; 
    const THINGS = thingsToDo.map(value=>{
        return <Input onClick={handlerCheck} labelDirection="right" type="checkbox" value={value} name={value} labelName={value} />
    }); 

    
    return (
        <div className="Box">
            <h3>To Do</h3>
            <List order values={THINGS} />
        </div>
    )

}

function AddTask({setList}:{setList:React.Dispatch<React.SetStateAction<string[]>>}){
    const onSend = (value:string)=>{
        if(!value) return ; 
        if(!checkFalsyPrimitiveValues(value))return ; 
        setList(prev =>[...prev,value]) ; 
    }; 
    return (
        <div >
            <Form className="Box" text="Add task" onSend={onSend} />
        </div>
    )
}

function ToDoList():React.JSX.Element{
    let myList:string[] = ["Read Manga","Learn React","Wathc anime","Sleep"] ; 
    const [thingsToDo, setThingToDo] = useState<string[]>(myList) ; 
    
    return (
        <div className="Sub-Box">
            <THINGS_TO_DO.Provider value={thingsToDo} >
                <DisplayList />
                <AddTask setList={setThingToDo} />
            </THINGS_TO_DO.Provider>
        </div>
    )
}

//Duck
function DucksImages(){
    const DogUrl:string ='/api/api/random'/**'https://cors-anywhere.herokuapp.com/https://random-d.uk/api/random' *//**'https://random-d.uk/api/random'; */
    //let DucksLinks:string[]=[] ; 

    const [Duck,setDuck] = useState<React.JSX.Element[]>([<></>]) ; 

    //This will only run when amounts, only once
    useEffect(()=>{
        console.log("Waiting the ducks")
        let PromiseDucks:Promise<string>[]= [] ; 
        //Loop 5 times to get 5 ducks
        for (var i = 0 ; i <= 5; i++){
            //Storage the Promise value in a variable
            let getDuckPromise:Promise<string> = fetch(DogUrl,{method:'GET'}).then(value=>{
                if (!value.ok)throw new Error("The content was not reach :("); 
                return value.json(); 
            }
            ).then(data=>{
                return data.url as string ; 
            })

            //When the getDuckPromise finish the get the value
            //We push it the new valu in an Promise<string>[] ; 
            PromiseDucks.push(getDuckPromise ) ; 
        }
        //Then with the Promise.all we can manipulate the array of promise whatever we want ...
        Promise.all(PromiseDucks).then((urls:string[])=>{
            const newDucks = urls.map(value=>
                <div>
                     <img src={value} className="Ducks" draggable />
                </div>
            )
            //And lastly we update all the React.JSX.Element[] in the useState hook ; 
            setDuck(newDucks) ; 
            console.log("The ducks was succesufully added :) ")
        })
        console.log("waiting... :o");
    },[])
    //This whill only run when the Ducks update in the lisk
    //My attempt of drag ducks like Neurosma did. start 3/11/25 at 21:00  
    /**useEffect(()=>{
        const MyDucks:NodeListOf<HTMLImageElement> = document.querySelectorAll<HTMLImageElement>('.Ducks') ; 
        //For every duck image i will do the following 
        MyDucks.forEach((duck:HTMLImageElement)=>{
            let isDragging:boolean = false; 
            
            let startX:number,startY:number,startTop:number,startLeft:number,velocityX:number,velocityY:number,lastTime,lastX,lastY; 
            function handler(this: HTMLImageElement, event: MouseEvent){
                isDragging = true ; 
                startX = event.clientX ; 
                startY = event.clientY ; 
                //startTop =  

                duck.draggable = isDragging ; 

            }

            duck.addEventListener('mousedown',handler); 
            return function ():void{
                    duck.removeEventListener('mousedown',handler); 
            }
        }) ; 

    },[Duck])*/

    return(
        <article className="Box Duck-Conteiner" >
            <h3>Ducks </h3>
            <p>3/11/2025</p>
            <List order values={Duck} />
        </article>
    )
}

//useRef 4/11/2025
function USEREF():React.JSX.Element{
    const myStackRef: React.RefObject<Stack<string>> = React.useRef<Stack<string>>(new Stack()) ; 

    TrackRender(USEREF) ;    
    const addData = React.useCallback((value:string )=>{
        myStackRef.current.push(value) ; 
    },[]) 
    const removeData = React.useCallback(()=>{
        if (myStackRef.current.empty()){
            console.log("The stak is currently empty ");
            return ;   
        } 

        let element:string = myStackRef.current.pop() ; 
        console.log(`The ${element} has been remove from the stack !!`)

    },[])
    
    return (
        <div  className='Box'>
            <h3 >Use Ref Hook</h3>
            <p>04/11/2025</p>
            <Form onSend={addData} text="storage data" />
            <Button text='remove first item' command={removeData} />
            <Button text='show stack' command={()=>{console.log(myStackRef.current.data);
            }} />
        </div>
    )
}

class Counter{
    private NUMBER:number = 0  ; 
    constructor(num?:number){
        this.NUMBER = num || 0 ; 
    }
    increase(){
        this.NUMBER++; 
        
    }
    decrease(){
        this.NUMBER -- ; 
    }
    get number():number{
        return this.NUMBER ; 
    }
}
//Diference on this 
function USEREF2():React.JSX.Element{ 
    const buttonRef:React.RefObject<HTMLButtonElement | null> = React.useRef<HTMLButtonElement>(null) ;
    const counter:React.RefObject<Counter>= React.useRef(new Counter()) ; 
    const counter2:React.RefObject<number> = React.useRef<number>(0) ; 
    const [num,setNum] = useState<number>(counter2.current); 
    function handlerButton(event:React.MouseEvent<HTMLButtonElement>) {
        console.log('The button was cliked twice :)');
        
        console.log(event) ; 
        if(buttonRef.current === null)return ; 
        buttonRef.current.style.backgroundColor = 'purple' ; 

    }
    useEffect(()=>{
        console.log('Re-render I am the USEREF 2 component ... ');
        console.log('The current reference of the button, ');
        console.log(buttonRef);
    })   ;
    return (
        <div  className='Box'>
            <h3  >Use Ref Hook</h3>
            <p>04/11/2025</p>
            <Button text="Click" command={()=>{counter.current.increase();console.log(counter.current.number) ;
            }} />
            <Button text="Click" command={()=>{setNum(prev=>prev+1); counter2.current++;console.log(counter2.current);
            }} />
            <p>{counter.current.number}</p>
            <p>{num}</p>
            <button
            ref={buttonRef}
            onDoubleClick={handlerButton}
            value='I am a button :)'
            title="Indedd a button" 
            >click my reference</button>

        </div>
    )
}


function USECALLBACK():React.JSX.Element{
    const [Name,setName] = useState<string>('') ;
    TrackRender(USECALLBACK ) ; 

    useEffect (()=>{
        console.log("Hello world!!!");
        console.log(`Hello ${Name}`);
    },[Name])

    const rememberFunc= React.useCallback((value:string)=>{
        setName(value) ; 
        let l:number[] = [] ; 
        for ( var a  of range(-2,10)){
            console.log(a) ; 
            l.push(a) ; 
        }
        console.log(all(l)) ; 
    },[])
 


    return (
        <div className='Box'>
            <h3>use Callback Hook </h3>
            <Form onSend={rememberFunc } text="Send your name "/>
            <Toggle head="content" Content={<p>Hello </p>} />
        </div>
    )
}
/**
 useRef hook rember a value throughtout several re-renders(it survives)
therefore we use the useRef to work as a simple ts/js code. 
example: 
myfile.ts
let Name:string = 'hersy'; 
let age:number = 19 ; 
function printValues<T = string,V = number>(first:T,seconds:V){
    console.log(first)
    console.log(second)
}
printValues(Name,age ) ; 
age = 21 ; 
Name = 'craice' ; 
printValues(Name,age ) ; 



myreactfile.tsx
function MyRef(){
    const Name = React.useRef<string>('hersy' ); 
    const age = React.useRef<number>(19) ; 
    function printValues<T = string,V = number>(first:T,seconds:V){
        console.log(first)
        console.log(second)
    }
    funtion click(){
        Name.current = 'hersy'; 
        age.current = 21 ; 
        printValues(Name.current,age.current ) ; 
    }
    useEffect(()=>{
        printValues(Name.current,age.current ) ; 
    },[])

    return (
        <div>
            <button onClick={click}>click  me </button>
        </div>
    )

}

for me the example above are the same logic but with 
different syntax

 */

//Hooks 
//Dispatch:  ; 
/**
1. useState = 
2. useEffect = 
3. useContext = 
4. useRef = 
5. useReducer = 
6. useCallback = 
7. useMemo = 
8. useImperativeHandle =
9. useLayoutEffect = 
10. useDebugValue = 
 
 */
const MESSAGE = React.createContext('null') ; 

function HOOKS():React.JSX.Element {
    //10. useDebugValue 
    TrackRender(HOOKS,true) ; 
    //1. useState
    const [value,setValue] = React.useState<string>('none') ; 
    //2. useEffect

    //4. useRef
    const buttonRef = React.useRef(null); 
    

    //dunno :( 
        //5. useReducer
    //const [state,dispatch] = React.useReducer<string>((prev:string)=>{

    //} ) ; 
    //6. useMemo
    //const myMemo = React.useMemo()

    //7. useCallback
    const myCall = React.useCallback(()=>{
        const btn:HTMLButtonElement|null = buttonRef.current  ;
        console.log(btn);  

    },[])

    //9.useLayoutEffect
    React.useLayoutEffect(()=>{

    })


    return (
        <div className='Box'>
            <Form text="send value " onSend={(v)=>{setValue(v)}} />
            <button
            value={value}
            id="My-Button-Ref"
            title="A simple ref Button"
            role="button"
            ref={buttonRef}
            onClick={myCall}
             />

             <MESSAGE.Provider value={value} >
                <PrintMessage />
             </MESSAGE.Provider>

        </div>
    )
}
function PrintMessage(){
    //3. UseContext
    const message = React.useContext(MESSAGE) ; 
    return     <p>Current value: {message}</p> ; 
}

function LittleDuck(): React.JSX.Element{
    TrackRender(LittleDuck) ;  
    let ducksList:string[] = [] ; 
    for (let i:number = 0 ; i <3 ; i++){
            const {duck} = useFetchDucks() ; 
            ducksList.push(duck) ; 
    }

    const allDucks:React.JSX.Element[] = ducksList.map(value=>{
        return (
            <img src={value} className="Ducks" />
        )
    })
    React.useEffect(()=>{
        console.log('The little Duck function has re-render');
        
    })

    return (
        <div className='Box'>
            <h4>Ducks here :3</h4>
            <List values={allDucks} />
        </div>
    )




}

//Rows
//----------------------------------------------------------------------------------------------------------------------------------->
/**This Row only use the UseState to share the current value
 where in one box is updater, 
 in another one is display it
 and another one do code
 whenever the request change. all thanks to my mail company
 useContext and createContex 
 */
function Row1(){
    const [request, setRequest] = useState<string>(" "); 
    return (
        <section className="content">
            <ReviewContext.Provider value={request} >
                <Review2/>
                <Review updater={setRequest} />
                <Review3/>
            </ReviewContext.Provider>
        </section>
    )
}
function Row2(){
    return (
        <section className="content">
            <USEREF />
            <USEREF2 />
            <USECALLBACK />
            <ToDoList />
            
        </section>
    )
}
function Row3(){
    return (
        <section className="content">

            
        </section>
    )
}
function Row4(){
    return (
        <section className="content">
            <LittleDuck />
            <HOOKS/>
        </section>
    )
}



//Main App
//----------------------------------------------------------------------------------------------------------------------------------->
export default function App(){
    return (
        <div   id='Hooks-App'> 
            <div id='Rows-Hooks' >
                <Row1/>
                <Row2/>
                <Row3/>
                <Row4/>
                <ToastContainer hideProgressBar limit={1} draggable/>
            </div>
            {/**<DucksImages />*/}
        </div>

       
    )
}