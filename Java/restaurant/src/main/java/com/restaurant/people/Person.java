package com.restaurant.people;

public abstract class Person {
    protected String name; 
    protected int age;
    protected Gender gender;
    protected boolean hasHungry =false; 
    protected boolean isSleepy = false;
    public static enum Gender{FEMALE,MALE;}

    public Person(String name,int age,Gender gender){
        this.name = name; 
        this.age = age; 
        this.gender = gender;
    }
    public void sleep(){
        System.out.println(this.name+" is sleeping...");
    }

}
