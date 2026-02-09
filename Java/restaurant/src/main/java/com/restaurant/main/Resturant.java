package com.restaurant.main;

import com.restaurant.people.*;
import com.restaurant.food.*;
import com.restaurant.food.dishes.*;
import com.restaurant.food.drinks.*;
import static com.restaurant.people.Person.Gender;

import java.util.Scanner;

public class Resturant {
    private Chef chef = new Chef("Scotley Slowik",39,Gender.MALE);
    private Waitress waitress = new Waitress("Jhon Miller",28,Gender.MALE);
    private Customer customer;
    private String currentOrder;

    //TODO:fix how can i add plates,and let the chef kwno what kind of food is 
    public Resturant(){
        //Menu.setDish("ramen", Ramen);
    }


    public void askSomethingToEat(){
        Scanner scanner = new Scanner(System.in);

        if(this.customer==null){
            System.out.println("No customer!!");
            return;
        }
        Menu.displayDishes();
        String dishOrder = scanner.next();
        customer.order = dishOrder;
        this.chef.

        Menu.displayDrinks();
        String drinkOrder = scanner.next();


        scanner.close();
    }


}
