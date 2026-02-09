import * as React from 'react';
import { useState} from 'react';
import Button from "../../components/buttons"; 
import { Input, Form} from '../../components/choices';
//divs: 
//content
//Box 
//Sub-Box
import type {FormProps, InputProps } from "../../utils/typing"; 
interface MultiFormProps extends FormProps {
    inputs:InputProps[],

}


//i wanted to create a form with a bunch of diffretents input but i could not do it... :|
export function MultiForm(props:MultiFormProps):React.JSX.Element{
    const listInputs:React.JSX.Element[] = props.inputs.map(element=>{
        return (
            <Input
            labelName={element.labelName}
            className={element.className}
            placeholder={element.placeholder}
            type={element.type}
            value={element.value}
            required={element.required}
           
            />
        )
    })

    const [value,setValue] = useState<string>(""); 
 
    const formHandler = (event:React.FormEvent)=>{
        event.preventDefault() ; 
        props.onSend(value)
        setValue(prev => prev = "" ); 
    }
    const changeHandler = (event:React.ChangeEvent<HTMLInputElement>)=>{
        let v:string = event.currentTarget.value ; 
        setValue(prev => prev = v ); 
    }

    return (
        <form name={props.name} onSubmit={formHandler} id={props.id} className={props.className || 'Form' } >
            {listInputs}

            <button
            className={"Button"}
            type="submit"
            >
            {props.text}
            </button>

        </form>
    )
}

/**
 * 
 *  <section className='Box'>
                //This one have no onChange
                <MultiForm
                inputs={[{
                    labelName:'Write the first number',
                    onChange:changeNumber,
                    name:"num1",
                    type:'text',
                    value:num1
                },{
                    labelName:'Write the second number',
                    onChange:changeNumber,
                    name:"num2",
                    type:'number',
                    value:num2
                },] }
                text='Send the values'
                onSend={()=>undefined}
                 />
            </section>
 */

//8/11/2025 The propotypeof LinkListed Disspaear, and i dunno why :( 
/**
 

function BigBox():React.JSX.Element{
    TrackRender(BigBox) ; 
    //This will only storage the data in an rray and display it into a htmlliselemetn 
    const [newUser,setNewUser] = React.useState<string[]>([]) ; 
    //This wil storage the value into the linklist
    const [user,setUser] = React.useState<string>('') ; 

    const onSend = React.useCallback((value:string)=>{
        if (!checkFalsyPrimitiveValues(value))return ; 
        setNewUser(prev=>[...prev,value]) ; 
        setUser(value) ; 
    },[]) ; 


    return(
        <div className='Sub-Box'>
            <ErrorBoundary  fallback='An error has ocurred :( ' >
                <Form text="Add user at the end of the line (Queue)" onSend={onSend} />
                <button draggable role="cell" >my button </button>
                <USER_NAMES_LIST.Provider  value={newUser} >
                    <MediumBox />
                    <DisplayFiFo userName={user} />
                </USER_NAMES_LIST.Provider>
            </ErrorBoundary>
        </div>
    )
}

// bUG HER ------------> AHHHASDJFALKSJDF ASJDF  ->>>>>>>>>>>>> BNU BUG BHUBU GUB BUG BUG  BUG BUG B UGB UG BSAFD ASFD 
function DisplayFiFo({userName}:{userName:string}){
    TrackRender(DisplayFiFo) ; 
    
    const list:React.RefObject<LinkedList<string>> = React.useRef<LinkedList<string>>( new LinkedList()) ; 
    const [message,setMessage] = React.useState<string>(''); 
    const LIST_NAMES:string[] = React.useContext(USER_NAMES_LIST) ; 
    //remove the item when the user click the button 
    const updateMessage= React.useCallback (()=>{
        if (!list.current)return ; 
        let first= list.current.peek(); 
        let last= list.current.lastPeek(); 
        let text:string = `The first person in the line is "${first || "nobody" }". And the last "${last || "nobody"}" `
        setMessage(text) ; 

    },[])
    function removeItemOnListNames(){
        console.log(list);
        
        if (list.current === null || list.current === undefined) return;
        list.current.poll() ; 
        updateMessage()

    }
    //ad an elemetn into the stack everytime the component re-render
    React.useEffect(()=>{
        if (!checkFalsyPrimitiveValues(userName))return ; 

        linkList.current.offer(userName) ; 
        updateMessage() ; 
        

    },[LIST_NAMES,userName]); 


    //button remove firt element, add elemetn at the end 
    return(
        <div className='Box'>

            <p>{message}</p>

            <Button text="Remove user at the begeggin of the line (Queue)  " command={removeItemOnListNames}  />
        </div>
    )

}

/**Handles only the logic, of storage new use into the LinkList 
function MediumBox():React.JSX.Element{
    TrackRender(MediumBox) ; 
    const LIST_NAMES:string[] = React.useContext(USER_NAMES_LIST) ; 
    return(
        <div className='Box'>
            <List order values={LIST_NAMES} />
        </div>
    )
}

 */



//Here i want to create two differents boxes wher one box only display the number and the another one the logic | 3/11/2025
/**
type CountDownProps = {
    seconds:number,
    pauseClock?:boolean,
    continueClock?:boolean,
}
//export const COUNTDONW_CONTEXT:React.Context<> = React.createContext(); 
TODO: fix the toast bug when the countdonw ends :(   
export function CountDown(props:CountDownProps){
    const [time,setTime] = useState<string>("00:00:00"); 

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
                setTime( result );
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
            setTime(this.NUMBER < 0 ? "Time is up":this.setCounter(this.NUMBER ))
    
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

    const clockRef = React.useRef(new Clock(props.seconds)) ;
    const clock:React.RefObject<Clock> = clockRef  ;
    
    if (props.pauseClock) {
        clock.current.pauseClock(); 
    }
    if (props.continueClock){
        clock.current.init() 
    }
    
    return (
        <div className="Box">
            <p className="Clock-Time" >{time}</p>  
        </div>
    )
}


function CountDown2(){
    const clock:React.RefObject<Clock> = useContext(COUNTDONW_CONTEXT); 
    const onSend = (value:string)=>{
        if (!value)return ; 
        let count:number = Number(value) ;
        clock.current.number = count ; 
        clock.current.init(); 
    }
    

    return (
        <div className="Box">
            <h3>Count Down</h3>
            <Form className='Box' type='number'  placeholder='Write your number in seconds' text='Start Count Down' onSend={onSend}  />
            <div className="content">
                <Button text='Pause counter' command={()=>clock.current.pauseClock()} />
                <Button text='Continue counter' command={()=>clock.current.init()} />
                <Button text='Restar counter' command={()=>clock.current.NUMBER = 0} />
            </div>
        </div>

    )
}
 

 */