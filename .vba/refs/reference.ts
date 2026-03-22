function main():void{
    let name:string;
    let div:HTMLDivElement|null;
    let answer:boolean|undefined;

    div=document.querySelector("#div");

    try {
        answer=document.querySelector<HTMLInputElement>("#input")?.checked
        if(answer && div?.innerText==""){
            div.innerText="The square is " + square(10, 2) ;
        }
        else{
            div.innerText=""
        }
        
    } catch (error) {
        console.log("why i keep screwtin gthings up!!!");
    }

}

function square(v1:number,v2?:number):number{
    return v2?v1*v2:v1*v1;
}
