//QUICKSORT
function swap( arr:any[], leftIndex:number=0, rightIndex:number|null=null):void
{ 
    if (arr.length <= 2 || arr === undefined){return }

    
    let right = rightIndex ===null ? arr.length -1:rightIndex;
    
    if (leftIndex < 0 || right >= arr.length || leftIndex >= right) {
        return; 
    }
    
    const temp= arr[leftIndex];
    arr[leftIndex] = arr[right] ;
    arr[right] = temp ; 
 
}



function split(array:any[], lowIndex:number=1, highIndex:number|null=null):number
{
if (highIndex ===null)
{
highIndex = array.length -1;
}

//2.
let pivot = array[highIndex]; // pivot = 6 

//3.
let index = lowIndex -1;// index = 0

//4.				1 < 10
for (let indexElement = lowIndex; indexElement < highIndex ; indexElement++)// 01
{

let currentValue = array[indexElement ]; 

if( currentValue === undefined || pivot === undefined){return index + 1; }
//5. 0 < 6
if(currentValue < pivot ){
index++; // = 2

swap(array, index, indexElement);
}
}

//7.
swap(array, index + 1, highIndex) ;

//8.
return index + 1;
}


/**
 * Sorts an array in-place using the Quicksort algorithm.
 * * This is a highly efficient, comparison-based sorting algorithm with an average
 * time complexity of O(n log n). The function mutates (changes) the original 
 * input array and returns a reference to it.
 * * @template Any The type of elements in the array (must be comparable, e.g., number, string).
 * @param array The array to be sorted. This array is modified directly.
 * @param start The starting index of the subarray to be sorted (inclusive). Defaults to 0.
 * @param end The ending index of the subarray to be sorted (inclusive). Defaults to the last index.
 * @returns A reference to the sorted input array.
 * * @example
 * const data = [10, 7, 8, 9, 1, 5];
 * quickSort(data); // Returns [1, 5, 7, 8, 9, 10]
 * * @throws {Error} If provided 'start' or 'end' indices are invalid.
 */

function quickSort<Any>(array:Any[], start:number=0, end:number |null=null ):Any[]{

end = end ===null ? array.length -1: end ; 

if (start < 0 || end >= array.length || start > end) {
    throw new Error("Invalid array indices provided to quickSort.");
}


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

/**This is my own attempt of doing binary search. 
    
Description: 
    This will give us only the index of the target value, return -1 if the value does
    not exist or occurs a problem.
    To make this funtiob more optimized, you need to give it a sorted list already


Parameters: 
    *@param {Array} array this is the array to follow through
    *@param {any} target this is the value you want to know the index
    *@returns {number} the index of the target at hand as a interget, -1 otherwise

*/

function binary<A>(array:A[],target:A,start=0,end=null):Prettify<BinaryObject>{
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


//(element, index, array); 
//RANGE ----------------------------------------------------------->ARRAY
const range =(end=0,start=0): number[]=>{
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



//PRINT ----------------------------------------------------------->VOID
export default function print(...value:any[]):void{
    if (value.length <= 0){
        console.log("");
        return ;
    }
    console.log(...value);
}

//RANDOM ------------------------------------------------------> NUMBER
const random = (min:number=0,max:number=100):number=>Math.floor( Math.random() * (max - min +1) + min );



//UNDEFINED ----------------------------------------------------------->BOOL
function isUndefined(value:any){
    return value ===undefined ;
}
//type ----------------------------------------------------------->BOOL
const type = (value:any) =>typeof value; 


//CONDITIONS -------------------------------------------------->ARRAY[BOOL]
function Conditions(array:any[],conditionFn:((element:any)=>boolean) | null = null):boolean[]{
    let func; 

    const defaultFunction = (element:any):boolean=>{
        return !!element;
    }

    if(!conditionFn){
        func = defaultFunction ;
    }else{
        func = conditionFn as (element: any) => boolean ; 
    }

    const result: boolean[] = array.map(func);

    return result ; 
}

//ALL ----------------------------------------------------------->BOOL
function all<A>(array:A[],conditionFn:((element:A)=>boolean) | null = null){
    return !Conditions(array,conditionFn).includes(false);
}

//ANY ----------------------------------------------------------->BOOL
function any<A>(array:A[],conditionFn:((element:any)=>boolean) | null = null){
    return Conditions(array,conditionFn).includes(true);
}
//ZIP ------------------------------------------------>ARRAY[ARRAY[ANY,ANY]]
//output: [[1,1],[2,2],[3,3]]
const zip = <Zip, Zip2>(array:Zip[],array2:Zip2[]):[Zip,Zip2][]=>{
    let zipArray:[Zip,Zip2][]= [];
    let minNumber = Math.min(array.length, array2.length) -1 ;
    for (let index = 0; index <= minNumber;index++){
        let firtsElement = array[index]; 
        let secondElement = array2[index]; 
        if (firtsElement === undefined || secondElement === undefined){break;}

        zipArray.push([firtsElement,secondElement]);

    }
    return zipArray;
}

//ENUMERATE ------------------------------------>ARRAY[ARRAY[NUMBER,ANY]]
const enumerate=<Any>(array:Any[],start:number=0):[number, Any][]=>{
    let result:[number, Any][] = []; 
    let end: number = start + array.length -1 ;
    let number: number;
    let value:any;

    for ([number,value] of zip(range(start,end),array)){
        result.push([number,value])
    }

    return result ; 
}
//PRINT ----------------------------------------------------------->VOID
//const print = (...value)=>console.log(...value);

//RANDOM ------------------------------------------------------> NUMBER
//const random = (min=0,max=100)=>Math.floor( Math.random() * (max - min +1) + min ); 

//sfg
export async function getData(url:string){
    try{

    const response = await fetch(url);
    if (!response.ok){
        throw new ReferenceError("Could no fetch the resource...")}

    const data = await response.json(); 
    return data;

    }catch(e){
        console.log(e);
        return undefined ;
    }
};

// _________________________________________________________________________________
/**
 * @description This funtion only see if the a work was valid or notl. if was not valid (meaning 
 * it was false) it will throw an erro. It will do nothing otherwise.
 * @param {Boolean} reason just a bolean to work 
 * @param {string} message A little text to pass in the error
 * @returns {void}
 */
export function assert(reason:boolean, message:string|null=null){
	if(reason){
	return ;
	}

	throw new Error(message ? message:"You have provide a non valid value");
};



// _________________________________________________________________________________

export function assertTypeof(value:any, type:any, message:string|undefined){
	if (value instanceof type){
		return ;
	}
	

	throw new Error(message || `Value ${value} is not instance of ${type.name || typeof type}`)

};


// _________________________________________________________________________________


export function callable(callbackfn:(element:any)=>any|null,...value:any[]){
	if (callbackfn ===null){
		return value ;
	}
	const result = callbackfn(value);
	if (result !== undefined || result ){
		return result;
	}
}



// _________________________________________________________________________________

export const arrange = (value:string,callbackfn:()=>any|undefined ):any => {
	const upper = (str:string) =>{ return str.trim().charAt(0).toUpperCase() + str.trim().slice(1).toLowerCase();}

	let match = value.match(/\S+/g);
    if (match === null){return null; }

	if (match.length > 1 ){
		let value =  match.map(upper);
		return callable(callbackfn, value.join(" ") );
	}

	return callable(callbackfn,upper(value))

}

// _________________________________________________________________________________



// _________________________________________________________________________________

export {
    quickSort,
    count,
    binary,
    range,
    random,
    isUndefined,
    type,
    all,
    any,
    zip,
    enumerate, 
    //isinstance
}

export type {Prettify}
