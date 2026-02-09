import print from "./myjs/utils.js";
import { zip, enumerate, all, any, assert, binary } from "./myjs/utils.js";
//<-------------- TESTING THE FUNCTIONS ALL HAND --------------------------->
let nums = [10, 0, 1, 9, 2, 8, 3, 7, 4, 5, 6, 0];
const days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];
let names = ["Craice", "Miseru", "Ashely", "Stephany", "Darwin"];
let ranNumbs = [];
let ndict = {
    name: "Hersy",
    age: 18
};
const info = {
    dict: { a: "this is a dict", b: "it is quite simple" },
    str: "001 this is a string-object!. you can:1. write number 123;2. you can write symbols !?#$ ;3. you can write spaces      . 4. This is pretty much it",
    int: 10,
    float: 10.50,
    array: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    n: null,
    und: undefined,
    boolean: true,
    func: function sum(a, b = -1) { if (a >= 100) {
        return b;
    } return a + b; },
    arrow: (x, y) => x + y,
};
const myMap = new Map();
for (let key in info) {
    let element = info[key];
    myMap.set(String(key), element);
}
for (const [a, b] of zip(days, names)) {
    print(a, "----->", b);
}
for (const [i, v] of enumerate(names)) {
    print(i, v);
}
let values = names.concat(days);
print(myMap);
try {
    assert(all(nums), "There at least one falsy value here...");
    print("Everything is ok");
}
catch (error) {
    print("error", error.message);
}
let result = binary(values, "Miseru");
print(result);
print(result.array);
print(info.arrow(10));
print("This is pretty much it. I guess so... ");
//This is my summary of the thing i did today 04/10/2025
/**
 * function quickSort(array:any[], start:number=0, end:number |null=null ):any[]{

end = end ===null ? array.length -1: end ;


if (start < end )
{

let index =  split(array,start,end);

quickSort(array,start, index -1);

quickSort(array,index +1 , end);

return array;
}
return array;
}

//BYNARY
function search(array:any[],target:any,start:number=0,end:number|null=null):number{
    end = end ===null ? array.length -1: end ;

    while ( start <= end){
        let mid = Math.floor( (start+end) /2 );


        let element = array[mid];
        if (element === undefined){break;}
        if(element === target){return mid}
        else if(element < target){start = mid +1  }
        else {end = mid -1 };

    }


    return -1;
}
//COUNT -------------------------------------------------------- number
function count(array:any[],value:any):number{
    let result  = array.filter((element)=>element ===value);
    return result.length;
    
};
interface BiObject{
    index:number,
    array:any[],
    target:any,
    amount:number,
    ok: boolean,
    time:string
};

type BinaryObject={
    index:number,
    array:any[],
    target:any,
    amount:number,
    ok: boolean,
    time:string
} ;


type Prettify<T> = {
    [K in keyof T]: T[K];
} &{};

binary([1,2],9)


function binary(array:any[],target:any,start=0,end=null):Prettify<BinaryObject>{
    let before:number = performance.now();
    //console.log(before);
    let sortedArray:any[] = quickSort(array);
    let result: number = search(sortedArray,target,start,end);
    let found:boolean = result !== -1 ;
    let amount:number = count(sortedArray,target);
     let after:number = performance.now();
    //console.log(after);
    let finish:number = after - before ;

    return {
        index:result,
        array:sortedArray,
        target:target,
        amount:amount,
        ok: found,
        time:finish.toFixed(4)
    };

}
 */ 
//# sourceMappingURL=1.js.map