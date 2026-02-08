const print = (...value)=>console.log(...value);
//dict class___________________________________
class PyDict extends Map{ 
constructor(){ 
super()
}

getvalues(){ 
let values = [];
for (const [key,value] of this.entries()){
values.push(value);
}

return this.values();
}

}



//Setting the dictionary___________________________________

const studentsInfo = new Array(

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

);

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

