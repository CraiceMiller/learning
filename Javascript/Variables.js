//This is my first javascript file 12/09/2025
//variables = a container that store a value (string, integer, float, boolean)
//            a variable bahave as if it was the value it contain

//1. Declaration        let x;
//2. Assignment         x = 100;

//let are unique


let _name= 'Cracie';
let country='altisora';
const food = "Chilly dogs";
const hobby = "read anime & wacht a bunch of anime";
const weight=130.25;
let age = 19;
let is_students = true ;
let for_sale = false;
let is_onlie;

is_onlie=true
hobby="none"


//----
//strings: is a serie of characteres they can include numbers but we treat them as characters. 
//      is a serie of text this could be double quotes
console.log(`What's up ${_name}`);
console.log (`"I bet up your favorite food is ${food} like me, donthca"`);
console.log (`"and you love ${hobby} like the wormbook you are"`);
console.log (`"btw you are above of ${age}, right, otherwirse you're gonna kick my ass bro"`);

//Booleans: is eitehr true or false
console.log(`"are you really a student dude?: ${is_students}"`)
if (for_sale) {
    console.log("indeed, my notebooks is for sale, why d'ya ask ")
    
} else {
    console.log("Sorry dude but my body, i mean, my notebook is NOT for sale anymore")
}; 
if (is_onlie){
    console.log("ofc dude, in fact, i wanna play the new wap that was added this morning")
} else{
    console.log("screw ya, i need to study cuz the dang teachers are a pain in my ass")
}
if (is_students && is_onlie) {
    console.log("hello")
    
} else {
    console.log("bye")
    
}




