import {print,arrangeUserName} from "./tools.js"

let user= "                       craICE MILLER castilla lEON                        ";
let user2 = "ashely";
let user3 = "hersy herson";
let user4 = "  mISERU sEMPAI "; 

let allUsers = [user,user2, user3,user4];


allUsers.forEach(
    (message) => print(arrangeUserName(message))
)