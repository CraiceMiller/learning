import React, { useState }  from "react"; 
import Button from "../../components/buttons"; 
import Input from "../../components/choices" ; 
import type {Student,Response} from "../../utils/typing"; 
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