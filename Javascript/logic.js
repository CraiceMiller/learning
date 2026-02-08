//QUICKSORT
function swap ( arr, leftIndex=0, rightIndex=null)
{ 
    if (rightIndex ===null){rightIndex = arr.length -1;};
    
    let temp = arr[leftIndex];
    arr[leftIndex] = arr[rightIndex] ;
    arr[rightIndex] = temp ; 
 
}



function split(array, lowIndex=1, highIndex=null)
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

//5. 0 < 6
if(array[indexElement ] < pivot ){
index++; // = 2

swap(array, index, indexElement);
}
}

//7.
swap(array, index + 1, highIndex) ;

//8.
return index + 1;
}




function quickSort(array, start=0, end=null )
{ 
if (end ===null)
{
end = array.length -1; // 10
}

if (start < end )
{ 

let index =  split(array,start,end);

quickSort(array,start, index -1);

quickSort(array,index +1 , end);

return array;
}
}

//BYNARY
function search(array,target,start=0,end=null){
    if (end===null){
        end = array.length -1; 
    }

    while ( start < end){
        let mid = Math.floor( (start+end) /2 );
        let element = array[mid];
        if(element === target){return mid}
        else if(element < target){start = mid +1  }
        else {end = mid -1 }; 

    }


    return -1; 
}
//COUNT -------------------------------------------------------- number
function count(array,value){
    let result  = array.filter((element)=>element ===value);
    return result.length; 
    
}


function binary(array,target,start=0,end=null){
    let before = new Date().getSeconds();
    //console.log(before);
    let sortedArray = quickSort(array);
    let result = search(sortedArray,target,start,end);
    let found = result !== -1 ; 
    let amount = count(sortedArray,target);
     let after = new Date().getSeconds(); 
    //console.log(after);
    let finish = after - before ; 

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



//PRINT ----------------------------------------------------------->VOID
const print = (...value)=>console.log(...value);

//RANDOM ------------------------------------------------------> NUMBER
const random = (min=0,max=100)=>Math.floor( Math.random() * (max - min +1) + min ); 

//---------------------------TESTING ------------------------------------
let nums = [ ]; 
let nums2 = [1,1,2,3,4,5,6,8,9,10,1,2,3,4];
let randomTarget = 4;
for (let _ of range(14)){
    let number = random(0,20);
    nums.unshift(number);  
}

let result = binary(nums,randomTarget);
print(result);
print(count(nums2,1));

result.ok ? print("The value was found :)"):print("The value was not found :(");