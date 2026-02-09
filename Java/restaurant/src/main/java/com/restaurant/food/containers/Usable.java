package com.restaurant.food.containers;

public interface Usable {
    abstract void use();
    abstract boolean isEmpty();
    abstract void setMealName(String name);
    abstract String getMealName();


}
