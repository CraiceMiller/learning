package com.restaurant.people;
import com.restaurant.food.Meal;
import com.restaurant.food.containers.*;
import com.restaurant.warehouse.*;


public class Chef extends Person {
    private boolean mealIsReady = false;
    private Meal meal;
    public Chef(String name,int age, Gender gender) {
        super(name,age,gender);
    }

    //TODO:complete this
    public void cook(){
        Meal newMeal = null;


        //everything is done
        this.mealIsReady = true;
        this.meal = newMeal;
    }


    protected boolean isReady(){
        return this.mealIsReady;
    }

    public Meal giveMeal(){return this.meal;}

}
