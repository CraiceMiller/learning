// QUICK-SORT

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

let nums = [10,0,1, 9,2,8,3,7,4,5,6 ]; 
quickSort(nums)
//console.log(quickSort(nums) ); 
console.log(nums )