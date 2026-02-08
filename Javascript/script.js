import {print} from "./myjs/tools.js";
//let path= "./User Accounts.json";



//Promise
function complet(done=true,text=""){
    return new Promise(
        (resolve,reject)=>{
            if(!done){
                return reject("Something goes wrong "+text)
            }

            return resolve("The task was complete "+text)
        }
    )
}


//This functions (sync) do not return a promise, only return a simple value.
//however when i create the funciton (complet) every function below will return a promise now 
function cleanHouse(done=true)
{
    if (!done){
        return complet(done, "You DO NOT clean the house. you gonna be scolded")
    }
   
    return complet(done,"You cleaned the house")
}

function doMath(done=true)
{
    if (!done){
        return complet(done, "You DO NOT complet your math task. you are going to have bad degrees...")
    }

    return complet(done,"You have done very complecated math tasks")
}


function wacthAnime(done=true)
{
    if (!done){
        return complet(done,"You so tired that you couldn't watch any anime ")
    }
  
    return complet(done,"You are happy to watch you favorite anime ... ")
}


//for default this return a Promise object 
async function study(done=true)
{
    return done

}


//ASYNC FUNCTION TO DO THE TASK
//i guess this funtion will wait untill the another function return the value and later will finish... i guess

/**
 * @description
        this function only carry out an awaitable function and do another thing based of the result in the 
        previous function provided. This will not do the second tasks if :
            - The result of the firts task is None.
            - The callbackfn param is None
            - The callbackfn is not Callable

    
* @param {function} task: The awaitable function to be executed
*@param {function|null} callbackfn:  The another task to do later to complet the first one, it will do nothing if 
        it is null
*@param {Any} args : is only the params the first task needs
 * 
 */
async function doTask(task,callbackfn=null,...args){
    try{
        const result = await task(...args); 

        if (result !== undefined && callbackfn !== null){
            callbackfn(result)
        }
    }catch(e){
        print(e)

    }
}



//I guess this function will not wait the another function and will finished without the 
async function doAsyncTask(task,callbackfn=null,...args){
    try{
        const result = task(...args); 

        if (result !== undefined && callbackfn !== null){
            callbackfn(result)
        }
    }catch(e){
        print(e)

    }
}



//API -------------------------------------------------------------------------------------------->
async function fetchData(url){
    try{

    const response = await fetch(url);
    if (!response.ok){
        throw new ReferenceError("Could no fetch the resource...")}

    const data = await response.json(); 
    return data;

    }catch(e){
        print(e)
    }
}


 

//API -------------------------------------------------------------------------------------------->

//testing

//let resp = fetchData(url);
const button = document.querySelector("#button"); 
const input = document.querySelector("#pokeName");
const img = document.querySelector("#pokeImg")
const body = document.querySelector("body")

//creating the function to get the apin 
async function getPokemon (event){
    //ensuring that the key pressed is enter or the even is a click...
    if (event.key !== "Enter" && event.type !=="click"){return ;}

    //getting the value of the input 
    const value = input.value; 
    if (value ===""){return; }

    //the variable url to search the api 
    let url = "https://pokeapi.co/api/v2/pokemon/";
    url +=value.toLowerCase() ;

    //waiting the result from fetch
    let result = await fetchData(url); 

    
    //updating the image
    img.src = result.sprites.front_default;
    img.style.display = "block";
    img.height = "100px";

    //cleaning the input 
    input.value = "";
    print(result)
}


input.value = "100";
button.addEventListener("click", getPokemon);
body.addEventListener("keydown",getPokemon);








doTask(
    doMath, 
    print,
    true 
)

/** 
cleanHouse().then(
    value =>{print(value); return wacthAnime()}
)
.then(
    value =>{print(value)}
)
.catch(
    error =>print(error)
)*/

let tasks = [cleanHouse,doMath,wacthAnime,study];
let map = tasks.map(value => doTask(value));
let doing = await Promise.all(map);
//print(doing);
//print("Hello world")


//await doMutiplyTasks(tasks,print)



/**
 * HOW TO SCAPE TUTORIAL HELL 
 *  1. you MUST know the basic of programming...
 * 
 */

async function  lookICanProgamHurHurHur()
{
    console.log("YEAH I KNOW THE FUNDAMENTALS...")
}