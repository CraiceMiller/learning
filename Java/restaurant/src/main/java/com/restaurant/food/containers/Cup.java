package com.restaurant.food.containers;
import com.restaurant.food.drinks.Drinkable;
public class Cup implements Usable {
    private Drinkable content;
    private String name;

  
    public void use(){
        if(content == null){
            System.out.println("There is nothing to drink:(");
            return;
        }
        this.content.drink();
    }

    public void fill(Drinkable d){
        this.content = d;
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
