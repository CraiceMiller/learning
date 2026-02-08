// QUICK-SORT

//0. 
/**
[10,0,1, 9,2,8,3,7,4,5,6 ], 0, 2 */
function swap ( arr, leftIndex=0, rightIndex=null)
{ 

if (rightIndex ===null){rightIndex = arr.length -1;}

/**
if (leftIndex >= rightIndex){throw new Error("Please select a valid input. The left parameter MUST to be less then the right parameter in order to do a flawless operation..." )  }*/

/**
[1,0,10, 9,2,8,3,7,4,5,6 ]*/
[arr[leftIndex], arr[rightIndex]] =[arr[rightIndex], arr[leftIndex]] ;
 
}


//1.
/**
[10,0,1, 9,2,8,3,7,4,5,6 ], 0, 10 */
function split(array, lowIndex=1, highIndex=null)
{
if (highIndex ===null)
{
highIndex = array.length -1;
}

//2.
let pivot = array[highIndex]; // pivot = 6 

//3.
let index = lowIndex ;// index = 0

//4.				1 < 10
for (let indexElement = lowIndex; indexElement < highIndex ; indexElement++)// 01
{

//5. 0 < 6
if(array[indexElement ] < pivot ){
indexElement++; // = 2

//6.	
/**
[10,0,1, 9,2,8,3,7,4,5,6 ], 0, 2 */
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

if (start > end )
{ 
return array ;
}

/**
[10,0,1, 9,2,8,3,7,4,5,6 ], 0, 10 */
let pi =  split(array,start,end);

quickSort(array,start, pi -1);

quickSort(array,pi +1 , end);

return array;
}

let nums = [10,0,1, 9,2,8,3,7,4,5,6 ]; 
swap(nums)
//console.log(quickSort(nums) ); 
console.log(nums )

