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

// _________________________________________________________________________________

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
// _________________________________________________________________________________

export const nxor = (value1, value2) =>{
    return not(xor(value1, value2))
}
// _________________________________________________________________________________

export const isinstance= (value,object)=>{
    return typeof value === object
};
// _________________________________________________________________________________

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
// _________________________________________________________________________________

/**
 * @description this function will fech basic data based on the url provided. if a probelm occured it will return 
 * undefined.... it return the a json object (or a dict in order to understand it better off). 
 * @remember dicts are key-value pairs. Meaning it will have a key and the value based on the key 
 * for instance: 
 *  -"name": "hesry"
 * 
 * @NOTE    PLEASE DON'T FORGET TO USE THE KEYWORD "await"  IN ORDER TO RECIVED THE DATA IN A VERY 
 * PRECICE WAY. OTHERWISE IT WILL RETURN A PRIMISE OBJECT INSTEAD OF THE WANTED VALUE 
 * 
 * @param {string} url this is a url string where you wanna get the value
 * @returns {Promise | undefined}
 */

export async function fetchData(url){
    try{

    const response = await fetch(url);
    if (!response.ok){
        throw new ReferenceError("Could no fetch the resource...")}

    const data = await response.json(); 
    return data;

    }catch(e){
        console.log(e);
        return undefined;
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

export function assert(reason, message=null){
	if(reason){
	return ;
	}

	throw new Error(message ? message:"You have provide a non valid value");
};



// _________________________________________________________________________________


export function assertTypeof(value, type, message){
	if (value instanceof type){
		return ;
	}
	

	throw new Error(message || `Value ${value} is not instance of ${type.name || typeof type}`)

};


// _________________________________________________________________________________


export function callable(callbackfn = null,...value){
	if (callbackfn ===null){
		return value ;
	}
	const result = callbackfn(...value);
	if (result !== undefined || result ){
		return result;
	}
}



// _________________________________________________________________________________

export const arrange = (value,callbackfn = null ) => {
	const upper = (str) =>{ return str.trim().charAt(0).toUpperCase() + str.trim().slice(1).toLowerCase();}

	let match = value.match(/\S+/g);
	if (match.length > 1 ){
		let value =  match.map(upper);
		return callable(callbackfn, value.join(" ") );
	}

	return callable(callbackfn,upper(value))

}

// _________________________________________________________________________________

/**
 * @description This function only return the a string of only the symbols whithin the  provided string 
 * 
 * @param {String} string 
 * @returns {String[]}
 */
export const onlySymbols = (string ) => {
    let arr = string.match(/\W+/g);
    arr.forEach((value,index)=>arr[index] = value.trim() )
    arr = arr.filter ( (value) => value !== "" )
    
    return arr;
}

// _________________________________________________________________________________
/**
 * @description This function only return the a string of only the numbers whithin the  provided string 
 * 
 * @param {String} string 
 * @returns {String[]}
 */
export const onlyNumbers = (string) => {
    let arr = string.match(/\d+/g);
    arr.forEach((value,index)=>arr[index] = value.trim() )
    arr = arr.filter ( (value) => value !== "" )
    return arr;
}
 
// _________________________________________________________________________________
/**
 * @description This function only return the a string of only the word whithin the  provided string in an array.
 * Without numbers
 * 
 * @param {String} string 
 * @returns {String[]}
 */
export const onlyWords = (string) => {
    let arr = string.match(/\w+/g);
    arr.forEach((value,index)=>arr[index] = value.trim() )
    arr = arr.filter ( (value) => value !== "" && isNaN(value) )
    return arr;
}



// _________________________________________________________________________________





// _________________________________________________________________________________





// _________________________________________________________________________________





// _________________________________________________________________________________




// _________________________________________________________________________________





// _________________________________________________________________________________




// _________________________________________________________________________________



// _________________________________________________________________________________
