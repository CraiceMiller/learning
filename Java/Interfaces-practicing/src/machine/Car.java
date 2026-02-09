package machine;

//TODO how can i extends and implement at the same time ? 
//is very easyyyyyy, using the combination of "inheretnace" and "compostion" definition 

//firt the inherentance 
public class Car extends Vehicule
{
    //then we use the composition
    GPS gps = new GPS();

}
//a car is a vehicule and has a gps