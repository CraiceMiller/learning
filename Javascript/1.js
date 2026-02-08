import { print,not,and,or,nor,nand,xor,nxor,isinstance,mybinary  } from "./tools.js";

let str="hello";
let int=10;
let float=5.75;
let bool=true;
let list=[1,2,3,4,5];
let dict={name:"ashley",age:18};
let None=null;
let unde=undefined;
const myarray = ["Hersy","Craice","Ashley","Miseru"];

myarray.sort();
print(myarray)



print("Hello world");
print(not(bool));
print(and(true,true));
print();
print(or(true,false));
print("bye world");
print(nor(false,false));
print();
print(nand(false,false));
print(xor(false,true));
print(nxor(false,false));
print();
print();
print(list[2]);
print(dict.name);
print(list.length);
print(str.endsWith("o"));
print(str.toUpperCase());
print(str.toLocaleUpperCase());
print(str.toString());
print(str.search("o"));
print(list);
print();

not(isinstance(str,"number")) ? print("It must be a number"):print("indeed it is a number");

let mylist=[2,5,1,3,4,6];
mylist.sort((a,b)=>a-b)

let index=mybinary(mylist,2);
index !=-1 ? print(`The index was found in ${index}`):print("The index was not found");


/**
 * 
 * @param {*} name 
 * @returns {number}
 */
function greet(name) {

    return `Hello ${name}`

    
}

