//RANGE ----------------------------------------------------------->ARRAY
const range =(end=0,start=0)=>{
    let numbers = [];
    if (start > 0){
        let temp = start; 
        start = end; 
        end = temp ; 
    }

    for (let index = start; index <= end;index++){
        numbers.push(index);
    }

    return numbers;
};

//UNDEFINED ----------------------------------------------------------->BOOL
function isUndefined(value){
    return value ===undefined ;
}
//UNDEFINED ----------------------------------------------------------->BOOL
const type = (value) =>typeof value; 


//CONDITIONS -------------------------------------------------->ARRAY[BOOL]
function Conditions(iterable,conditionFn=null){
        if (conditionFn === null ) {
        const defaultFunction = (element)=>{
            return new Boolean(element).valueOf();
        }
        conditionFn = defaultFunction; 
    }
    
    let search = iterable.map(conditionFn);
    return search ; 
}

//ALL ----------------------------------------------------------->BOOL
function all(iterable,conditionFn=null){
    return !Conditions(iterable,conditionFn).includes(false);
}

//ANY ----------------------------------------------------------->BOOL
function any(iterable,conditionFn=null){
    return Conditions(iterable,conditionFn).includes(true);
}
//ZIP ------------------------------------------------>ARRAY[ARRAY[ANY,ANY]]
//output: [[1,1],[2,2],[3,3]]
const zip = (iterable,iterable2,iterables)=>{
    let zipArray = [];
    let minNumber = Math.min(iterable.length, iterable2.length) -1 ;
    for (let index = 0; index <= minNumber;index++){
        let firtsElement = iterable[index]; 
        let secondElement = iterable2[index]; 

        zipArray.push([firtsElement,secondElement]);

    }
    return zipArray;
}

//ENUMERATE ------------------------------------>ARRAY[ARRAY[NUMBER,ANY]]
const enumerate = (iterable,start=0)=>{
    let result = []; 
    let end = start + iterable.length -1 ;
    for (const [number,value] of zip(range(start,end),iterable)){
        result.push([number,value])
    }

    return result ; 
}
//PRINT ----------------------------------------------------------->VOID
const print = (...value)=>console.log(...value);

//RANDOM ------------------------------------------------------> NUMBER
const random = (min=0,max=100)=>Math.floor( Math.random() * (max - min +1) + min ); 

//ISINSTANCE ------------------------------------------------------> BOOL
const isinstance = (value,object ) =>{
    let element = Object.prototype.toString.call(value);
    let element2 = Object.prototype.toString.call(new object);
    return element === element2; 

}

//<-------------- TESTING THE FUNCTIONS ALL HAND --------------------------->
let nums = [10,0,1, 9,2,8,3,7,4,5,6,undefined]; 
const days = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"];
let names = ["Craice","Miseru","Ashely","Stephany","Darwin"];
let ranNumbs = []; 
let ndict = {
    name:"Hersy",
    age:18
};
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

for (let i in range(10)){
    ranNumbs.push(random(0,100));
}
print(ranNumbs);

//let mran = range(10);
//let mran2 = range(2,10);
//console.log(mran,mran2);

//console.log(nums );
//for (let i of range(10)){
//    print(i);
//}

//for (let [index,value] of enumerate(nums)){
 //   print(index,"--->", value);
//}
print(all(nums,isUndefined));
print(any(nums,isUndefined));
print(isinstance(2,Number));
print(type(myMap).name);
//print(myMap.get("str"));
//print(new Array (myMap.values()));

//for (let [index,[a,b]] of enumerate( zip(days,names),10)){
//print(index, a,b);
//}//

//for (let z of enumerate(days,5)){
//    print(z);
//}//