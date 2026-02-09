package com.restaurant.people;
import com.restaurant.food.Meal;
//This one is association, due it does not owns nothing, only iteractive with 
//others objects
public class Waitress extends Person {
    private Meal currentMeal;

    public Waitress(String name,int age, Gender gender) {
        super(name,age,gender);
    }

    /**
     * this is my solution to talk with two differents objeccts
     * @param chef
     */
    public void recieveFood(Chef chef){
        if(!chef.isReady())return;
        this.setMeal(chef.giveMeal());
    }

    public void server(Customer customer){
        customer.eat(this.currentMeal);
    }
    public void setMeal(Meal meal){
        this.currentMeal = meal;
    }

}
