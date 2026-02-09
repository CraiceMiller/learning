let Name:string = "Hersy";
let age:number = 18;
let isStundet:boolean = true; 
console.log(age);

function greet(name:string,list:string[]|null=null):void{
    console.log(name); 
    if(list===null){return}
    for (let i:number = 0;i < list.length;i++){
        console.log(list[i]);
    }
}

greet(Name,["Craice","Ashely"]);