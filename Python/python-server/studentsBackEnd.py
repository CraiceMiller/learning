from mypython.files import FileManager #type: ignore 
from typing import Any


#creating the variables needed...
FILE:FileManager = FileManager()
DATABASE:str = "C:/Users/Usuario Pc/Desktop/programming/data/studentsDataBase.json"


#creating the function needed...

def get_current_data()->list[dict]: 
    return FILE.read_json(DATABASE,False)


#function to recive the data and append it into my data const
def add_data(data:dict[str,Any])->dict:
    """function to recive the data and append it into my data const"""
    result:bool = FILE.write_json(DATABASE,data)
    if ( not result ):
        return  {
        "ok":False,
        "message":"Something went wrong", 
        "responseClass":"data",
        "encoded": False, 
        "status":"error",
        
        "details":{ 
            "httpReason":"error" ,
            "httpCode":550, 
            "code": "error"
            }, 

        "Headers":{
            "content-Type":"application/json"
            }
        }

    return {
        "ok":True,
        "message":f"Everything is ok, The student {data["basic"]["name"]} has been added succefully :)" , 
        "responseClass":"data",
        "encoded": False, 
        "status":"Send Data",
        
        "details":{ 
            "httpReason":"sendData" ,
            "httpCode":200, 
            "code": "succesfully"
            }, 

        "Headers":{
            "content-Type":"application/json"
        }
    }

#This is just return a dict of an array with all the students id
def students_id()->dict[str,list[int]]: 
    """This is just return a dict of an array with all the students id """
    try:
        DATA = get_current_data()
        if(not DATA):
            return {"id":[0]}
        
        return {
            "ids":[i["basic"]["id"] for i in DATA] 
        }
    
    except : 
        return {
            "id":[0] 
        }



"""
Backend: 
studentBackEnd.py
from mypython.files import FileManager #type: ignore 
from typing import Any


#creating the variables needed...
FILE:FileManager = FileManager()
DATABASE:str = "C:/Users/Usuario Pc/Desktop/programming/data/studentsDataBase.json"
DATA:list[dict] = FILE.read_json(DATABASE,False)

#creating the function needed...


#function to recive the data and append it into my data const
def add_data(data:dict[str,Any])->dict:

    result:bool = FILE.write_json(DATABASE,data)
    if ( not result ):
        return  {
        "ok":False,
        "message":"Something went wrong", 
        "responseClass":"data",
        "encoded": False, 
        "status":"error",
        
        "details":{ 
            "httpReason":"error" ,
            "httpCode":550, 
            "code": "error"
            }, 

        "Headers":{
            "content-Type":"application/json"
            }
        }

    return {
        "ok":True,
        "message":f"Everything is ok, The student {data["basic"]["name"]} has been added succefully :)" , 
        "responseClass":"data",
        "encoded": False, 
        "status":"Send Data",
        
        "details":{ 
            "httpReason":"sendData" ,
            "httpCode":200, 
            "code": "succesfully"
            }, 

        "Headers":{
            "content-Type":"application/json"
        }
    }

#This is just return a dict of an array with all the students id
def students_id()->dict[str,list[int]]: 

    try:
        global DATA
        return {
            "id":[i["basic"]["id"] for i in DATA] 
        }
    
    except : 
        return {
            "id":[1] 
        }

        

studentsServer.py
from flask import Flask, jsonify, request, Response
from flask_cors import CORS #type: ignore
from studentsBackEnd import DATA,add_data, students_id  #type: ignore 

app = Flask(__name__) 
URL = "/api/data"
CORS(app)

@app.get(URL)
def sendData()->Response:
    return jsonify(DATA)

@app.get("/api/ids")
def getIds():
     return jsonify(students_id())

@app.post(URL)
def getData()->tuple[Response,int] : 
    response = request.get_json(force=True, silent = True,cache=True)
    

    if response is None: 
            return jsonify( {"status":"error", 
                             "message": "no JSON received"}), 400


    result:dict= add_data(response)
    if (not result["ok"]): 
        return jsonify(result), 550

    return jsonify(result), 200








if __name__ == "__main__":
    app.run(debug=True)

    

Front-End : 
#studentForms.ts
import type {Student,Response} from "../myjs/typing"; 
import {getData, sendData} from "../myjs/utils"; 



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

#studentFormUI.tsx
import React, { useState }  from "react"; 
import Button from "./components/buttons"; 
import Input from "./components/input" ; 
import type {Student,Response} from "../myjs/typing"; 
import {sendStudentInfo} from "./studentForm"; 
/**input.tsx
 * import type {InputProps} from "../../myjs/typing.ts";  


export default function Input({labelName,placeholder,type,className}:InputProps){

    return (
        <div className={className} >

            <label >{labelName} </label>
            <input type={type} placeholder={placeholder} />
            
        </div>

        

    )


}
 * 

typing.ts
export type  InputProps= {
    labelName?: string;
    placeholder?:string,
    type?:string , 
    className?:string 
} 


export type Student = {
    basic:{ 
        id:number,
        name:string, 
        lastName:string, 
        age:number, 
        gender:"male"|"female"
    }, 
    educational:{
        degree: "management bussines" | "chartered accountant" | "bachelor's degree in computer science", 
        year?: "first" | "second" | "third", 
        schoolCycle?:string 
    }

    details?:{
        country?:string, 
        phone:number,
        transportation?:"public"|"car" | "motocycle" | null, 
        languages?:string[], 
        hasJob?:boolean,
        dateBirth?: Date,
        parent?:{
            mother?:{
                name:string,
                address?:string, 
                email?:string,
                other?:{
                    extraInfo:string
                }

            }, 
            father?:{
                name:string,
                address?:string, 
                email?:string,
                other?:{
                    extraInfo:string
                }

            }, 
        }, 
        emergencyContact?:{
            name:string, 
            phone:number, 
            relationship:string, 
        }
    }
}


 * 

buttons.tsx
import type {ButtonProps} from "../../myjs/typing.ts";  



export default function Button({text="Button",command,title,type}:ButtonProps){
    return(
        <> 
        <button onClick={command} title={title} type={type} >{text}</button>
        </>
    )
}

StudentStule.css
:root {
    font-family: system-ui, Avenir, Helvetica, Arial, sans-serif;
    color: rgba(255, 255, 255, 0.87);
    background-color: #0E101C;
    font-synthesis: none;
    text-rendering: optimizeLegibility;
}


  
body {
    margin: 10vh;
    display: flex;
    gap:10px; 
    place-items: center;
    align-items: center;
    justify-content: center;
    text-align: center;
}

div{
  display: flex;
  flex-direction: column;
  padding: 0;
  gap:2vw; 


}

.block{
    justify-items: flex-start;
    align-items: flex-start;
    gap:1.5px; 


}


input{
    background-color: transparent;
    border: 0.5px solid white;
    color:white; 
}
label{
    color:white ; 
}
.row{
    flex-direction: row;
    justify-content:flex-end ;
}

#buttons{
    min-height: 2vw;
    justify-content: center;
}

#info{
  display: flex;
  min-width: 20px;
  min-height: 20px;
  flex-direction: column;
  height: 100%;
  width: 35%;
  gap:2vw; 
  border:2px solid transparent;
}
#my-form{
    display: flex;
    justify-content: space-around;
    min-width: 20px;
    min-height: 20px;
    flex-direction: column;
    height: 100%;
    width:75%;
    padding:10px; 
    border:2px solid transparent;
 }

main{
  display: flex; 
  justify-content: space-around;
  align-items: center;
  min-width: 20px;
  min-height: 20px;
  height: 500px;
  width: 850px; 
  padding: 10px; 
  gap:10px; 
  flex-direction: row;
  border:2px solid purple ;
}
  


h1 {
  font-size: 3vw;
   line-height: 1.1;
   color: #7D42F6; 
   text-decoration: dotted;
}
  
button {
    border-radius: 20px;
    border: 1px solid transparent;
    padding: 0.6em 1.2em;
    font-size: 1em;
    font-weight: 500;
    width: 10em;
    background-color: #2A1B81;
    color:#ffffff; 
}

button:hover {
    box-shadow:1px 1px 15px #646cff;
}

button:focus,
button:focus-visible {
    outline: 4px auto -webkit-focus-ring-color;
  }


@media (max-width: 200px){
    :root{
        background-color: red;

    }
}
 */

export default function App(){
    const initialStudent: Student = {
        basic: {
            id: 0,
            name: "",
            lastName: "",
            age: 0,
            gender: "male", 
        },
        educational: {
            degree: "bachelor's degree in computer science", 
        },
    };
    const [message, changeMessage] = useState<string>("Please, Could you fill the new form"); 
    const [information, updateInformation] = useState<Student>(initialStudent); 
    

    const cleanInput = (m=true)=>{
        updateInformation(initialStudent); 
        if (m){
        changeMessage("So you can start again :)")
        }


    }

    async function submitHandler(event:React.FormEvent){

        event.preventDefault();
        if(information.basic.age <= 0){
            changeMessage("You must prived a valid age"); 
            return ; 
        }

        const result: Response = await sendStudentInfo(information)
        cleanInput(false); 
        changeMessage(result.message); 
    }

    const handlerInputChange = (event:React.ChangeEvent<HTMLInputElement>)=>{
        const {name, value }= event.target; 
        const [ SECTION, FIELD ] = name.split(".");
        
        updateInformation(prevInfo=>{

            const newInfo= JSON.parse(JSON.stringify(prevInfo));

            if(newInfo[SECTION ] !== undefined && newInfo[SECTION][FIELD] !== undefined){
                newInfo[SECTION][FIELD] = value ; 
            }
            
            return newInfo ; 
        } )





    }

   
    



    return(
        
        <>
        <div id="info">
            <h1>My form </h1>

            <p>{message}</p>

        </div>

        <form id="my-form" onSubmit={submitHandler}>
            <div className="row">
                <Input
                labelName="Names"
                type="text"
                placeholder="name"
                className="block" 
                name="basic.name"
                value={information.basic.name}
                onChange={handlerInputChange}
                />

                <Input
                labelName="Last Names"
                type="text"
                className="block"
                placeholder="Last names"
                name="basic.lastName"
                value={information.basic.lastName}
                onChange={handlerInputChange}

                />
            </div>


            <div className="row" >
            <Input
            labelName="Age"
            type="number"
            className="block"
            placeholder="your age" 
            name="basic.age"
            value={information.basic.age}
            onChange={handlerInputChange}
            />
            <Input
            labelName="Degree"
            type="text"
            className="block"
            placeholder="your carrer"
            name="educational.degree"
            value={information.educational.degree}
            onChange={handlerInputChange}

            />
            </div>

            <div className="row">
            <label>Gender: </label>

                <label>Women</label>
                <input
                type="radio"
                name="basic.gender"  
                value="female"
                checked={information.basic.gender === "female"}
                onChange={handlerInputChange}
                />

                
                <label>men</label>
                <input
                type="radio"
                name="basic.gender"  
                value="male"
                checked={information.basic.gender === "male"}
                onChange={handlerInputChange}
                />

                

            </div>

            <div id="buttons" className="row">
                <Button text={"Send"} type={"submit"} />
                <Button text={"Clean"} type={"button"} command={cleanInput}   />

            </div>

        </form>

      
        
        </>
    ); 
}


typing.ts
export type Student = {
    basic:{ 
        id:number,
        name:string, 
        lastName:string, 
        age:number, 
        gender:"male"|"female"
    }, 
    educational:{
        degree: "management bussines" | "chartered accountant" | "bachelor's degree in computer science", 
        year?: "first" | "second" | "third", 
        schoolCycle?:string 
    }

    details?:{
        country?:string, 
        phone:number,
        transportation?:"public"|"car" | "motocycle" | null, 
        languages?:string[], 
        hasJob?:boolean,
        dateBirth?: Date,
        parent?:{
            mother?:{
                name:string,
                address?:string, 
                email?:string,
                other?:{
                    extraInfo:string
                }

            }, 
            father?:{
                name:string,
                address?:string, 
                email?:string,
                other?:{
                    extraInfo:string
                }

            }, 
        }, 
        emergencyContact?:{
            name:string, 
            phone:number, 
            relationship:string, 
        }
    }
}

export type Response = {
    ok:boolean , 
    message:string , 
    method: 'POST'|'GET', 
    responseClass: string, 
    encoded:boolean , 
    status:string, 
    body?:string, 
    details?:{
        httpReason?:string, 
        httpCode: number, 
        code?:string
    }, 
    Headers?:{
        contentType:string
    }
}



utils.ts 

//
export async function getData<dict>(url:string):Promise<dict | undefined >{
    try{

    const response = await fetch(url);
    if (!response.ok){
        throw new ReferenceError("Could no fetch the resource...")}

    const data = await JSON.parse(JSON.stringify(response)); 
    return data;

    }catch(e){
        console.log(e);
        return undefined ;
    }
};


//
export async function sendData<dict>(url:string,newData:dict){
    try{
        const info = {
            method: 'POST', 
            message: "new data", 
            body: JSON.stringify(newData,undefined,4), 
            status:"sending", 
            headers: {
                'Content-Type':'aplication/json'
            }
        }; 

        const response = await fetch(url,info); 
        return await  response.json(); 

        
    }catch(e){
        return {
            "status":"error", 
            "ok": false
        }
    }

}



"""

