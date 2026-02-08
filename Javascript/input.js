const title=document.getElementById("h1");
const textBox=document.getElementById("textbox");
const submit=document.querySelector(".submit");
const p=document.getElementById("text");
let username;


title.textContent = "Input!";
p.textContent = "Wrtie your username :3"
//I guess this is an event 
submit.onclick = ()=>{
  //here we get the value from the textbox,
  //i guess it is the same in python 
  // textbox.get()
  username=textBox.value;
  //Here we just update the pargraph in html
  p.textContent = `Hello ${username}`
  textBox.value = "";
}


   



  