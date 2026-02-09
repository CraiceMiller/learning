package com.restaurant.food;
import com.restaurant.food.containers.*;
import java.util.ArrayList;

public class Meal {
    public Cup cup;
    public Dish dish;
    private ArrayList<Usable> allTheMeal = new ArrayList<Usable>();

    public ArrayList<Usable> getAllMeal(){
        this.allTheMeal.add(cup);
        this.allTheMeal.add(dish);
        return this.allTheMeal;
    }
    


}
