import print from "./myjs/utils.js";
import {binary,enumerate,any,zip,quickSort} from "./myjs/utils.js";
//<-------------- TESTING THE FUNCTIONS ALL HAND --------------------------->

const days:string[] = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"];
let names:string[]= ["Craice","Miseru","Ashely","Stephany","Darwin"];
let values = names.concat(days); 
for (const va of enumerate(days,100)){
    print(va); 
}

for (const v of zip(names,[1,2,3])){
    print(v)
}


let result = binary(values,"Duck"); 
result.ok ?
print("the value was found in the index: ", result.index," and this is the array ",result.array):
print("The value ",result.target, " was not found ..."); 


export function greet<T>(names:T[]):void{
    if (!any(names)){
        print("Hello world"); 
        return ; 
    }
    for( const [index,na] of enumerate(names,1)){
        print(na, " Friend No.",index);
    }  
}
print(any(days,el => el.length > 6));
greet(names);
print(quickSort(days)); 

