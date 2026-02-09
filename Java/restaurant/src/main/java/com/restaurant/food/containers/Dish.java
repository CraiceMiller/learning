package com.restaurant.food.containers;
import com.restaurant.food.dishes.Eateable;
public class Dish implements  Usable {

    private Eateable content;
    private String name;
   
    public void use() {
        if(content == null){
            System.out.println("There is nothing to eat:(");
            return;
        }
        this.content.eat();
    }

    public boolean isEmpty() {
        return this.content == null ;
    }
    @Override
    public String getMealName() {
        return this.name;
    }
    @Override
    public void setMealName(String name) {
        this.name= name;
    }

}
