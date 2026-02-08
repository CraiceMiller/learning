async function recive(url){
    const response = await fetch(url);
    const result = await response.json();
    return result ; 
};

async function send(url,data){
    let info = {
        method: 'POST', 
        message: 'sending data',
        headers: { 
            'Content-Type':'application/json'
        }, 
        body: JSON.stringify(data)

    } ;

    const response = await fetch(url,info);
    const result = await response.json(); 
    return result; 

};


const dict ={
name: "Craice",
age: 18, 
student:true
};

let json  = JSON.stringify(dict);
let data = JSON.parse(json);
function greet(name){for(let i=0; i< 10;i++){console.log(name)}}; 

console.log(data);
console.log(dict);