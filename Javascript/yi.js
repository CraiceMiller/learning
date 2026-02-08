function* numbers(){
let i = 0; 
    while (true){
        yield i
        i++;
    }
}



function* name(){
yield "hello World";
return null;
}

const nums = numbers();
const na = name();
console.log(nums.next().value);console.log(nums.return());
console.log(na.next());console.log(na.next());
console.log(nums);
console.log(na);