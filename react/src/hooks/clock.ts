import React from "react" ; 

class Clock {
    public NUMBER:number  = 0 ; 
    public IntervalId:number | null = null ; 
    public isCounting:boolean = false ; 
    public handler:React.Dispatch<React.SetStateAction<string>> ; 
    constructor (n:number,handler:React.Dispatch<React.SetStateAction<string>>)
    {
        this.NUMBER = n ; 
        this.handler = handler
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
            this.handler( result );
            //console.log(result) ; 
            //console.log("the interval id is from inside the interval :  ", this.IntervalId)
            if(this.NUMBER  < 0){
                if(this.IntervalId === null)return ;
                this.removeSetTimeOut( this.IntervalId ); 
            }
           

        },1000)
        //console.log("The invertal return id is here...")

    }

    private  removeSetTimeOut(intervalId:number){
        clearInterval(intervalId) ; 
        this.handler(this.NUMBER < 0 ? "Time is up":this.setCounter(this.NUMBER ))

        //Bug here :( 
        /**if (this.NUMBER < 0 ){
            let id:Toast.Id = this.showToast()  ; 
            // debugger ; 
            toast.dismiss(id) ; 
        }*/
        
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

    get number(){
        return this.NUMBER
    }

    set number(value:number){
        this.NUMBER = value ; 
    }



}


export function useCountDown(seconds:number ):[string, Clock]
{
    const [counter,setCounter] = React.useState<string>("00:00:00") ; 
    const clockRef = React.useRef(new Clock(seconds,setCounter )) ;
    React.useEffect(()=>{
        clockRef.current.init() ; 
        return ()=>{
            clockRef.current.pauseClock() ; 
        }
    },[])


    return [counter, clockRef.current] 
}

