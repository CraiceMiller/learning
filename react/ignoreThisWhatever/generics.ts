function getArray(item:any):any{
    return [item]
}
function getArray2<Item>(item:Item):Item[] {
    return [item]
}

function doSomething<This,That>(value:This,value2:That):[This, That]{
    return [value, value2]
   
}


function anotherThing<ThisItem,ThatItem>(item:ThisItem[]):ThisItem[]{
    return item 
}

type Something<anotherSomethig = number > = {
    name: string, 
    age?:number, 
    info:anotherSomethig
}

type A<B > = {
    id:number, 
    info:B
}


type P<T> = {
    [A in  keyof  T]: T[A]
}

type C<D extends string > = {
    result: D
}



const fn = <T extends {length:number}>(value:T):number=>{
    return value.length
}

const fn2 = <Z extends Something<Z>>(value:Z)=>{
    return value.info
}

type ResponseData <D extends  Object = {succes:boolean}> = {
    status:number; 
    data:D

}





function test1():void{ 
    let defalultDATa:P<ResponseData> = {
        status:200,
        data:{succes:true}
    }
    
console.log(defalultDATa.data.succes.valueOf.name.toLocaleUpperCase());


let r4:P<Something>={
    name:"Craice", 
    info:123
}
let r5:Something<Something<boolean>> = {
    name:"School", 
    age:200, 
    info:{
        name:"Somehting", 
        info: false
    }
}

//let a1= fn2("Bye world"); 
let a2 = fn<string>("Something is going on here"); 
const {age,info } = r5 ; 
let a3:Something<boolean> = {
    name:"Miseru", 
    info:false
}
console.log(info, age)





class MyClass<thatItem>{
    private values:thatItem[]
    constructor(...value:thatItem[]){

        this.values=[...value]
    }

    myMetod<What>(callbackfn:(v:thatItem,index:number,array:thatItem[] )=>What,):What[]{
        let result:What[]= []; 

        for ( let i:number = 0 ; i < this.values.length ; i++){
            result.push(callbackfn(this.values[i],i,this.values))
        }

        return result ; 

    }

} 


let animes:string[]=["City-Animation","Nazo no Kanojo X","Danganronpa","No Game No Life"]; 
let numberLetter:number[] = animes.map<number>(value => value.length); 
console.log(animes);
console.log( numberLetter );
console.log( numberLetter[0].toFixed(2) );
let r1:number = getArray(12)
let r2:string[]= getArray2<string>("hello")
let r3 =doSomething("hello",999)

let r6 = new MyClass("City-Animation","Nazo no Kanojo X","Danganronpa","No Game No Life")
let r7:A<Something<string>> = { 
    info:{
        name:"Ashely", 
        age:19, 
        info:"She is a soft girl"
    } , 
    id:100

}








console.log(r1,r2,r3,r4,r5,r6); 
console.log(r6.myMetod(value => value.length));
console.log("City-Animation" in animes );
console.log(r7.info.info.includes("a"));
//console.log([x in keyof r7]);


}

import React from "react";
function test2():void{
    interface O<T> {
        /**This is just a map */
        map<U>(callbackfn: (value: T, index: number, array: T[]) => U): U[];
        /**This will only print the value in a console */
        display<T>():void;  
    
    }
    
    type I<T> = {
        map<U>(callbackfn: (value: T, index: number, array: T[]) => U): U[];
        display<U>():void;  
    
    }
    
    //WHY I GOT THIS ERROR: Class 'MyClass<thatItem>' incorrectly implements interface 'O<thatItem>'.
     // Property 'values' is private in type 'MyClass<thatItem>' but not in type 'O<thatItem>'
     //AND WHAT IS THE DIFFERENCE IF I IMPLEMENTS AN INTERFACE AND A TYPE ?
    class MyClass<thatItem> implements O<thatItem> {
        public values:thatItem[]
        constructor(...value:thatItem[]){
    
            this.values=[...value]
        }
    
        map<What>(callbackfn:(v:thatItem,index:number,array:thatItem[] )=>What,):What[]{
            let result:What[]= []; 
    
            for ( let i:number = 0 ; i < this.values.length ; i++){
                result.push(callbackfn(this.values[i],i,this.values))
            }
    
            return result ; 
    
        }
    
        display<ThatItem>(): void {
            for (const value of this.values){
                console.log(value)
            }
            
        }
    
    } 
    
      
    
    
    
    
    function getData<T = ResponseData>(data:T){
    
        return data
    }
    
    
    //I REALLY TRIED SO HARD TO UNDERSTAND WHAT THIS MEANS AND THE ONLY CONCLUSION I REACHED WAS 
    //THIS FUNCTION HANDLES AN EVENT, THIS IS A onChange EVENT (React.ChangeEvent) THAT ALSO HANDLES MY
    //INPUT HTML ELEMENT...
    interface ChangeEvent<T=Element> {
        target:T 
        //and the rest of the properties here...
    }
    //
     //interface ChangeEvent<T=HTMLInputElement> {
      //  target:{
      //  value:any
     // }
    //  
    //}
    const handler:(event:React.ChangeEvent<HTMLInputElement> )=>void= (event:React.ChangeEvent<HTMLInputElement> )=>{
    const a = event.target ; 
    console.log(a.value)
    }
    
    //AND I DONT GET IT , WHY SICNE THESE ONES (ChangeEvent, and my O<T>) ARE INTERFACES 
    //WHY I CANNOT DO THIS WITH MY OWN INTERFACE ?
    const f4 = <T>(value:O<T>):void=>{
        value.display()
    
    }
    
    const c:MyClass<number> = new  MyClass<number>(1,2,3,5); 
    console.log(c.map<string>( v =>{return v.toString()} )); 
    
    console.log( )
    //this  DOES NOT WORK 
    f4(c); 

    

}

function calculateArea(side:number):number; 
function calculateArea(width:number, height:number):number ;
function calculateArea(arg1:number,arg2?:number):number{
    if (arg2 === undefined){
        return arg1 * arg1
    }
    return arg1 * arg2
}
let result:number = calculateArea(10); 
console.log(result)
test2(); 


/**
 * GOAL: 
 *  learn how to use Generics in function,types and classes(objes)
 * 
 * STEPS: 
 * how can i use a single generic like <Item> in a function and a type : 
 *      just like any in python : 
 *         function fn<Any>(value:Any):Any{
 *              return value}
 *          console.log(fn<number>(123))
 * 
 * how the generic works in a type: 
 * we can use them in three types: 
 *      1. generic: a single value we want to change 
 *          when we need it 
 *             type Something<Any> = {
 *                  name:string, 
 *                  value:Any
                }

        2. default: this is the easy one. it work the same like 
                a default parameter in function: 
            function fun(name:string = "user"):void{console.log(name)}

            Likewise we can use anoter type like a default:
            type AnotherSomething<Any = number> = {
                country:string, 
                info:Any
            }

           

        3.extend: this works the same like we do in a class inherentence
        python: 
        class A:
            def doThis(self): 
                ...
            ...
        class B(A): 
            def doThat(self): 
                ...
            ...

        ts/js
        class A{
            doThis(){}
        }

        class B extends A{
            doThat(){}
        }

        what we are doing here is that class B has every Metod, property,
        so on, from A. so i can do this: 
            B.doThis() //doThis methos belongs to A

        using the same idea we can do the same using types: 
        type X = {
            color?:string, 
            height?:number, 
            isAlive?:boolean
        }

        type Y <Z extends X> = {
            language:string, 
            data:Z
        }

        const ThisSomething:Y = {
            language: "japanese", 
            data: {
                isAlive:true, 
                height:58.12
            }
        }

 * 
 * how can i use two generics in a funtion: 
        i still dont know :( 

 * how can i use them whenever i want: 
            is still dont know :( 
 * 
 *  ANALOGY: 
 *  A box that can be storage anything i want, whenever i need it, 
 * using the same template box
 * 
 * CONSLUCION: 
 * it is just a replace of Any, we explicity tell TypeScript 
 * what value we want to return
 * 
 */

                /**
                 * there are a lot of thing a person can dead intead of literatly die (the heart doesn't move). 
                 * for instance; a person also can die when is forgotten for everyone. 
                 * that's means if a person say: "you are going to die", that means every
                 * person who knwos you will die instead of you ....
                 */

                /**
                 * when you belive in a lie, that lie, it becomes in your reality...
                 */