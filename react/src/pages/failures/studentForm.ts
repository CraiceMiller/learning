import type {Student,Response} from "../../utils/typing"; 
import {getData, sendData} from "../../utils/utils"; 



const ID_URL:string = "http://127.0.0.1:5000/api/ids"
const ID_DATA:string = "http://127.0.0.1:5000/api/data"

type IDProps = {
    ids:number[]
}

//This function only get us the last id in my studentSever.py
async function getLastId():Promise<number>{
    const  data: IDProps | undefined = await getData<IDProps>(ID_URL); 


    console.log("This my getLastId function ")
    console.log(data, typeof data)
    if (!data){return 1 }
    return Math.max(...data.ids )
    
}

//This function only create us a studnet object
export async function sendStudentInfo(INFORMATION:Student):Promise<Response>{
    try{ 
    INFORMATION.basic.id =  await getLastId () + 1; 
    console.log(INFORMATION); 

    const response = await sendData<Student>(ID_DATA,INFORMATION) ; 
    return response
    }catch(e){
        return {
            "ok":false,
            "message":"Something went wrong", 
            "method":"GET",
            "responseClass":"data",
            "encoded": false, 
            "status":"error",
            
            "details":{ 
                "httpReason":"error" ,
                "httpCode":550, 
                "code": "error"
                }, 
    
            "Headers":{
                "contentType":"application/json"
                }
            }
    
    }
}