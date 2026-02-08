//Solving Basics Problems
/**
1. print number form 1 to 100, but every number multiply by three must be print the work "frezze" 
*/ 

function assert(reason, message){
	if(reason){
	return ;
	}

	throw new Error(message ? message:"You have provide a non valid value");
}

function assertTypeof(value, type, message){
	if (value instanceof type){
		return ;
	}
	

	throw new Error(message || `Value ${value} is not instance of ${type.name || typeof type}`)

}




function Frez(maxNumber=10){
for (let index = 0; index <= maxNumber; index++){ 


(index % 3 == 0) ?console.log("Frezze!"):console.log(index);
	
}
}

function run(callback,...values){
	try{
		
		callback(...values);

	}catch(error){

	 	console.log("An error has occured" +  error);


	}

}



const variable = {

dict: {a:"this is a dict", b:"it is quite simple"},
str: "this is a string object where you can write everything you want, 
int: 10, 
float:10.50, 
array:[1,2,3,4,5,6,7,8,9,10],
n:null,
und:undefiend, 
boolean:true,
func:function sum(a,b=-1){if(a >=100){return b}return a+b}, 
arrow:(x,y)=>x+y,

}


console.log(variable.int);




 





/**********   */

let x = true;
let numbersArray = [1,2,3,4,5,6,7,8,9,10];
let stringArray = ["World!", "#Id", "Hello", "Dollar $", "Porcentegage %", "And \&", "(Parenthesis)", "Equeals ="];
let moreNumbers = [2,2,1,5,12,12,10,7,2,15,0,3];


