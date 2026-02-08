//15/09/2025
//callback
let text =document.getElementById("text");
let head= document.getElementById("h1");



function hello(name){
    const hello=`Hello ${name}`;
    head.textContent= hello;
} 



function bye(callback){
    head.textContent= "Bye World";
    callback();
}

function sum(callback,a,b){
    let result=a+b;
    callback(result);
}

function print(...values){
    if (values.length===0){
        console.log("")
        return 
    }
   console.log(...values)
}


function displaytext(_text){
    text.textContent = _text;

}

function evenNumber(array,callback){
    let even=[];
    for (const number of array) {
        if (number % 2 == 0){
            even.push(number);
        }
    }
    callback(even)
}

function changeTitle(_head){
    head.textContent = _head;
}

function changeParagraph(p){
    text.textContent = p;
}



let array=[1,2,3,4,5,6,7,8,9,10];
let names=["hersy","craice","misery","ashley","stephany","junior","andrew","samantha","mark","oliver atom","tomas","aligoberta","carrera"];
evenNumber(array,print)

sum(changeTitle,100,50);
evenNumber(array,changeParagraph)


names = names.sort();

names.forEach(element => {
    if (element.length < 6){print(element)}
});

let shortnames=names.filter(na=>na.length < 6);
print(shortnames);
print(names)






