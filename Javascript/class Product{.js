class Product{
#price;
#quantity;
#total;
#name; 
#description;

constructor(name,price,quantity,description=null)
{  
	this.#name = name; 
	this.#price = price; 
	this.#total = 0; 
	this.#quantity = quantity;
	this.#description = description; 
}

display(){ 
for (const [key,value] of this.info){
console.log(key,value);

}
}


get info(){
return new Map()
.set("name", this.#name)
.set("price", this.#price)
.set("quantity", this.#quantity)
.set("description", this.#description)

}


get price(){
return this.#price; 
}

set price(value){
this.#price = value; 
}



}

const print = (...value ) => console.log(...value);
const product1 = new Product ("Coffee",
15,
75,
new Map()
.set("size", "medium")
.set("type", "Latte")
.set("sugar", false)
); 

print(product1.price);

product1.display(); 