const title=document.getElementById("h1");
const textBox=document.getElementById("textbox");
const textBox2=document.getElementById("textbox2");
const textBox3=document.getElementById("textbox3");
const submit=document.querySelector(".submit");
const p=document.getElementById("text");
let result;
title.textContent = "Typecasting!";
p.textContent = "Wrtie a number an operatior and another number";


/**
 * Just a symple calculator
 * @param {number} num1 
 * @param {string} symbol
 * @param {number} num2 
 * @returns {number|null}
 */
function calculator(num1,symbol,num2){
    if (symbol==="/" && num2 ===0){return null}
    if (symbol ==="+"){
        return num1 + num2;
    }
    if (symbol ==="-"){
        return num1 - num2;
    }
    if (symbol ==="*" || symbol ==="x" ){
        return num1 * num2;
    }
    if (symbol ==="/"){
        return num1 / num2

    }

    return null


}




submit.onclick = ()=>{
    let n1=Number(textBox.value);
    let symbol=textBox2.value;
    let n2=Number(textBox3.value);

    result = calculator(n1,symbol,n2)
    result ===null ? p.textContent ="Something goes wrong":p.textContent = `The result is ${result}`;
}





