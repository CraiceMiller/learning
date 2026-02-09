package com.restaurant.people;
import com.restaurant.food.Meal;
import com.restaurant.food.Menu;
import com.restaurant.food.containers.Usable;

public class Customer extends Person {
    //private final int MAX_RATE =10;
    private int happinessRate = 5;
    public String order;
    
    public Customer(String name,int age, Gender gender) {
        super(name,age,gender);
    }

    private void eatTheMeal(Usable u ){
        if(u==null){
            System.out.println("There is nothing to eat :(");
            this.happinessRate--;
            return;
        }
        if(u.isEmpty()){
            System.out.println("The content is empty :(");
            this.happinessRate--;
            return;
        }
        u.use();
        this.happinessRate++;
    }
    
    public void eat(Meal meal){
        if(meal==null){
            System.out.println("no food >:(!!");
            this.happinessRate -=3;
            return;
        }

        meal.getAllMeal().forEach(value->{
            this.eatTheMeal(value);
        } );
    }

    public boolean isHappy(){return this.happinessRate >=5;}
}
