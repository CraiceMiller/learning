//12/09/2025

//I guess this is call a callback
function myoperation(a,b,operation) {
    return operation(a,b)
};
function sum(a,b) {
    return a + b
    
};
function subtracion(a,b) {
    return a - b
    
};
function multiplication(a,b) {
    return a * b
    
};
function division(a,b){
    if (b == 0){
        return 0
    }
    return a / b
};
function power(a,b) {
    return a ** b
    
};

let result;
result=myoperation(10,2,power);
result +=2;

//I dont know waht is this
result ++;
result ++;


console.log(`The result is: ${result}`);



