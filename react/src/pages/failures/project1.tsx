import * as React from 'react';
import { useState } from 'react';
import Button from "../../components/buttons"; 
import {Input,ComboBox,List,Toggle,DivToggle} from "../../components/choices"; 
//const Values = new Map ([["km",1000],["m",100],["cm",10] ])





interface ConverProps{
    logic(to:string):number, 
    ConverG(amount:number, to:string):number,
    ConverPound(amount:number, to:string):number,
    /**This is the main logic to work with  */
    converter<V>(amount:number,unit:string, to:string ):number,

}

type Methods = {
    g:(amount:number, to:string)=>number, 
    kg:(amount:number, to:string)=>number, 
    pound:(amount:number, to:string)=>number, 

}

class Convert implements ConverProps {

    static methods:Methods ={
        g:Convert.prototype.ConverG, 
        pound:Convert.prototype.ConverPound, 
        kg:Convert.prototype.ConverKg,
    }

    static Values = new Map ([["kg",1000],["g",1000]]) ; 

    logic(to:string):number{
        const r:number| undefined = Convert.Values.get(to);
        return r === undefined ? 0:r; 
    }



    public ConverG(amount:number, to:string):number{ 
        const r:number = amount / Convert.prototype.logic(to)  ; 
        return r
    }

    public ConverKg(amount:number, to:string):number{ 
        //Why i cannot do this this.logic(to) ; 
        return amount * Convert.prototype.logic(to)   ; 
    }
    
    public ConverPound(amount:number, to:string):number{
        return amount * (453.592 / this.logic(to )) ; 
    }
    
    

    //1. Generics
    public converter<V extends keyof Methods>(amount:number,unit:V, to:string):number{
        if (unit === to)return amount ; 

        const fn = Convert.methods[unit]; 
        if (fn ===undefined)return 0 ; 
        const r = fn(amount,to ); 
        return r
    }

    get values (){
        return Convert.Values.keys
    }
    

}





export default function App(){
    //2. Use State
    const listWeights:string[] = ["kg","g"]; 
    const [value,setValue] = useState<number>(0);
    const [userValue,setUserValue] = useState<number>(0);
    const [weight,setWeight] = useState< keyof Methods | string >("g");
    const [result, setResult] = useState<string>("kg") ; 


    const sumbitHandler = (event:React.FormEvent)=>{
        event.preventDefault() ; 
        let r:number = new Convert().converter(userValue,weight as keyof Methods ,result); 
        setValue(prev=> prev =  r) ; 
        setUserValue(prev => prev = 0) ; 
    }
    //3. OnChange event
    const changeHandler = (event:React.ChangeEvent<HTMLSelectElement>)=>{
        let value:string = event.currentTarget.value ; 
        if(value === null)return ; 
        setWeight(prev => prev = value  ) ; 
    }

    const changeHandler2 = (event:React.ChangeEvent<HTMLSelectElement>)=>{
        let value:string = event.currentTarget.value ; 
        if(value === null)return ; 
        setResult(prev => prev = value  ) ; 
    }

    const userHandler = (event:React.ChangeEvent<HTMLInputElement>)=>{
        let value:string = event.currentTarget.value ; 

        if(value === null || isNaN(Number(value)))return ; 
        setUserValue(prev => prev = Number(value)) ; 
    }
    //4. OnClick event
    const resetValues = (event:React.MouseEvent<HTMLButtonElement> )=>{
        setUserValue(prev => prev = 0) ; 
        setValue(prev => prev = 0) ; 
        setWeight(prev => prev = "g"); 
        setResult(prev => prev = "kg")


        
    }

    return (
        <section>

            <section className="content" >
                     <span > <h1>Converter Proyect</h1> </span>
            </section>
            
            <section className="content" >
                <form onSubmit={sumbitHandler} className='Box' >

                    <div className='Sub-Box'>
                        <Input id="user-Value" labelName={weight} onChange={userHandler} value={userValue} type={ 'number'}/>
                        <Input disabled={true} value={value} labelName={result} type={ 'number'}/>
                    </div>


                    <div className='Sub-Box'>
                        <ComboBox value={weight} onChange={changeHandler} options={listWeights} />
                        <Button type="submit" withStyle={false} text='Convert' command={()=>undefined} />
                        <Button type="reset" withStyle={false} text='Reset' command={resetValues} />
                        <ComboBox value={result} onChange={changeHandler2} options={listWeights} />
                    </div>

                    <div className='Sub-Box'>
                        <Toggle head='my togle' Content={<p>if you not even relize how hard is to learn ts,thml, and css. well it is pretty easy actually but one is the dumg</p>} />
                        <DivToggle head='names' Content={<List values={["Hersy","Craice","Ashyle"]} />}/>
                    </div>

                    

                   
                </form>

            </section>
            
        </section >
    )
}