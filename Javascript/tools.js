//tools.js
/**
 A simple function from python.
 * Prints the values to a stream
 *@param {any} value
 *@returns {void}
*/
export const print = (...value) =>{
    if (typeof value === "undefined"){
        console.log("");
        return ;
    }
    console.log(...value);
};

export const not = (value1) => {
    return !value1 
};

export const and= (value1, value2)=>{
    return value1 && value2
};

export const or = (value1, value2)=>{
    return value1 || value2
};

export const nor=(value1, value2) =>{
    return not(or(value1,value2))
}

export const nand = (value1, value2) =>{
    return not(and(value1,value2))
}

export const xor = (value1, value2) =>{
    return value1 != value2
}

export const nxor = (value1, value2) =>{
    return not(xor(value1, value2))
}

export const isinstance= (value,object)=>{
    return typeof value === object
};

/**This is my own attempt of doing binary search. 
    
Description: 
    This will give us only the index of the target value, return -1 if the value does
    not exist or occurs a problem.
    To make this funtiob more optimized, you need to give it a sorted list already


Parameters: 
    *@param {Array} iterable this is the iterable to follow through
    *@param {any} target this is the value you want to know the index
    *@returns {number} the index of the target at hand as a interget, -1 otherwise

Example: 
>>> mybinary([1,2,3,4,5],3);
    output: 2 */
export  function mybinary(iterable,target){
    let start= 0;
    let end = iterable.length -1;

    while (start <= end) {
        let mid= Math.trunc((start + end)/2);

        if (iterable[mid]===target){return mid};

        if (iterable[mid]<target){start=mid + 1}
        else { end=mid-1};
    };

    return -1
};


/**
 * @description This funtion only get the username as a string and return it into an arrange sring 
 * @param {string} username 
 * @returns {string}
 * @example 
 * >>> console.log(arrangeUserName("    mISERU sEMPAI    ") )
 * //Output: Miseru Sempai 
 */
export function arrangeUserName(username){
    let result = "";
    let arrange = (str) =>{return str.trim().charAt(0).toUpperCase()+ str.trim().slice(1,).toLowerCase()};

    if (username.includes(" ")){
        username= username.trim();
        let allMassage = username.split(" ");
        let result = allMassage.map(arrange);
        return result.join(" ");
    }

    return arrange(username);
};
