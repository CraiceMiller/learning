//QUICKSORT
function swap(arr, leftIndex = 0, rightIndex = null) {
    if (arr.length <= 2 || arr === undefined) {
        return;
    }
    let right = rightIndex === null ? arr.length - 1 : rightIndex;
    if (leftIndex < 0 || right >= arr.length || leftIndex >= right) {
        return;
    }
    const temp = arr[leftIndex];
    arr[leftIndex] = arr[right];
    arr[right] = temp;
}
function split(array, lowIndex = 1, highIndex = null) {
    if (highIndex === null) {
        highIndex = array.length - 1;
    }
    //2.
    let pivot = array[highIndex]; // pivot = 6 
    //3.
    let index = lowIndex - 1; // index = 0
    //4.				1 < 10
    for (let indexElement = lowIndex; indexElement < highIndex; indexElement++) // 01
     {
        let currentValue = array[indexElement];
        if (currentValue === undefined || pivot === undefined) {
            return index + 1;
        }
        //5. 0 < 6
        if (currentValue < pivot) {
            index++; // = 2
            swap(array, index, indexElement);
        }
    }
    //7.
    swap(array, index + 1, highIndex);
    //8.
    return index + 1;
}
function quickSort(array, start = 0, end = null) {
    end = end === null ? array.length - 1 : end;
    if (start < end) {
        let index = split(array, start, end);
        quickSort(array, start, index - 1);
        quickSort(array, index + 1, end);
        return array;
    }
    return array;
}
//BYNARY
function search(array, target, start = 0, end = null) {
    end = end === null ? array.length - 1 : end;
    while (start <= end) {
        let mid = Math.floor((start + end) / 2);
        let element = array[mid];
        if (element === undefined) {
            break;
        }
        if (element === target) {
            return mid;
        }
        else if (element < target) {
            start = mid + 1;
        }
        else {
            end = mid - 1;
        }
        ;
    }
    return -1;
}
//COUNT -------------------------------------------------------- number
function count(array, value) {
    let result = array.filter((element) => element === value);
    return result.length;
}
;
;
binary([1, 2], 9);
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
function binary(array, target, start = 0, end = null) {
    let before = performance.now();
    //console.log(before);
    let sortedArray = quickSort(array);
    let result = search(sortedArray, target, start, end);
    let found = result !== -1;
    let amount = count(sortedArray, target);
    let after = performance.now();
    //console.log(after);
    let finish = after - before;
    return {
        index: result,
        array: sortedArray,
        target: target,
        amount: amount,
        ok: found,
        time: finish.toFixed(4)
    };
}
//(element, index, array); 
//RANGE ----------------------------------------------------------->ARRAY
const range = (end = 0, start = 0) => {
    let numbers = [];
    if (start > 0) {
        let temp = start;
        start = end;
        end = temp;
    }
    for (let index = start; index <= end; index++) {
        numbers.push(index);
    }
    return numbers;
};
//PRINT ----------------------------------------------------------->VOID
export default function print(...value) {
    if (value.length <= 0) {
        console.log("");
        return;
    }
    console.log(...value);
}
//RANDOM ------------------------------------------------------> NUMBER
const random = (min = 0, max = 100) => Math.floor(Math.random() * (max - min + 1) + min);
//UNDEFINED ----------------------------------------------------------->BOOL
function isUndefined(value) {
    return value === undefined;
}
//type ----------------------------------------------------------->BOOL
const type = (value) => typeof value;
//CONDITIONS -------------------------------------------------->ARRAY[BOOL]
function Conditions(array, conditionFn = null) {
    let func;
    const defaultFunction = (element) => {
        return !!element;
    };
    if (!conditionFn) {
        func = defaultFunction;
    }
    else {
        func = conditionFn;
    }
    const result = array.map(func);
    return result;
}
//ALL ----------------------------------------------------------->BOOL
function all(array, conditionFn = null) {
    return !Conditions(array, conditionFn).includes(false);
}
//ANY ----------------------------------------------------------->BOOL
function any(array, conditionFn = null) {
    return Conditions(array, conditionFn).includes(true);
}
//ZIP ------------------------------------------------>ARRAY[ARRAY[ANY,ANY]]
//output: [[1,1],[2,2],[3,3]]
const zip = (array, array2) => {
    let zipArray = [];
    let minNumber = Math.min(array.length, array2.length) - 1;
    for (let index = 0; index <= minNumber; index++) {
        let firtsElement = array[index];
        let secondElement = array2[index];
        if (firtsElement === undefined || secondElement === undefined) {
            break;
        }
        zipArray.push([firtsElement, secondElement]);
    }
    return zipArray;
};
//ENUMERATE ------------------------------------>ARRAY[ARRAY[NUMBER,ANY]]
const enumerate = (array, start = 0) => {
    let result = [];
    let end = start + array.length - 1;
    let number;
    let value;
    for ([number, value] of zip(range(start, end), array)) {
        result.push([number, value]);
    }
    return result;
};
//PRINT ----------------------------------------------------------->VOID
//const print = (...value)=>console.log(...value);
//RANDOM ------------------------------------------------------> NUMBER
//const random = (min=0,max=100)=>Math.floor( Math.random() * (max - min +1) + min ); 
//sfg
export async function getData(url) {
    try {
        const response = await fetch(url);
        if (!response.ok) {
            throw new ReferenceError("Could no fetch the resource...");
        }
        const data = await response.json();
        return data;
    }
    catch (e) {
        console.log(e);
        return undefined;
    }
}
;
// _________________________________________________________________________________
/**
 * @description This funtion only see if the a work was valid or notl. if was not valid (meaning
 * it was false) it will throw an erro. It will do nothing otherwise.
 * @param {Boolean} reason just a bolean to work
 * @param {string} message A little text to pass in the error
 * @returns {void}
 */
export function assert(reason, message = null) {
    if (reason) {
        return;
    }
    throw new Error(message ? message : "You have provide a non valid value");
}
;
// _________________________________________________________________________________
export function assertTypeof(value, type, message) {
    if (value instanceof type) {
        return;
    }
    throw new Error(message || `Value ${value} is not instance of ${type.name || typeof type}`);
}
;
// _________________________________________________________________________________
export function callable(callbackfn, ...value) {
    if (callbackfn === null) {
        return value;
    }
    const result = callbackfn(value);
    if (result !== undefined || result) {
        return result;
    }
}
// _________________________________________________________________________________
export const arrange = (value, callbackfn) => {
    const upper = (str) => { return str.trim().charAt(0).toUpperCase() + str.trim().slice(1).toLowerCase(); };
    let match = value.match(/\S+/g);
    if (match === null) {
        return null;
    }
    if (match.length > 1) {
        let value = match.map(upper);
        return callable(callbackfn, value.join(" "));
    }
    return callable(callbackfn, upper(value));
};
// _________________________________________________________________________________
// _________________________________________________________________________________
export { quickSort, count, binary, range, random, isUndefined, type, all, any, zip, enumerate,
//isinstance
 };
//# sourceMappingURL=utils.js.map