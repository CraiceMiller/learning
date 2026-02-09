"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
let Name = "Hersy";
let age = 18;
let isStundet = true;
console.log(age);
function greet(name, list = null) {
    console.log(name);
    if (list === null) {
        return;
    }
    for (let i = 0; i < list.length; i++) {
        console.log(list[i]);
    }
}
greet(Name, ["Craice", "Ashely"]);
//# sourceMappingURL=basics2.js.map