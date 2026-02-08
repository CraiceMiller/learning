import {print} from "./tools.js";

//Setting the dictionary___________________________________

const studentsInfo = [ 
    new Map()
    .set("name","Hersy"  )
    .set("age",18  )
    .set("grade-Level","Tourism Bachelor")
    .set("isGoodStudent",true)
    .set("AverageNotes",85)

    ,

    new Map()
    .set("name","Craice"  )
    .set("age",19  )
    .set("grade-Level","Computer Scince")
    .set("isGoodStudent",true)
    .set("AverageNotes",90)

    ,

    new Map()
    .set("name","Ashley"  )
    .set("age",17  )
    .set("grade-Level","Arts")
    .set("isGoodStudent",false)
    .set("AverageNotes",74)

];

//Testing ___________________________________
let averages = [];
/**let  dict = Array(...studentsInfo);
let info = dict.map((value)=>{return value[1]}) ; 
print(info);
print(averages);*/

for ( const dict of studentsInfo){ 
const note = dict.get("AverageNotes"); 

if (note !== undefined){averages.push(note);}

}
print(averages);
print(studentsInfo[0].get("collage"));
print(studentsInfo)



//JSON FILE CREATING ATTEPT >:v        ___________________________________
const jn = JSON.stringify(studentsInfo,null,4);
print("hello World1!!!!")

const blob = new Blob(jn,{type:"application/json"} ); 
const url = new URL.createObjectURL(blob)