package com.restaurant.food;
import java.util.HashMap;
import  com.restaurant.food.dishes.Eateable;
import  com.restaurant.food.drinks.Drinkable;


public class Menu {

   
    private static HashMap<String,Eateable> dishesList = new HashMap<String,Eateable>();
    private static  HashMap<String,Drinkable> drinkList = new HashMap<String,Drinkable>();



    public static void displayDishes(){
        
        System.out.println("---------Dishes--------------");
        for(String v:Menu.dishesList.keySet()){
            System.out.println("-> "+v);
        }
    }

    public static void displayDrinks(){
        System.out.println("---------Drink--------------");
        for(String v:Menu.drinkList.keySet()){
            System.out.println("-> "+v);
        }
    }

    public static void setDish(String name,Drinkable value){
        Menu.drinkList.put(name,value);
    }
    
    public static void setDrink(String name,Eateable value){
        Menu.dishesList.put(name,value);
    }

    public static Eateable getDishOrder(String order){
        Eateable result = Menu.dishesList.get(order);
        return result;
    }

    public static Drinkable getDrinkOrder(String order){
        Drinkable result = Menu.drinkList.get(order);
        return result;
    }


}
