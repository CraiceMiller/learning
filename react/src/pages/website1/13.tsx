import React, { Children } from "react" ; 
import {TrackRender,ErrorBoundary,useGetData,useDraggable,useDraggableEnter} from "@hooks/react-utils" ; 
import {toast,ToastContainer} from "react-toastify" ; 
import {quickSort,binary} from "@utils/utils" ; 
import { ComboBox, List } from "@components/choices";
import * as Query from "@tanstack/react-query" ; 
import {CreateSlot,SwapyContainer,CreateItem} from "@lib/swap" ; 

//----------------------------------------------------------------------------------------------------------------------------------->
//error handler 


//crypto.randomUUID
//useQuery



//----------------------------------------------------------------------------------------------------------------------------------->


class Counter extends React.Component  {
    public state = {num:0} 

    increment(){
        this.setState({num:this.state.num++})
    }
    dincrement(){
        this.setState({num:this.state.num--})
        
    }
    render(): React.ReactNode {
        return (
            <div className='Box'>
                <h3>My Class componenet Coutner :3</h3>
                <button onClick={this.increment} >increas me </button>
                <button onClick={this.dincrement} >Dincreas me </button>
            </div>
        )
        
    }

}

//Something 
//----------------------------------------------------------------------------------------------------------------------------------->


const UsersList:string[] = [
    'Hersy', 
    'Craice', 
    'Ashely',
    'Miseru', 
    'Stephany', 
    'Rossy'
]



type Messaure = {height:number,width:number}
//5 useContext, here this value will be share for alll the component inside a father 
const messageContext = React.createContext<string>('')
function Something(){
    TrackRender(Something,true) ; 
    const getSize = ():Messaure=>{
        const { innerHeight,innerWidth } = window; 
        return {height:innerHeight,width:innerWidth}
    }
    //1. useState, get the user value as string, and a value to update the user
    const [user,setUser] = React.useState('') ; 
    const [messaure,setMessaure] = React.useState<Messaure>(getSize()) ;

    //2. useEffect; this will only when amount, this run code that is not relate with react.
    const m = ()=>{setMessaure(getSize())} ; 
    React.useEffect(()=>{
        window.addEventListener('resize',m) ; 
        console.log('I am been called after the re-render ends') ; 

        return ()=>{
            window.removeEventListener('resize',m) ; 
        }

    },[])

    //4. useRef, This value will remember my div value for the rest of the cicle-life 
    const divRef:React.RefObject<HTMLDivElement | null> = React.useRef<HTMLDivElement | null >(null) ; 
    const keepIncrementing:  React.RefObject<boolean> = React.useRef<boolean>(true) ; 

     //5.  useReducer
     type counterState = 'increment' | 'dincrement' ; 
     function myReducer(state:number,action:string):number{
        switch (action) {
            case 'increment':
                return state + 1;

            case 'dincrement': 
                return state - 1 ; 

        
            default:
                return state;
        }

    }
    const [value,setValue] = React.useReducer<number,[counterState]>(myReducer,0)


    //6. useCallback, i dunno :( 
        //this click function will change when the value change 
    const click = React.useCallback((event:React.MouseEvent<HTMLButtonElement>)=>{
        toast('The button has been clicked :)')
        console.log(event);
        console.log(value);


        if (value >= 5){
            keepIncrementing.current = false; 

        }
        if (value <= 0){
            keepIncrementing.current = true ; 
        }
        console.log(keepIncrementing.current);
        

        if (keepIncrementing.current){
            setValue("increment")
        }else{
            setValue("dincrement")
        }

    },[value]) ; 

    const pointer = React.useCallback((event:React.MouseEvent<HTMLDivElement>)=>{
        //console.log(event);
        //console.log(divRef); 
        //console.log(divRef.current?.style)
        let div = divRef.current ; 
        if (!div)return ; 
        div.style.boxShadow = '0 0 15px purple' ; 

    },[]); 
    const pointerLeave = React.useCallback((event:React.MouseEvent<HTMLDivElement>)=>{

        let div = divRef.current ; 
        if (!div)return ; 
        div.style.boxShadow = '' ; 

    },[]); 

    const ChangeHanlder = React.useCallback((event:React.ChangeEvent<HTMLSelectElement>)=>{
        console.log(event);
        const {value} = event.currentTarget ; 
        setUser(value) ; 
    },[])
    //7. useMemo 
    const memorizeValue = React.useMemo<string>(()=>{
        let sortedUser = quickSort(UsersList) ; 
        let UserIndex = binary(sortedUser,user) ;
        if (UserIndex === -1)return '' ; 

        return sortedUser.at(UserIndex) || '' ; 

    },[user])

    //9. useLayoutEffect
    React.useLayoutEffect(()=>{
        console.log('I am been called before the re-render ends') ; 

    },[])

    return (
        <div ref={divRef} onPointerLeave={pointerLeave} onPointerOver={pointer}  className='Box'>
            <h3>More Hooks</h3>
            <p>9/11/2025</p>

            <ErrorBoundary  fallback='Something Goes Wrong' >
                <p>Current Size: Width-{messaure.width}, Height {messaure.height} </p>
                <p> Current Number is {value} </p>
                <ComboBox options={UsersList} value={user} onChange={ChangeHanlder}   />

                <messageContext.Provider value={user} >
                    <DisplayMessage value={memorizeValue} click={click} />
                </messageContext.Provider>

            </ErrorBoundary>

        </div>
    )
}

/**
1. useState = hook that gets and update a certain element. It trigers a re-render
2. useEffect = hook that runs (after the render) a block of code aside the react enviroment when only mount,every re-render or when a certain value change. It Does not trigger a re-reder 
3. useContext = hook that allows us to share data to  diferent child component. It trigger a re-render 
4. useRef = hook that  remembers the initial data(when mounts) and storage during the whole cicle-life. It Does not trigger a re-render
5. useReducer = same as useState but handles differentes logic at once. It trigger a re-render
6. useCallback = hook that remembers a function and it can be share with differents componnets. it will 
keep the same when the function amount, at least that a depency inside it change, if we want ot use a value
outside to this function. if we want to keep the function as the same we use an emptry array.    It Does not trigger a re-render 
7. useMemo = hook that remembers a value.  It Does not trigger a re-render 
8. useImperativeHandle =
9. useLayoutEffect = same to useEffect, but run before the re-renders ends
10. useDebugValue = It trigger a re-render

 */

/**
 Trigger re-render : 
 useState
 useContext

 No trigger re-render: 
 useEffect
 useRef
 useCallback 

 Can be shared with another components 
 useCallback
 useContext

 Remember things: 
 useCallback 
 useRef 
 useMemo 

 */

/**
 
state Management:
    works with react state
        - useState
        - useReducer
        - useSyncExternalStore

Effect Hooks: 
    performs  side effects
        -useEffect
        -useLayoutEffect
        -useInsertionEffect

Ref Hooks
    works with refernce JavaScript values or DOM elemetns
        -useRef
        -useImperativeHandle 

Performace Hooks
    improve app perforamce with memoization
        -useMemo
        -useCallback
Context Hooks
    hook to read from reactg context 
        -useContext 

Transition Hooks: 
    to use transitions for better user experiences
        -useTranstiton
        -useDeferredValue

Random Hooks: 
    -useDebugValue
    -useId

Powerfull Hooks: 
    -useFormStatus
    -useFormState
    -useOptimistic

 
 */

function DisplayMessage({click,value}:{value:string,click:(event:React.MouseEvent<HTMLButtonElement>)=>void}){
    TrackRender(DisplayMessage)
    const message = React.useContext(messageContext) ;
    //10. 
    React.useDebugValue(message) ;  

    return (
        <aside style={{border:'2px solid white', padding:'2vw'}} >
            <p> Current User is: {message} </p>
            <button onClick={click} >click me </button>
            <h4>{value}</h4>
        </aside>
    )
}

//Ducks 11/11/2025
//----------------------------------------------------------------------------------------------------------------------------------->

//This just se the queryclient needed
const queryClient = new Query.QueryClient() ; 
/**This will only get one image from a random duck */
// Define the props interface to include the forwarded ref
interface DuckImagesProps {
    n: number;
    // We add a specific ref type for the image element
    ref?: React.Ref<HTMLImageElement>; 
    title?:string; 
}

// Wrap the component with React.forwardRef
const DuckImages = React.forwardRef<HTMLImageElement, DuckImagesProps>(({ n,title }, ref) => 
{
    const { data, isLoading, isError } = useGetData([`Duck No. ${n}`], '/api/api/random'); 
    
    if (isLoading) {
        //debugger ; 
        return <p>Loading...</p>;
    }
    if (isError) {
        return <p>Error!!!</p>;
    }
    

    return (
        <img
            draggable
            title={title}
            ref={ref} 
            src={data.url}
            className="Ducks" 
        />
    );
});




// If you need to export this function, remember to use the forwardRef version:
// export default DuckImages;
/**Here display the list of image and try to make draggable */
function ShowDuckList():React.JSX.Element
{
    //The functions are in the App fucnction component 
    TrackRender(ShowDuckList) ; 
    const imgRef = React.useRef<HTMLImageElement | null>(null) ; 
    React.useEffect(()=>{
        const firstDuck:HTMLImageElement | null = imgRef.current; 
        let speed:number = 1; 
        let currentSpeed:number = 1; 
        //debugger; 
        
        if (firstDuck === null)return ; 
        //debugger; 
        function lerp(a:number,b:number,t:number):number
        {
            return a+ (b-a) * t; 
        }
        function spin():number
        {
            if (firstDuck === null)return 1 ;
            currentSpeed = lerp(currentSpeed,speed,0.1) ; 
            firstDuck.style.transform += `rotate(${currentSpeed}deg)`; 
            return requestAnimationFrame(spin) ; 
        }
        let id:number = spin() ; 
        const addSpeed = ()=>{speed *= 2;};
        firstDuck.addEventListener('click',addSpeed) ; 
        //debugger; 
        
        return ()=>{
            cancelAnimationFrame(id) ; 
            firstDuck.removeEventListener('click',addSpeed) ; 
        }

    },[imgRef.current]); 

    const swapHandler = (event:Swapy.SwapEvent)=>{
        toast(`${event.draggingItem} move to ${event.toSlot}!`)

    }

    return (
        <aside className='Box'>
            <ErrorBoundary fallback='Something goes wrong' >
                 <h3>Little <big> Ducks </big>  Here</h3>
                <p><small> 11/11/2025 </small> </p>
                <p>  ducks are cute  </p>
                <SwapyContainer onSwapy={swapHandler}  >
                    <List 
                    order
                    values={
                        [1,2,3,4,6,7,8,9,10].map(i=>(
                            <CreateSlot
                            slotName={`slot-no-${i}`}
                            className="Ducks-Image-Slots"
                            itemIside
                            itemProps={{
                                title:`Duck No ${i}`,
                                itemName:`Duck-no-${i}`,
                                children:<DuckImages
                                n={i}
                                title={`Duck no ${i}`}
                                ref={i === 1 ?imgRef:undefined}
                                key={i} />
                            }}
                            />
                        )
                        )

                    }
                    />
                </SwapyContainer>
                {/**<div className='Dragging' style={{position:'absolute', height:'200px',width:'200px',cursor:'move',backgroundColor:'white' }} ></div>*/}
            </ErrorBoundary>
        </aside>
    )

}

function DragAttempt():React.JSX.Element
{
    useDraggable('.Chess-Pice') ; 
    useDraggableEnter('.square') ; 
    return (
        <div>
            <h3>Drag things using math equation </h3>
            <p><small>12/11/2025</small> </p>
            <section id='Game-Board'>
                <div className='row'>
                    <div className="white square" >
                        <img 
                        id='Pown'
                        alt='just a pice'
                        className="Chess-Pice pown"
                        src='https://static.vecteezy.com/system/resources/thumbnails/068/086/457/small/glossy-black-pawn-chess-piece-strategic-game-single-object-classic-strategy-game-piece-transparent-background-png.png'/>

                    </div >
                    <div className="black square"></div>
                    <div className="white square"></div>
                    <div className="black square"></div>

                </div>
                <div className='row'>
                    <div className="black square"></div>
                    <div className="white square" >
                    </div >
                    <div className="black square"></div>
                    <div className="white square"></div>
                </div>
                

                <p id='info'></p>
            </section>
        </div>
    )
}
import * as Swapy from "swapy" ; 

function DragSwapy():React.JSX.Element 
{
    const divRef = React.useRef<HTMLDivElement| null>(null) ;

    //Working with the swap 
    React.useEffect(()=>
    {
        const cont = divRef.current ; 
        if (cont === null) return ; 
       

            //creating the swapy element ; 
        const mySwap:Swapy.Swapy= Swapy.createSwapy(cont) ;  
        mySwap.enable(true); 
 
            //event 
        mySwap.onSwap((event: Swapy.SwapEvent)=>
        {
            console.log('i am a swap event :) ')
            console.log(event);
            
        })

        return ()=>
        {
            mySwap.destroy()
        }

    },[divRef.current])

    return (
        <section className='Box'>
            <h3>SWAPY DRAG LYBRARY ... </h3>
            <p>12/11/2025  </p>
            <div id='swapy-container' ref={divRef} style={{ 
                display: 'flex', 
                gap: '10px', 
                border: '2px solid #58c', 
                padding: '10px' 
            }}>
                {/**<div data-swapy-slot='slot-0' style={{ minWidth: '100px', minHeight: '100px', border: '1px dashed gray' }} >
                    <div data-swapy-slot='item-A' style={{ background: '#333', padding: '10px', color: 'white' }} >
                        <h2>My attempt </h2>
                    </div>

        </div>*/}
                
                {/* 1. Slot A: The area where an item can be dropped */}
                <div 
                    data-swapy-slot="slot-1" 
                    style={{ minWidth: '100px', minHeight: '100px', border: '1px dashed gray' }}
                >
                    {/* 2. Item A: The draggable element inside the slot */}
                    <div 
                        data-swapy-item="item-a"
                        style={{ background: '#333', padding: '10px', color: 'white' }}
                    >
                        Item A
                    </div>
                </div>

                {/* 1. Slot B */}
                <div 
                    data-swapy-slot="slot-2" 
                    style={{ minWidth: '100px', minHeight: '100px', border: '1px dashed gray' }}
                >
                    {/* 2. Item B */}
                    <div 
                        data-swapy-item="item-b"
                        style={{ background: '#0f0', padding: '10px', color: 'white' }}
                    >
                        Item B
                    </div>
                </div>

                {/* 1. Slot C (Empty) */}
                 <div 
                    data-swapy-slot="slot-3" 
                    style={{ minWidth: '100px', minHeight: '100px', border: '1px dashed gray' }}
                 >
                    {/* This slot is empty, waiting for an item */}
                 </div>
            </div>

        </section>
    )
}



function MyGame():React.JSX.Element
{
    let MY_SLOTS = [] ;
    const [message,setMessage] = React.useState<string>('') ; 
    for (let index = 1; index < 6; index++) {
        if(index <= 3){
            MY_SLOTS.push(
                <CreateSlot
                className="My-Slots"
                slotName={`slot-${index}`} 
                itemIside
                itemProps={{
                    className:"My-Items",
                    itemName:`item-${index}`, 
                    children:<h2>{index}</h2>
                }
                }
                />
            )
            continue ; 
        }

        MY_SLOTS.push(
            <CreateSlot
            className="My-Slots"
            slotName={`slot-${index}`} 
            />
        )
    }
    const divRef = React.useRef<HTMLDivElement | null> (null) ; 
    React.useEffect(()=>
    {
        const container = divRef.current ; 
        if (container === null)return ; 
        //Crating the swap 
        const My_Current_Swapy = Swapy.createSwapy(container,
            {
                animation: "spring", 
                //autoScrollOnDrag:true, 
                //dragOnHold:true, 
                //swapMode: 'hover'

        }) ; 
        My_Current_Swapy.enable(true ) ; 

        //event : 
        My_Current_Swapy.onSwap((event:Swapy.SwapEvent)=>
        {
            console.log(event);
            let text:string = `<< ${event.draggingItem} >> item  move to << ${event.toSlot.toUpperCase()} >> slot ` ; 
            setMessage(text) ; 
            toast('you have dragg an element :) ' ) ; 
            
        })


    },[divRef.current])

    return (
        <section className="Box My-Game" >
            <h3>Try my Funny Game  </h3>
            <p>{message} </p>
            <div ref={divRef} className="Swapy-Container"   id='My-Game-Container' >
                {MY_SLOTS}
            </div>
        </section>

    )
}

function Something2 ()
{
    const Swap = (event:Swapy.SwapEvent)=>{
        console.log(event);    
        toast(`${event.draggingItem} move to ${event.toSlot}`)
    }; 

    return (
        <div className='Box' >
            <h3>My swapy hook container</h3>
            <p><small>13/11/2025 at 13:00</small> </p>
            <ErrorBoundary fallback='Something goes wrong' >
                <SwapyContainer   onSwapy={Swap}  >
                    <CreateSlot  slotName="slot-A" />
                    <CreateSlot  slotName="slot-B" />
                    <CreateSlot  slotName="slot-C" >
                        <CreateItem itemName="item-1" title="an object" children={<h2>Box No.1</h2>} /> 
                    </CreateSlot>
                </SwapyContainer>
            </ErrorBoundary>
        </div>
    )
}

//Rows
//----------------------------------------------------------------------------------------------------------------------------------->

function Row1(){

    return (
        <section className="content">
            <DragAttempt/>
        </section>
    )
}
function Row2(){
    return (
        <section className="content">
            <DragSwapy /> 
            <Something/>
            

            
        </section>
    )
}
function Row3(){
    return (
        <section className="content">
            <MyGame />
            
        </section>
    )
}
function Row4(){
    return (
        <section className="content">
            <Something2 />

        </section>
    )
}



//Main App
//----------------------------------------------------------------------------------------------------------------------------------->


export default function App(){
    useDraggable('.Dragging') ;
    useDraggable('.Ducks') ;
    return (
        <div   id='Hooks-App'> 
            <div id='Rows-Hooks' >
                <Row1/>
                <Row2/>
                <Row3/>
                <Row4/>
                <ToastContainer
                
                limit={2}
                draggable
                theme="dark"
                draggableDirection="y"
                position="bottom-left"
                pauseOnHover
                autoClose={2000}
                />
            </div>
            {/**<DucksImages />*/}
            <Query.QueryClientProvider client={queryClient}  >
                 <ShowDuckList /> 
            </Query.QueryClientProvider>
        </div>

       
    )
}