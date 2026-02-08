import { print } from "./tools.js";
let animes = ['nazo no kanojo'];
let moreAnimes= ["Call of the night","Dr. Stone","Re-zero"];

print(animes)
print("Append")
animes.push('jojos',"Re-zero");
animes.unshift('city animation');
print(animes)
print("Insert")
animes.splice(2,"Stain-Gate")
print(animes)
print("Remove")
//animes.remove("Re-zero")
//print(animes)
print("Index")
print(animes.indexOf("jojos"))
//print(animes)
print("Count")
let count = animes.filter(item => item == "Re-zero").length
print(count)
print("Sort")
animes.sort()
print(animes)
print("Copy")
let Copy=animes.slice();
print(Copy)
print("Extend")
animes=animes.concat(moreAnimes)
print(animes)
print("Pop last")
animes.pop()
print(animes)
print("Pop First")
animes.shift()
print(animes)
print("Reverse")
animes.reverse()
print(animes)
print("Map")
animes=animes.map(x=>x.toUpperCase());
print(animes)
print("Filter")
animes=animes.filter(y=>y.length <=9);
print(animes)
print("Clear")
animes.length = 0;
print(animes)


