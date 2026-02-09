function greet0(name:string|undefined= undefined):void{
    console.log(`Hello ${name || "user"}, nice to meet you.`)
    console.log("I am a normal function")
    console.log("syntax: ");
    console.log("function greet0(name:string|undefined= undefined):void")

}

interface  greet1{
    name?:string,
    I_AM_AN_INTERFACE:string
    SYNTAX_interface_greet1:string


}

declare function greet2(name:string|undefined= undefined):void{
    console.log(`Hello ${name || "user"}, nice to meet you.`)
    console.log("I am a declare function")
    console.log("syntax: ");
    console.log(" declare function greet2() ")

}

/** 
debugger function greet3(){

}

type function greet4(){

}*/

export default function greet5(name:string|undefined=undefined):void{
    console.log(`Hello ${name || "user"}, nice to meet you.`)
    console.log("I am an expoert DEFAULT function")
    console.log("syntax: ");
    console.log("export default function greet5(name:string|undefined=undefined):void")

}

async function greet6(name:string|undefined=undefined):Promise<void>{
    console.log(`Hello ${name || "user"}, nice to meet you.`)
    console.log("I am an async function")
    console.log("syntax: ");
    console.log("async function greet6(name:string|undefined=undefined):Promise<void>")
    
}
 
export function greet7(name:string|undefined=undefined):void{
    console.log(`Hello ${name || "user"}, nice to meet you.`)
    console.log("I am an exported function")
    console.log("syntax: ");
    console.log(" export function greet7(name:string|undefined=undefined):void")
    

}

//import function greet8(){

//}

const value:greet1 = {
    name:"hersy", 
    I_AM_AN_INTERFACE:"now i am part of a delete statement", 
    SYNTAX_interface_greet1: "this syntax: delete value.name"
}

delete value.name


class greet10 implements greet1{
    public name:string|undefined; 
    public I_AM_AN_INTERFACE:string; 
    public SYNTAX_interface_greet1: string; 

    constructor(name:string|undefined){
        this.name = name
        this.SYNTAX_interface_greet1 = "Now is this syntax:class greet10 implements greet1 "
    }
}


class greet11 extends greet10 {
    readonly taxRate:number; 
    public info:string ; 
    constructor(r,name:string|undefined){
        super(name)
        this.info = "Hello, i am a class extend; syntax :class greet11 extends greet10  "
        this.taxRate = r ; 
    }

    private greet12():void{
        console.log(` Hello ${this.name || "user"}, nice to meet you.`)
        console.log("I am an private function (method). i can only be use within my class")
        console.log("syntax: ");
        console.log(" private greet12():void  ")

    }
    
    public greet13():void{
        this.greet12()
        //this.taxRate = 100 ; 
        console.log(` Hello ${this.name || "user"}, nice to meet you.`)
        console.log("I am an public function (method). i can be use everywhere")
        console.log("syntax: ");
        console.log("public greet13():void  ")
    
    }

}

const something = new greet11(10,"Hersy")
something.greet13()
//something.taxRate = 20 ; 


enum People {
    Craice= 1,
    Hersy=3, 
    Ashely=10

}

type User ={
    readonly id:number, 
    name:string, 
    country?:string 
}

function greet14(people:People):void{
    if (people === People.Craice){
        console.log("What'up craice, whatcha doing today...");
        return 
    }
    console.log(`Hello ${people}`);  
}

greet14(People.Ashely)

type StatNames = 'HP' | 'STR' | 'MAG';

type Config = {
    [key in StatNames]?: number; 
};

const defaultStats = {
    HP: 50,
    STR: 15,
    MAG:20, 
    DEX: 10, 
} satisfies Config; 

function getStat(statName: keyof typeof defaultStats) {
   
    return defaultStats[statName];
}

console.log(getStat("DEX")); 

/** 
readonly function greet16(){
    
}



satisfies function greet17(){

}

*/


type greet18 = {
    name:string, 
    I_AM_A_TYPE:string, 
    SYNTAX_tye_greet18:string, 

}




