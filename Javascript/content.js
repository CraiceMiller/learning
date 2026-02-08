import { print } from "./tools.js";

//1.variabes
const NAME="Ashely";                        //string
let age=15;                                 // int and float
let isStudent=true;                          //bool
let friends=["Hersy","Craice","Miseru","Stephany"] //arrays
let morInfo={
    country:"Altisora",
    languages:["english","spanish"]         //dictiornaries or hash(i dunno)
}

//2. funtions
const add = (a,b)=> a + b;                   // a lambda funtion. lambda a,b: a+ b
function isAdult(age){                       //normal funtion
    return age >= 18
}; 
function greet(name){
    let text="Hello, Nice to meet you "; 
    if (name){
        console.log(text + name)
    }else{
        console.log(text + "!")
    }
}

//const print=(any)=>console.log(any);

//3.if statment
if (NAME==="Hersy") {
    console.log("Get out of here Hersy, we dont wanna troblues here") //  a normal if 
} else {
    console.log(`Hello ${NAME} how are you :3`)
    
}

isAdult(age) ? console.log("You are an adult"): console.log("you are not an adult"); //ternaria if

let result = add(10,5);
result <=20 ? print("It is a nice number"):print("Too large!");
//print("It is a nice number") if result <= 20 else print("Too large!")

//3.for statment
let numfriend =0;
for (let index = 0; index < friends.length; index++) {         //for based in index
    numfriend += index;
    const element = friends[index];
    greet(element);
    
};

for (const name of friends) {                               //the noraml for
    if (name=="Miseru"){
        break
    }
    print(name)
};
print("-----------");
for (const key in morInfo) {                                //for using in hash
    if (Object.hasOwnProperty.call(morInfo, key)) {
        const element = morInfo[key];
        print(element)
    }
};
print("-----------");

print(`Num of friend: ${numfriend}`),
greet();
//4. while statment
let num=0;
while (num<=5) {                  //the normal while
    print(num);
    num +=1
};
print("Hello world")
/* i dunno what this does 
do {
    
} while (condition);*/

//5. classes
/* 
__init__
instances variables 
class variables
properties

static methods
methods
class methods

*/
//1 class
/**This only create a object of a basic peson */
class Person{
    //4.1 first set the private instance
    #age;
    #isAlive;
    //2 class methods
    static species = "Homo sapiens";

    //3 __init__ 
    /**
     * @param {*} name : this is the name of the peson;
     *@param {*} age : this is the age of the person;
     */
    constructor(name,age){
        //4 isntance variables, public
        this._name=name;
        //5 private instance
        this.#age=age;
        this.#isAlive=true;
    }

    //6 static methods
    static add(a,b){
        return a + b
    }

    #isAdult(){
        if (this.#age <= 18){
            return "I am not an adult"
        }else{
            return "I am an adult"
        }
    }

    //7. methods
    presentation(){
        if (!this.#isAlive){
            print("A misterious voice said: 'this person is dead' ")
            return false
        }

        print(`Hello I am ${this._name}, Nice to meet you and `+this.#isAdult());
        return true
    }

    hangout(){
        if (!this.#isAlive){
            print("A misterious voice said: 'this person is dead' ")
        }

        if (!this.#isAdult()){
            print("Sorry dude, but I can hang out with you , due i am not an adult yet")
        }
        print("Ok let's go")
    }

    


    //8 properties
    get name(){return this._name}

    set name(value){
        if (typeof value !== "string"){
            print("You can do that, only string values..")
            return 
        }
        this._name = value
    }

    get age(){
        return this.#age
    }

    set age(value){
        if (typeof value !== "number"){
            print("You can do that, only interger values..")
            return 
        }
        print(`the value ${this.#age} change to ${value}`)
        this.#age = value
    }

    get alive(){
        return this.#isAlive;
    }

    set alive(value){
        if (typeof value !== "boolean"){
            print("You can do that, only boolean values..")
            return 
        }

        this.#isAlive=value
    }



}

const ASHELY =  new Person(NAME,age);
ASHELY.alive = true;
ASHELY.presentation();
print(ASHELY.age);
print(ASHELY._name);
ASHELY.age = 20;
print(ASHELY.age);
ASHELY.hangout();
ASHELY.name = false;
ASHELY.name = "false";
print(ASHELY.name);
print(ASHELY.species);
print(Person.species);


