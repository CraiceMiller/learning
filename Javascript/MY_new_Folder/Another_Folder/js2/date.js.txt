const print=(...value)=>console.log(...value);
const date = new Date();
//const hour = `${date.getHours()}:${date.getMinutes()} `;
//const days = ["Sunday","Monday","Tuesday","Wednesday", "Thursday","Friday","Saturday"]; 
//const indexDay = date.getDay();
//const day = days[indexeDay];
//print(date);
//print(new Date());
print(date.toDateString());
print( );
print( );

Date.prototype.Hour = function Hour(fn=null){
    //const print=(...value)=>console.log(...value);
    const date = new Date();
    const hour = `${date.getHours()}:${date.getMinutes()} `;
    if(fn !== null){
        fn(hour);
        return null;
    }

    
    return hour; 
}

Date.prototype.Today = function Today(fn=null){
    //const print=(...value)=>console.log(...value);
    const date = new Date();
    const days = ["Sunday","Monday","Tuesday","Wednesday", "Thursday","Friday","Saturday"]; 
const indexDay = date.getDay();
const day = days[indexDay];
    if(fn !== null){
        fn(day);
        return null;
    }

    return day;

}
const h = new Date();
h.Today(print);
h.Hour(print);