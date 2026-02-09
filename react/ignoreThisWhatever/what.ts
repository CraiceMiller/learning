import print from "../src/utils/utils.js";
import type {Prettify,User} from "../src/utils/typing.js";  
import { all, assert, any, enumerate, quickSort, binary, search } from "../src/utils/utils.js";
let nums = [1, 2, 4, 5, 6, 6, 9, 10, 23, 0, -1, -34, -3, 1234, 3, 2, 1, 5, 6];




let a: Prettify<User> = {
    name: "Craice",
    age: 19,
    info: { country: "Altisora" }
}
print(a); 

print();
print(all<number>([1, 3, 4, 100, 23]))
print();

let c = "Craice miller"; 
// (c.small("red"))

print(binary( quickSort(nums), 2))
