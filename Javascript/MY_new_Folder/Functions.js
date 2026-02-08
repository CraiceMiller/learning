// _________________________________________________________________________________

function greet(name){

 	console.log(`Hello ${name} Nice to meet you `);

};

// _________________________________________________________________________________



function mySort(array){

 	let sortedArray = array;

 	typeof sortedArray[0]== "string"? sortedArray.sort():sortedArray.sort((a,b)=>a-b);

 

 	return sortedArray;

}

// _________________________________________________________________________________

\**A funtion that merge two arrays and sort them  */

function arrangeArrays(main,array,...arrays){

 	let combinedArray = main.concat(array);

 	if (arrays.lenght > 0) {

 		for (const newArray in arrays){

 			combinedArray.concat(newArray);

 		}
 	}
 	return mySort(combinedArray);
};





// _________________________________________________________________________________


function assert(reason, message){
	if(reason){
	return ;
	}

	throw new Error(message ? message:"You have provide a non valid value");
}





// _________________________________________________________________________________


function assertTypeof(value, type, message){
	if (value instanceof type){
		return ;
	}
	

	throw new Error(message || `Value ${value} is not instance of ${type.name || typeof type}`)

}


// _________________________________________________________________________________


function run(callback,...values){
	try{
		callback(...values);
	}catch(error){
	 	console.log("An error has occured" +  error);
	}
}



// _________________________________________________________________________________


function callable(callbackfn = null,...value){
	if (callbackfn ===null){
		return value ;
	}
	const result = callbackfn(...value);
	if (result !== undefined || result ){
		return result;
	}
}



// _________________________________________________________________________________

const arrange = (value,callbackfn = null ) => {
	const upper = (str) =>{ return str.trim().charAt(0).toUpperCase() + str.trim().slice(1).toLowerCase();}

	let match = value.match(/\S+/g);
	if (match.length > 1 ){
		let value =  match.map(upper);
		return callable(callbackfn, value.join(" ") );
	}

	return callable(callbackfn,upper(value))

}

// _________________________________________________________________________________





// _________________________________________________________________________________






// _________________________________________________________________________________







// _________________________________________________________________________________

