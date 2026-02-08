const title=document.querySelector("h1");
const textBox=document.querySelector("#textbox");
const submit=document.querySelector(".submit");
const p=document.querySelector("#text");
const PI=Math.PI;
let result;
let radius;
title.textContent = "Circuference!";
p.textContent = "Just write the radius of the circle";

/**
 * 
 * @param {number} radius 
 * @returns {number}
 */
function getcircuference(radius){
    return 2 * PI * radius;

}

submit.onclick=()=>{
    radius=Number(textBox.value);
    if (isNaN(radius)){p.textContent = `It must be a number`;return}
    result=getcircuference(radius);
    p.textContent = `The result is ${result.toFixed(3)}`

}


