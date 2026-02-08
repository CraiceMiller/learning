function swap ( arr, leftIndex=0, rightIndex=null){ 

if (rightIndex ===null){rightIndex = arr.length -1;}
/**
if (leftIndex >= rightIndex){throw new Error("Please select a valid input. The left parameter MUST to be less then the right parameter in order to do a flawless operation..." )  }*/


[arr[leftIndex], arr[rightIndex]] =[arr[rightIndex], arr[leftIndex]] ; 
}

function sort (array){


let mid = Math.trunc(array.length / 2 ) -1;
let left = array.splice(0,mid);
let right= array.splice(mid,-1);

if (array.length <= 1){return left.concat(right) ; }
swap(right,0, right.length);
swap(left,0, left.length);
sort(left);
sort(right);
}




function bynary(array, target,start = 0, end = null)
{
if (end ===null){end = array.length -1;}
while (start <= end)
{

let mid = Math.trunc(array.length / 2 ) -1; 

if (array[mid] === target){return mid}
else if (array[mid] <= target){ start = mid + 1}
else{end = mid -1 }


}

return -1
}



let nums = [10,0,1, 9,2,8,3,7,4,5,6 ]; 
let n = [1,2,3,4,5,6,7,8,9,10]

//sort(nums) 
console.log(bynary(n,9))





