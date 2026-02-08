async function complet(done=true,text=""){
    return new Promise(
        (solve,reject)=>{

            if (!done){
                return reject("A problem has occured "+text);
            }

            return solve("Completed "+ text);



        }

        
    )

}

function type(value,object,error=true,message=null,){
    if( value instanceof object){
        return true ; 
    }

    if (error){
        throw new Error(message || `The value "${value}" it is not a type of "${object.name || typeof object}"! `)}

    return false; 
}




let result = complet(true);
console.log(result.toLocaleString());
console.log(typeof result);
let t = type(result,Promise,false);
console.log(String.name); 
console.log(t);