import {print} from "./tools.js"

/**
programming:.
│   __init__.py
│
│
├───data
│       Historial file.json
│       info.json
│       my_first_json.json
│       Sale_Management.json
│       todo.json
│       User Accounts.json
│
├───frames
│   │   __init__.py
│   │
│   ├───myjs
│   │       tools.js
│   │
│   └───mypython
│       │   bank.py
│       │   classes.py
│       │   dictionary.py
│       │   file_detection.py
│       │   functions.py
│       │   logicalGates.py
│       │   translator.py
│       │   watch.py
│       │   _bank.py
│       │   __init__.py
│       │
│       └───__pycache__
│             
│
├───Html
│   │   advertasing.html
│   │   boxes.html
│   │   boxes2.html
│   │   boxes3.html
│   │   boxestyle.css
│   │   boxestyle2.css
│   │   boxestyle3.css
│   │   calculator.html
│   │   checked.html
│   │   counter.html
│   │   index.html
│   │   indextext.py
│   │   layout.html
│   │   layout.js
│   │   learn.html
│   │   stylelearn.css
│   │   testing.html
│   │   vedal.html
│   │   vedalstyle.css
│   │
│   └───assets
│           BOOM - Evil (Official Video).mp3
│           duck.png
│           I gave my AI control of a CAR.mp4
│           neurosama.jpg
│           vedal.jpg
│
├───javascript
│       1.js
│       2.js
│       3.js
│       4.js
│       array.js
│       arrays.js
│       callbacks.js
│       circuference.js
│       class Product{.js
│       content.js
│       Functions.js
│       hash.js
│       input.js
│       Math.js
│       moreArrays.js
│       names.js
│       print.js
│       QUICK-SORT.js
│       script.js
│       searching.js
│       Solving Basics Problems.js
│       tools.js
│       typecasting.js
│       Variables.js
│
└───python
        arrays.py
        my_ocs.py
        my_original_character.py
        script.py
 
 */


class Character{
    #name;
    #health;
    #pwAttack;
    #gold;
    #id;
    #isAlive;
    constructor(id,name,pwattack,health = 100,gold = 10){
        this.#name = name;
        this.#health = health; 
        this.#pwAttack = pwattack;
        this.#gold = gold;
        this.#id = id;
        this.#isAlive = true; 
    }

    attack(target){
        if (!this.canAttack()){return }

        const powerAttack = this.#pwAttack  * 0.45;
        target.reciveDamage(powerAttack);
        print(`${this.#name} attacks ${target.#name}`);
        print(`${target.#name} recive ${powerAttack}`); 
        print(`${target.#name}'s health:  ${target.#health}`);
    }


    reciveDamage(damage){
        this.#health -= damage;
        if (this.#health <= 0){
            print(`${this.#name} has dead...`);
            this.#isAlive = false; 
        }

    }


    showStatus(){
        const STATUS = this.status;
        print("-------------------------------");
        for (const key in STATUS) {
            print(`${key} : ` , STATUS[key])
        }
        
    }

    canAttack(){
        if(!this.#isAlive){
            print(`${this.#name} cannot still fighting, due is dead`)
            return false;
        }

        print(`${this.#name} can still fighting`);
        return true;

    }


    get status(){
        return {
            name:this.#name,
            powerAttack:this.#pwAttack, 
            health:this.#health,
            gold: this.#gold
        }
    }

    get health(){
        return this.#gold
    }



}


class Knight extends Character {
    #health; 
    #mgAttack;

    constructor(id,name,pwattack,health =120,mgAttack = 20, gold = 40){
        super(id,name,pwattack,health,gold); 
        this.#mgAttack = mgAttack;
    }

    get status() {
        let STATUS = super.status;
        STATUS.health = this.#health;
        STATUS.magicAttack = this.#mgAttack;
        return STATUS;

    }

}


//Testing 

const Craice = new Knight(1200,"Craice",150,40,700); 
const Hersy = new Knight(1201,"Hersy",100,20,200); 



Hersy.showStatus();
print();
Craice.attack(Hersy);
Hersy.attack(Craice);
Craice.attack(Hersy);
Craice.attack(Hersy);
Hersy.attack(Craice);
print();
Hersy.showStatus();







