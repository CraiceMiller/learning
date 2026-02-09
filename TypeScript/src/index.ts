import {Task} from "./types.js" ; 

const readAnime= new Task<string[]>("Read Anime",22,
["Nishijou",
"Re-Zero", 
"Full Metal Alchemist",
"No game no life"])
readAnime.do()
console.log(readAnime.length, readAnime.taskName); 
