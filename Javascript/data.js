import { print,fetchData} from "./myjs/tools.js";

print("Hello world")
print("Bye world ")

let newUser = {
    username:"Stephany", 
    balance: 5000
}

async function sendData(url,data){
    try{
        const response = await fetch(url, 
            {
                method: 'POST', 
                headers: {
                    'Content-Type': 'aplication/json'
                },
                body: JSON.stringify(data)

            })

        const result  = await response.json()
        print("The server is running")

    }catch(e){
        print(e)
    }
}

 
let url = "http://127.0.0.1:5000/app/data"; 
let usersURL = "http://127.0.0.1:5000/app/users";
let setUsers = "http://127.0.0.1:5000/api/save_user" 

let result = await fetchData(url); 
let users = await fetchData(usersURL); 
print(result)
print(users)

print(result.name)

let age = result.age

age >= 18 ? print("You are an adult"):print("You're young"); 

for (const dict of users){
    print(dict.username); 
    print(dict.balance);
    print("-------->")
}


let info = JSON.stringify(users); 
let obj = JSON.parse(info)
print(info )
print()
print(obj)
let r = await sendData(setUsers,newUser);