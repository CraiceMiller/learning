// 0. A SIMPLE FUNCTION THAT GREET ...*

function greet(name){

 	console.log(`Hello ${name} Nice to meet you `);

}





*//1.JUST CREATING THE VARIABLES*



let numbersArray = \[1,2,3,4,5,6,7,8,9,10];

let stringArray = \["World!", "#Id", "Hello", "Dollar $", "Porcentegage %", "And \&", "(Parenthesis)", "Equeals ="]

let moreNumbers = \[2,2,1,5,12,12,10,7,2,15,0,3];





*//2. A FOR STATMENT*

for (let index = 0; index <= stringArray.lenght; index++){

 	let element = stringArray\[index];

 	if (element !== "hello"){

 		console.log(`This element is ${element}`)

 	}

};





//3. FOR OF STATEMENT

stringArray.forEach(greet);



let numofLetter=0;

//console.log(stringArray );console.log(stringArray.length );

for (const value of stringArray){

 	numofLetter += value.length;

};



console.log(numofLetter);

numofLetter >40 ? console.log("That was so many letters dude!"):console.log("Ok dude :)");







//4. FOREACH STATEMENT

const minNumber = 7;

numbersArray.forEach(number =>{



 	if (number <= minNumber){

 	return;

 	}



 	console.log(number);



})



//5. a function that arrange an array...

function mySort(array){

 	let sortedArray = array;

 	typeof sortedArray[0]== "string"? sortedArray.sort():sortedArray.sort((a,b)=>a-b);

 

 	return sortedArray;





}



/\*\*6. A funtion that merge two arrays and sort them  \*/

function arrangeArrays(main,array,...arrays){

 	let combinedArray = main.concat(array);



 	if (arrays.lenght > 0) {

 		for (const newArray in arrays){

 			combinedArray.concat(newArray);

 		}

 	}



 



 	return mySort(combinedArray);

 

}



let result = arrangeArrays(numbersArray, moreNumbers);

console.log(result);

