/**This funtion only greet the user*/
function greet(array){ 
    for (let index = 0; index < array.length; index++) {
        const element = array[index];
        console.log();
        console.log(`Hello ${element}, nice to meet you :)`)
    };
};

/**This is my own attempt of doing binary search. 
    
    Description: 
        This will give us only the index of the target value, return -1 if the value does
        not exist or occurs a problem.
        To make this funtiob more optimized, you need to give it a sorted list already
    Return: 
        the index of the target at hand as a interget, -1 otherwise

    Parameters: 
        @param iterable: this is the iterable to follow through
        @param target:this is the value you want to know the index

    Example: 
    >>> mybinary([1,2,3,4,5],3)
        output: 2 */
function mybinary(iterable,target){
    let start= 0;
    let end = iterable.length;
    
    while (start <= end) {
        let mid= Math.trunc((start + end)/2);

        if (iterable[mid]==target){return mid};

        if (iterable[mid]<target){start=mid + 1}
        else { end=mid-1};
    };

    return -1
};



const myarray = ["Hersy","Craice","Ashley","Miseru"];
const numbers= [1,2,3,,4,5,6,7,8,9,10];

greet(myarray)

for (const key in myarray) {
    if (Object.hasOwnProperty.call(myarray, key)) {
        const element = myarray[key];
        console.log("Hello " + element );
    };
};

myarray.forEach(element => {
    console.log("Nice to meet you "+element)
    
});


let result = mybinary(numbers,9);
if (result != -1){
    console.log(`The value was found in the index ${result}`)
}
else{
    console.log("The target was not found")
};
