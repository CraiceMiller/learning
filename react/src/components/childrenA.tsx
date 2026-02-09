import React from "react"; 
import {useContext, useState,createContext,useEffect } from "react" ;
import {Form,List} from  "./choices"; 

export const userContext:React.Context<string> = createContext('User') ; 

export function MyComponentA():React.JSX.Element{
    const [user,setUser] = useState<string>(""); 
    return (
        <div className="Mini-Box" >
            <h5> MyComponentA </h5>
            <Form  text="cllick it " onSend={v=>v ? setUser(v):undefined}  />

            <p>I am the {MyComponentA.name} and I am sending the  message <ins> <b>'{user}'  </b>  </ins>  to the component C </p>
            <p>{ `Hello ${user}` } </p>
            
            <userContext.Provider value={user}>
                <MyComponentB />
            </userContext.Provider>
            

        </div>
    )
}

export function MyComponentB():React.JSX.Element{
    return (
        <div className="Mini-Box" >
            <h5> MyComponentB </h5>
            <MyComponentC />
        </div>
    )
}



export function MyComponentC():React.JSX.Element{
    const [Names,listNames] = useState<string[]>([]); 
    //const [user,setUser] = useState<string>(""); 

    const user:string = useContext(userContext ) ;
    //console.log("I am here componenet C"); 
    //console.log( user) ; 
    // this will happend every time the user re-render; 
    useEffect(()=>user ? listNames(prev => [...prev, user]):undefined, [user])


    return (
        <div className="Mini-Box" >
            <h5> MyComponentC </h5>
            <p>And i recive the message <b>  '{user}' </b>  from {userContext.name}</p>
            <p>{`Bye ${user}`} </p>

            <List  values={Names} />

        </div>
    )
}