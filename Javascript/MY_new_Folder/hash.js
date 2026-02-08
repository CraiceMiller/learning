//23/09/205 at 13:00-16:00
const print = (...value)=>console.log(...value);
const variable = {
dict: {a:"this is a dict", b:"it is quite simple"},
str: "001 this is a string-object!. you can:1. write number 123;2. you can write symbols !?#$ ;3. you can write spaces      . 4. This is pretty much it", 
int: 10, 
float:10.50, 
array:[1,2,3,4,5,6,7,8,9,10],
n:null,
und:undefined,
boolean:true,
func:function sum(a,b=-1){if(a >=100){return b}return a+b}, 
arrow:(x,y)=>x+y,

}
const myMap = new Map();

for (let key in variable){ 
myMap.set(String(key),variable[key]);

}

const keys = new Array(myMap.keys());
print(typeof keys);
print(keys);

console.log(myMap)
console.log(variable);

/**
myMap.forEach( 
(value,key)=>{ 
print(`This is a key "${key}": key is type of ${typeof key} `);
print(`and Its value is "${value}" : value is type of ${typeof value}`);
print();
}

)*/


print( 
myMap.get("str")
.trim()
.toLocaleLowerCase()
.fontsize(100)
.blink()
.bold()
.big()
.italics() 
.fontcolor("red") 
 )

//FUNCTION ----------------------------
const onlySymbols = (string ) => {
let arr = string.match(/\W+/g);
arr.forEach((value,index)=>arr[index] = value.trim() )
arr = arr.filter ( (value) => value !== "" )

return arr;
}

//FUNCTION ----------------------------
const onlyNumbers = (string) => {
let arr = string.match(/\d+/g);
arr.forEach((value,index)=>arr[index] = value.trim() )
arr = arr.filter ( (value) => value !== "" )
return arr;
}

//FUNCTION ----------------------------
const onlyWords = (string) => {
let arr = string.match(/\w+/g);
arr.forEach((value,index)=>arr[index] = value.trim() )
arr = arr.filter ( (value) => value !== "" && isNaN(value) )
return arr;
}

/**
let str = myMap.get("str"); 
let arr = str.match(/\W+/g);
arr.forEach((value,index)=>arr[index] = value.trim() )
arr = arr.filter ( (value) => value !== "" )
*/

let str = myMap.get("str")
print("-----"); 
print(onlyWords(str).sort()); 
print(onlyNumbers(str).sort((a,b)=>a-b) );
print(onlySymbols(str));
print(myMap.get("arrow")(10,10));
print(myMap.get("arrow")(10,10));
print(myMap.get("func")(10,50));
print(myMap.get("dict").a)
print(myMap.get("boolean").toString())
