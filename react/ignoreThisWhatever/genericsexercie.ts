interface Item<T> {
    /**This only greet the user.. */
    greet(name?:string):void;
    /**This will only get the the value of an object */
    getProperty<Type,Key extends keyof Type>(obj:Type,key:Key):any;
    /**This one will only get the length of an object */
    getLength<Type extends {length:number}>(arg:Type):number; 


}
// TODO: create a class that that can handle every exerice i came accross...
class Solution<T = any> implements Item<T>{
    public className = "soluction"; 
    today:string = "19/10/2025"; 

    greet(name?: string ): void {
        console.log(`Hello ${name|| "user"}, nice to meet you `); 
    }

    getProperty<Type, Key extends keyof Type>(obj: Type, key: Key) {
        return obj[key]
    }

    getLength<Type extends { length: number; }>(arg: Type): number {
        return arg.length ; 
    }

    indentity<Type>(arg:Type):Type{
        return arg
    }




}

function createSoluction<A extends Solution>(c:new ()=>A):A{
    return new c(); 
}

interface DetectGeneric<Type>{
    (arg:Type):Type
}

type Prettify<Value>={
    [Key in keyof Value]: Value[Key]
} & {}

const solution:Solution = createSoluction(Solution) ; 
let names:string[] = ["Hersy","Craice","Ashley","Miseru"]; 
names.forEach(value=>solution.greet(value) ) ; 
console.log("className: ",solution.className) ; 
console.log("getProperty ", solution.getProperty(names,2)); 
console.log("getLength ", solution.getLength<string>(names[0]) ); 
console.log("names.keys(): ", names.keys())
console.log("solution" , solution); 

let s:DetectGeneric<string> = solution.indentity ; 
s.bind(s); 
console.log("s: ", s); 

import type {User} from "../utils/typing"; 
const user1:Prettify<User> = {
    age:19, 
    name:"Craice", 
    info:{
        country:"Altisora"
    }
}
user1
console.log(user1); 

for (let i : number =  0; i <= names.length ; i++){
    if(i===2){
        continue
    }
    console.log(names[i] )
} ; 

class _Node<T = any > {
    public data; public prev; public next ; 
    constructor(data:T,previous:_Node<T>,next:_Node<T>){
        this.data = data ;
        this.prev = previous; 
        this.next = next ;  
    }
}



class LinkedList<V = any>{
    private size:number ; 
    private head?:V[]; 
    private tail?:V[];
    


    constructor(data:V[]){
        this.size = 0; 
        this.head = undefined; 
        this.tail = undefined; 
    }



}


const Thisfn = <T>(v:T):T[]=>{
    return [v]
}
interface A<B extends {length:number} = string> {
    name?:string, 
    info:B
}
const C:A<number[]>= {
    name:"Ashley", 
    info:[123]
}

console.log(Thisfn("Craice"))
console.log(C)



