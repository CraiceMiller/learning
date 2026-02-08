function callable(callbackfn = null,...value){
	if (callbackfn ===null){
		return value ;
	}
	const result = callbackfn(...value);
	if (result !== undefined || result ){
		return result;
	}
}


const arrange = (value,callbackfn = null ) => {
	const upper = (str) =>{ return str.trim().charAt(0).toUpperCase() + str.trim().slice(1).toLowerCase();}


	let match = value.match(/\S+/g);
	if (match.length > 1 ){
		let value =  match.map(upper);
		return callable(callbackfn, value.join(" ") );
	}

	return callable(callbackfn,upper(value))


	
}

const print = function (...values){console.log(...values)};

let word = "     heLLO wORLD!!   "; 
let name = " hersy helston third";
let user = "asheley";

arrange(word,print);
print(arrange(name));
arrange(user,print);
let x = callable(null, "Nice World");
print(x);
let y = callable(null,["this", "world"].join(" "));
print(y);