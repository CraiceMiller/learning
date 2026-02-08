//A SIMPLE DICTIONARY IT IS AN OBJECT	
const person = {

//OBJECTS HAVE VARIABLES TOO, CALL 'PROPITY'...
name: ['craice','miler'], 
age: 18, 

//AND HAVE FUNCTION, CALL 'METHODS'....
bio: function(){
console.log(`${this.name.join(" ")} is ${this.age} years old... `
);
},
introduce: function(){ 
console.log(`Hi I am ${this.name[0]}`);
},
sum:(a,b)=>a+b

}

person.bio();person.introduce();console.log(person.name);
console.log(person.sum(10,5))


//A CLASS OBJECT ------------------------------->


class Vehicule {
    #Type; #turnON; #Running; 
    constructor(model, color="black", type="land"){
        this.model = model ;
        this.#Type = type + " Vehicule";
        this.#turnON = false; 
        this.#Running = false; 
    }
    static gasolineAmount = 100; 

    turnOnVehicule(){
        if (this.#turnON){
            console.log(`The ${this.model} is already turn-on! `);
            return false ; 
        };
        this.#turnON = true; 
        console.log(`The ${this.model} have turned-on now...! `); 
        return true; 
    }

    turnOffVehicule(){
        if (!this.#turnON){
            console.log(`The ${this.model} is already turn-off! `);
            return false ; 
        };
        this.#turnON = false; 
        console.log(`The ${this.model} have turned-off now...! `); 
        return true; 
    }

    get type(){
        return this.#Type; 
    }

    get isTurnON(){
        return this.#turnON ;  
    }

    get isRunning(){
        return this.#Running ; 
    }

    get gasolineTank(){
        let amount = this.gasolineAmount;
        if (amount >=90){
            console.log("FULL");
        }
        
        if (amount <= 0){
            console.log("empty");
        }
        
        if ( amount >= 40){
            console.log("steadly");
        }

        else{
            console.log("The car is getting running out of gasoline");
        }

         
        return amount

    }


}



class Car extends Vehicule {
    #wheels;#Speed;#Type; #turnON; #Running;
    constructor(model,speed=100, color="black",){
        super(model,color,"land");
        this.#wheels = 4;
        this.#Speed = speed; 
    }

    

    drive(minutes=60){
        if (!this.#turnON){
            console.log("you MUST turn on the car first!!");
            return false; 
        }

        if (this.gasolineAmount <= 0){
            console.log("The car has no gasoline to run");
            return false; 
        }

        if (this.#Running){
            console.log("The car is already doing another action. Therefore it cannot drive right now "); 
            return false; 
        }

        console.log("The car is driving"); 
        this.this.gasolineAmount -= gasolineAmount - (minutes * 0.20); 
        this.#Running = true; 
        return true; 
    }

    stop(){
        if (!this.#Running){
            console.log("The car was not doing any action... "); 
            return false; 
        }

        

    }

    

    


}

const n = new Notification("Hello Nice to meet you");
const car = new Car("car");
console.log(car.isTurnON);
console.log(car.gasolineTank);
car.turnOnVehicule();
console.log(car.isTurnON);
car.drive(); console.log(car.gasolineTank);
    
//#######################################################
 function random(min=0,max=100){
    let digits = Math.random(); 
    console.log(`Result of digit ${digits} `)
    let number = digits * (max - min + 1)+min; 
     console.log(`Result of number ${number} `)
    let result = Math.floor(number); 
    return result 

}

let r = random(); 
console.log(r); 
