import * as React from 'react';
import { useState,useEffect,useContext,useRef,useCallback} from 'react';
import Button from "../../components/buttons"; 
import { Input, Form,List,ComboBox} from '../../components/choices';
import {toast,ToastContainer} from "react-toastify"; 
import "react-toastify/ReactToastify.css"; 
// import "./styles/clockStyle.css"; 
import * as Toast from "react-toastify"; 
//divs: 
//content
//Box 
//Sub-Box

/**
 * TO LEARN : 
    - CLOSURE
    - DOM
    - USEEFFECT
    - RENDER 
*/


function random(min:number = 0 , max:number = 1):number {
    return Math.floor(Math.random() * ( max - min  + 1) + min ); 
}


function USEEFFECT():React.JSX.Element{
    const listColor:string[] = ["#010101","#B14203","#32CAC3","#A59F89"]; 
    const [num, setNumber] = useState<number>(0); 
    const [color,setColor] = useState<string>("#010101"); 

    const myCallback:React.EffectCallback = ()=>{
        document.title = `Color ${color} ` ; 
       // console.log("Current number: " + num )
        //console.log("Current Color: " + color )

    } ; 

    console.log("Hi am the function '", USEEFFECT.name , "' !!!");


    const myDepList:React.DependencyList = [num]; 


    const numHandler = (value:string)=>{
        setNumber(Number(value)); 
    }

    const colorHandler = ()=>{
        
        //This ensure us that the color random color will never be same of the previous one ..
        setColor(prev => {
            let newColor:string; 

            newColor = listColor[random(0,listColor.length - 1) ]; 

            while (newColor === prev){
                newColor=listColor[random(0,listColor.length - 1) ]; 
            }

            return newColor ; 
        } ); 
    }

    // we add an empty array in order to excetud only once. 
    //or we can add it elements
    useEffect(myCallback,myDepList); 


    return (
        <section style={{backgroundColor:color}} className={"Box"}>

            <h3>Use Effect Hook</h3> 
            <Form className='Box' type='number' text='Send the number' onSend={numHandler} placeholder='Type a number...' />
            <Button command={colorHandler} text='change color '/>
            <p>Number: {num} </p>



        </section>

    )
}

function USEEFFECT2(){
    const [width, setWidth] = useState<number>(window.innerWidth); 
    const [height, setHeight] = useState<number>(window.innerHeight); 
    console.log("Hi am the function '", USEEFFECT2.name , "' ------->");

    


    


    
    const handleSize =()=>{
        setWidth(window.innerWidth); 
        setHeight(window.innerHeight); 
    }

    useEffect(()=>{
        window.addEventListener("resize",handleSize);

        return ()=>{
            window.removeEventListener("resize",handleSize)
        }

    },[] )

    useEffect(()=>{
        document.title = `Currently Size: ${width}x${height} `

    },[width,height])

    return ( 
        <div className='Box'>
            <h3>Use Effect Hook</h3> 
            <p>Currently window Width: {width}px </p>
            <p>Currently window Height: {height}px </p>
            <p> I still dont get it :(</p>



        </div>
    )
}

function Closures(){
    //Trying with fucntion 
    function func1():[number,()=>number]{
        let age:number = 19 ; 
        function func2(){
            age++; 
            console.log(age); 
            return age ; 
        }

        return [age,func2] ; 
    }; 
    console.log("Hi am the function '", Closures.name , "' -|||||||||||->");


    //trying with class
    class Outter {
        //this value will be remember no matter how many
        // new object of this I create 
        static num2:number = 0 ; 

        public num:number 
        //This number will always be reset (0) every 
        // time i create a new Outter object
        constructor(){
            this.num = 0 ;
        }
    
        inner(){
            this.num ++ ; 
            console.log("the current number is: " + this.num );
            return  this.num;
        }

        inner2(){
            Outter.num2++; 
            console.log("The class number is :  "+ Outter.num2);
            return Outter.num2 ; 
            
        }
    
    }
    
    


    const something = ()=>{
        const [age,increAge] = func1() ; 
        console.log(age);
        increAge();
        increAge(); 
        increAge(); 
        increAge();

        //
        const counter = new Outter(); 
        const counter2 = new Outter(); 
        counter.inner(); 
        counter.inner();  
        counter.inner();  
        counter.inner();  
        counter.inner2(); 
        counter.inner2(); 
        counter.inner2(); 
        counter2.inner2(); 
        counter2.inner2(); 
        counter2.inner2(); 
        counter2.inner2(); 
        counter2.inner(); 







    
    }





    return (
        <div className='Box' >
            <h3>Closure Topic</h3>
            <p> Value:  </p>
            <Button command={something} text='click' />
            <p>Still not :(</p>
            

        </div>
    )
}


function USEEFFECT3(){
    let listName:string[] = ["Stephany","Edward","Sophya", "elizabet"]; 
    const [name,SetName] = useState<string>(""); 
    const change = (event:React.ChangeEvent<HTMLSelectElement>)=>{
        const {value} = event.currentTarget ; 
        SetName(value) ; 
    }; 
    console.log("Hi am the function '", USEEFFECT3.name , "' -###############->");

        //This one executed once and then is delate
    useEffect(()=>{
        console.log("I am the useEffect who handles the DOM event click event ...")

        const something = ()=>{
            console.log("You are clickin the website"); 

        };


        window.addEventListener("click",something )

        return ()=>{
            window.removeEventListener("click",something )
        }

    }, [] )



    useEffect(()=>{
        //debugger; 
        console.log("hello useEffect :( ")
        console.log(`Hello ${name}`); 
        
    },[name])

    return (
        <div className='Box' >
            <h3>Use Effect 3 </h3>
            <ComboBox options={listName} value={name} onChange={change} />
            {/**<Button command={()=>undefined} text='click' />*/}
           <p>{name}</p>
            

        </div>
    )
}

function PokeApi(){
    const [pokemon,SetPokemon] = useState<string>(""); 
    const [Image, setImage] = useState<string>("#");
    const [num, setNum] = useState<number>(0); 
    const [pokeName, setName] = useState<string>("");
    console.log("Am the poiemon component here _______----< plese wacth me I am  alone :|"); 

    let url:string = "https://pokeapi.co/api/v2/pokemon/" ;
     


    const getPokemon = (value:string)=>{
        SetPokemon(value) ; 
    }


    //HERE is another example of how to use useEffect. 
    //to fect data and to do something later with that fect data
    useEffect(()=>{
        //debugger; 
        console.log("The use efect is running...")

        fetch(url+pokemon).then(r=>{
            if (!r.ok)return null ;

            return r.json()
        }
            
            ).then(
                data=>{
                    if (data === null)return ; 

                    let r  = data.sprites?.front_default; 
                    //console.log(r); 
                    //console.log(data); 
                    setImage(r); 
                    setName(data.name )
                }
        )
    },[pokemon] /** , [pokemon,num]*/) //This function will only be executed when the variable pokemon changes

    



    return(
        <div className='Sub-Box'>
              <div className="Box">
                <p>You have click {num} times </p>
                <Button command={()=>setNum(prev => prev + 1 )} text='click me' />
            </div>

            <Form text='send pokemon'  onSend={getPokemon} />

            <div className="Box">
                <img src={Image} />
                <p> {pokeName} </p>
            </div>
            

        </div>
    )
}

/**
 My analogy :
    the restaurant: 
        The owner opens the restaurant (mounting), 
        the cheft preparet the food (rendering)
        the waiter serve the food (DOM)
        repeat the proces of prepare and serve the food 
        untill the night (re-render)

 Mounting: 
    The action of executed all the code, and insert all 
    my components into the html. only once.


 Rendering: 
    The action of running a componenet in order to create
    a visual output. only
        Re-render: 
            The action of repeat the render and display it 
            into the website...


 DOM: 
    the result of a render. it take the finishing render and 
    display it into the website.

 */

 

// The component function that runs during the RENDER phase
export function LifecycleTracker() {
        // 1. STATE DEFINITION
        const [count, setCount] = useState<number>(0);
        
        // 2. RENDERING PHASE: This line runs every single time the component function executes.
        console.log("--- 1. RENDERING: Component function is running (Calculation Phase) ---");
    
        // 3. MOUNTING/RE-RENDERING PHASE: The useEffect hook runs *after* rendering.
    
        // A. MOUNTING EFFECT (Runs only ONCE after the initial mount)
        useEffect(() => {
            console.log("--- 3. EFFECT: MOUNTED (Runs only once, setup complete) ---");
            // This is where you would fetch API data or set up global listeners.
            
            // The cleanup function for the Mounting Effect runs only when the component UNMOUNTS
            return () => {
                console.log("--- 5. CLEANUP: Component is UNMOUNTING (Leaving the screen) ---");
            };
        }, []); // 👈 The empty array ensures it runs only ONCE.
    
        // B. WATCHER EFFECT (Runs on mount AND every time 'count' changes)
        useEffect(() => {
            // CLEANUP for the previous run of this specific effect happens first (if not the first run)
            console.log(`--- 4. CLEANUP: Watcher Cleanup Ran (Before new effect runs) ---`);
    
            // NEW EFFECT RUN
            console.log(`--- 4. EFFECT: 'count' Watcher Ran. Current count is ${count} ---`);
            
            // This cleanup runs right before the next re-render where 'count' changes again.
            return () => {
                console.log(`--- 4. CLEANUP: Prepared for next 'count' change ---`);
            };
        }, [count]); // 👈 Runs whenever the 'count' state changes.
    
    
        // --- RETURN PHASE --- (The HTML structure is calculated)
        return (
            <div style={{ padding: '20px', border: '1px solid #ccc' }}>
                <p>Current Count: **{count}**</p>
                <button onClick={() => setCount(count + 1)}>
                    Increment
                </button>
                <p>Check the console to see the sequence of Mounting and Rendering!</p>
            </div>
        );
    }

"use client";
function ServerComponent(){
    useState()
    return <div> </div>
}

/**Create a simple digital clok 
 * 1. You must use the useEffect hook
 * 2. Uset the setInterval function
 */
function DigitalClock(){
    const [time,setTime] = useState<string>(""); 
    const [now,setNow] = useState<string>("AM"); 
    

    useEffect(()=>{

        const updateTime = ():string=>{ 
            const setZero = (num:number):string=> num >= 10 ? `${num}`:`0${num}`; 
            const date = new Date();
            let hour:number = date.getHours(); 
            let minute:number = date.getMinutes(); 
            let seconds:number = date.getSeconds() ; 
            let currentTime = `${setZero(hour)}:${setZero(minute)}:${setZero(seconds)}` ; 
            if (hour >= 12){
                    setNow("PM");

            }else{
                    setNow("AM");
            }

            return currentTime
        }

        let id:number = setInterval(()=>setTime(()=>updateTime()) ,1000 );

        return ()=>clearInterval(id) ; 
    },[])
    //console.log("I am the digital clock function .:)")
    



    return (
        <div className="Box">
            <h3>Digital Clock</h3>
            <div className="content" >
                <p className="Clock-Time" >{time}</p>
                <p> {now} </p>
            </div>
        </div>

    )
}
/**
 
function CountDown(){
    const [time,setTime] = useState<string>("00:00:00"); 
    //const [txt,setTxt] = useState<string>(""); 
    class Clock {
        public NUMBER:number  = 0 ; 

        consturctor (num:number){
            this.NUMBER = num ; 

        }

        

    }
    

    const onSend = (value:string)=>{
        if (!value)return ; 

        let count:number = Number(value) ;
 
            
        let intervalId:number = setInterval(()=>{  
            let result: string = setCounter(count); 
            count -- ; 
            setTime( result );
            console.log(intervalId);
            
            

            if(count<= 0){
                clearInterval(intervalId)
                setTime("Time is up")
                //Bug here :( 
                let id:Toast.Id = showToast()  ; 
               // debugger ; 
                toast.dismiss(id) ; 
                
            }
           

        },1000)


       
    }

    const setCounter = (num:number):string=>{
        let hour:number = Math.floor(num / 3600) ; 
        let minute:number = Math.floor(num / 60) % 60 ;
        let seconds:number =num % 60 ; 
        const setZero:Function = (num:number):string=> num >= 10 ? `${num}`:`0${num}`; 
        let currentTime:string = `${setZero(hour)}:${setZero(minute)}:${setZero(seconds)}` ; 
        return currentTime

    }

    const showToast = ():Toast.Id=>{
        return toast.success<string>("Time is up")  ; 
    }

    



    return (
        <div className="Box">
            <h3>Count Down</h3>
            <Form type='number'  placeholder='Write your number in seconds' text='Start Count Down' onSend={onSend}  />
            <Form type='number'  placeholder='Write your number in minutes' text='Start Count Down' onSend={(value)=>onSend(value * 60) }  />
            <Form type='number'  placeholder='Write your number in hour' text='Start Count Down' onSend={onSend}  />
            <div className="content" >
                <p className="Clock-Time" >{time}</p>
            </div>
            <ToastContainer />
        </div>

    )
}

 
 */

function CountDownDisplayNumber(){
    const currentTime:string = useContext(COUNTDOWN_CONTEXT) ; 
    return (
        <div className="Box Count-Count-Number">  
            <p className="Clock-Time" >{currentTime}</p>
        </div>
    )
}
function CountDownLogic(props:{seconds?:number,setTime:React.Dispatch<React.SetStateAction<string>>}){
   // const [time,setTime] = useState<string>("00:00:00"); 
    //console.log("I am inside the ConuntDown fucntion :)");
    //This function is call everytime the time is change 
    //const [txt,setTxt] = useState<string>(""); 
    class Clock {
        public NUMBER:number  = 0 ; 
        public IntervalId:number | null = null ; 
        public isCounting:boolean = false ; 

        constructor(num:number){
            this.NUMBER = num ; 
            this.IntervalId = null ; 
            this.isCounting = false

        }

        private setCounter = (num:number):string=>{
            let hour:number = Math.floor(num / 3600) ; 
            let minute:number = Math.floor(num / 60) % 60 ;
            let seconds:number =num % 60 ; 
            const setZero:Function = (num:number):string=> num >= 10 ? `${num}`:`0${num}`; 
            let currentTime:string = `${setZero(hour)}:${setZero(minute)}:${setZero(seconds)}` ; 
            return currentTime
        }

        private configClockLogic():void{
            

            this.IntervalId = setInterval(()=>{  
                let result: string = this.setCounter(this.NUMBER ); 
                this.NUMBER  -- ; 
                props.setTime( result );
                console.log(result) ; 
                console.log("the interval id is from inside the interval :  ", this.IntervalId)
                if(this.NUMBER  < 0){
                    if(this.IntervalId === null)return ;
                    this.removeSetTimeOut( this.IntervalId ); 
                }
               
    
            },1000)
            console.log("The invertal return id is here...")

        }

        private  removeSetTimeOut(intervalId:number){
            clearInterval(intervalId) ; 
            props.setTime(this.NUMBER < 0 ? "Time is up":this.setCounter(this.NUMBER ))

            //Bug here :( 
            if (this.NUMBER < 0 ){
                let id:Toast.Id = this.showToast()  ; 
                // debugger ; 
                toast.dismiss(id) ; 
            }
            
            this.isCounting = false ;
            
        }

        init():void{
            if (this.isCounting)return ; 

            if (this.NUMBER <= 0)return ;
            this.configClockLogic(); 
            this.isCounting = true ; 
     
        }

        

        pauseClock(){
            if (!this.isCounting)return ; 

            //debugger ; 
            const ID:number|null = this.IntervalId ; 
            if(ID === null)return ; 
            this.removeSetTimeOut( ID) ; 
             
            //debugger ;   
        }

        showToast = ():Toast.Id=>{
            return toast.success<string>("Time is up")  ; 
        }


        get number(){
            return this.NUMBER
        }

        set number(value:number){
            this.NUMBER = value ; 
        }



    }

    const clockRef = React.useRef(new Clock(props.seconds !== undefined ? props.seconds : 0 )) ;
    const clock:React.RefObject<Clock> = clockRef  ;
    

    const onSend = (value:string)=>{
        if (!value)return ; 
        let count:number = Number(value) ;
        clock.current.number = count ; 
        clock.current.init(); 
    }

    const PauseClock = ()=>{
        clock.current.pauseClock(); 

    }
    

    return (
        <div className="Box Count-Count-Logic ">
            <h3>Count Down</h3>
            <Form className='Box' type='number'  placeholder='Write your number in seconds' text='Start Count Down' onSend={onSend}  />
            <div className="content">
                <Button text='Pause counter' command={PauseClock} />
                <Button text='Continue counter' command={()=>clock.current.init()} />
                <Button text='Restar counter' command={()=>clock.current.NUMBER = 0} />
            </div>    
        </div>

    )
} 

export const COUNTDOWN_CONTEXT:React.Context<string> = React.createContext("00:00:00") ; 
export function CountDown(){
    const [time,setTime] = useState<string>("00:00:00"); 
    return (
        <div className="Sub-Box Count-Down">  
            <COUNTDOWN_CONTEXT.Provider value={time}  >
                <CountDownDisplayNumber />
                <CountDownLogic setTime={setTime}/>
            </COUNTDOWN_CONTEXT.Provider>
        </div>
    )
}


/**
 A toast is just a beautiful style to send notifivations
 Type: 
    - succes: 
    - error: 
    - loading:
    - info: 
   - warn:

Themes: 
    - dark:
    - light: 
    - colored: 

Transitons: 
    - Bounce: 
    - Slide: 
    - Zoom: 
   -  Flip: 

Roles: 
    -alert: 



 */




function TestToast(){
    const showToast= ()=>{
        toast<string>("I am a toast :)"); 
       
    }; 

    

    const showToast2= ()=>{
        toast.info<React.JSX.Element>(
            <div>
                This is my button toast 
                <Button text='Toast!' command={()=>undefined}  />
            </div>

        ); 
       
    }; 

    const showToast3 = ()=>{
        let id:Toast.Id = toast.success<string>("This is a succes message", 
        {
            position:"bottom-left", 
            delay:1000,

        })

        toast.done(id)
        let active:boolean = toast.isActive(id) ; 
        console.log("MY third toast is active: ", active);

        toast.play
        toast.pause
        toast.promise
        toast.clearWaitingQueue(); 
        let id2:Toast.Id = toast.dark("This is dark"); 
        console.log("Id no 2. ", id2)
        
        const b : Toast.OnChangeCallback = (value:Toast.ToastItem):void=>{
            value.content
        } ;
        toast.onChange(b )
        
        
        

    }
   

    return (
        <div className="Box">
            <h3>Toast</h3>
            
            <Button command={showToast} text="Test 1 " />
            <Button command={showToast2} text="Test 2 " />
            <Button command={showToast3} text="Test 3" />

            <ToastContainer
            hideProgressBar={false}
            draggable={true}
            className="Toast-Class"
            theme='light'  
            role='alert'
            aria-label='Monserrat'
            closeOnClick={true}
            autoClose={3000}
            toastClassName={"Toast-Class-Name"}
            rtl={false}
            position='top-center'
            closeButton={true}
            limit={3}
            newestOnTop={true}
            pauseOnHover={false}
            stacked={false}
            pauseOnFocusLoss={false}
            
            
            
           
           

            /> 
        </div>
    )
}

//import React,{useContext,createContect,Context} from "react";  
import {MyComponentA} from "../../components/childrenA"; 
//import {MyComponentB} from "./components/childrenB"; 
//import {MyComponentC} from "./components/childrenC "; 
/**
the child A has B
the child B has C 
the child C has nothing

 */

function USECONTEXT(){
    return(
        <div className="Box">
            <h3>use Context </h3>
            <p>I am the father :) </p>
            <MyComponentA /> 
            
        </div>
    )
}


//##########################################
function Row1():React.JSX.Element{ 
    const [text,setText] = useState<string>("");
    const [result, setResult] = useState<string>(""); 
    const [num1, setNum1] = useState<number>(); 
    const [num2, setNum2] = useState<number>(); 
    const [names, setNames] = useState<string[]>([]); 

    const formHandler = (value:string)=>{

        setText(prev=>{
            return greet(value);
        })

        if (!value)return ; 

        setNames(prev => [...prev,value]); 
      

        //setName(prev => prev = "" ); 

    }
    const sumNumber = (event:React.FormEvent)=>{
        event.preventDefault(); 
        if(num1  === undefined || num2 === undefined) return ; 

        let r: number = num1 + num2 ; 
        let t:string = num1 > num2 ? "The number " + num1 +" is greater than " + num2 :"The number " + num1 +" is Lower than " + num2 ;
        setResult(prev => prev = "The result is: " + r + "  |  "+ t) ; 
        setNum1(prev => prev =undefined); 
        setNum2(prev => prev = undefined); 

       

    }
    const changeNumber = (event:React.ChangeEvent<HTMLInputElement>)=>{
        let n: string = event.currentTarget.name ; 
        let v:number = Number(event.currentTarget.value);
         
        if (n==="num1"){setNum1(prev => prev = v);return ; }
        setNum2(prev => prev = v); 
    }

    const  greet = (userName?:string):string=>{
        return "Hello " + (userName || "user ")
    }

    const removeItem = (event:React.MouseEvent<HTMLLIElement>)=>{
        const {textContent} = event.currentTarget ; 
        if (textContent === null)return ; 
        setNames(prev => prev.filter(e => e !== textContent)); 
    }

    return(
        <div className='content' >

            <section className="Box">
                <h3>Greet User</h3>

                <Form className='Box' placeholder='What is your name' text="Submit your name here"  onSend={formHandler} />
                <p>{text}</p>
            </section>

            <section className='Box'>
                <h3>Numbers</h3>
                <form className='Box' onSubmit={sumNumber}>
                    <Input onChange={changeNumber} name="num1" type='number' labelName='Write the first number' value={num1} />
                    <Input  onChange={changeNumber}  name="num2" type='number' labelName='Write the second number' value={num2} />
                    <Button  command={()=>undefined} text='send number' type='submit'  />
                    <p>{result}</p>
                </form>
            </section>

            <section id="List" className="Box">
                <h3>Names</h3>
                <List valueClicked={removeItem} values={names } />
            </section>

            

           

        </div>
    )
}

function Row2():React.JSX.Element{ 
    
    console.log("I am the ", Row2.name , "  FUNCTION HERE, i am the one who handles all the components :) ")
    return(
        <div className='content' >
            <USEEFFECT3/> 
            <USEEFFECT/> 
            <USEEFFECT2/> 
            <Closures/>


        </div>
    )
}

function Row3():React.JSX.Element{ 
    console.log("I am the Row no. 3")
    return(
        <div className='content' >
            <LifecycleTracker/>
            <PokeApi/>
        </div>
    )
}

function Row4():React.JSX.Element{ //
    console.log("I am the Row no. 4")
    return(
        <div className='content' >
            <DigitalClock/>
            <CountDown />
        </div>
    )
}
function Row5():React.JSX.Element{ 
    console.log("I am the Row no. 5")
    return(
        <div className='content' >
            <USECONTEXT/>

            <TestToast/>
        </div>
    )
}

//##########################################
export default function App(){
    return (
        <div>
            <Row1/>
            <Row2/>
            <Row3/>
            <Row4/>
            <Row5/>

        </div>
    )
}
/**
 *  return(
        <div className='content' >
            <section className="Box">
                <form className="Box" onSubmit={formHandler} >
                    <Input onChange={changeH} value={name}  placeholder='What is your name'/>
                    <Button type="submit" text="Submit your name here" command={()=>undefined} />
                    <p>{text} </p>
                </form>
            </section>
        </div>
    )
 */


function Component1(){return <p>Hello world</p>}
function Component2(){return <p>Bye world</p>}
/**HTML TEXT DECORATOR ....
 * 
 <b></b>
            <i></i>
            <big></big>
            <small></small>
            <sub></sub>
            <sup></sup>
            <ins></ins>
            <del></del>
            <mark></mark>
 */


export function MyApp(){
    const something = ()=>{
        console.log("You are clickin the website"); 

    };

    const [txt, setTxt] = useState<string>(""); 

    useEffect(()=>{
        window.addEventListener("click",something); 
        return ()=>{
            window.removeEventListener("click",something); 
        }
    })

    return (
        <div>
            <Component1 />
            <button onClick={()=>setTxt("react is complicated :|")} >click me </button>
            <p>{txt}</p>
            <Component2 />
        </div>
    )
}
//When react update the all this element into the thml is call "render"
//When everything of this is finisih to render is call "mount"