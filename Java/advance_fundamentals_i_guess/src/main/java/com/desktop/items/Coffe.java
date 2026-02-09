package com.desktop.items;

//with this i can say "a cup of coffe"
public class Coffe implements IDrinkable {
    public static enum Type{
        LATTE(60),AMERICANO(75) ,BLACK(20);
        private final int value;
        Type(int v){
            this.value = v;
        }
        int getValue(){return this.value;}
    }
    private Type currentType;
    private int amountOfCaffeine;

    public Coffe(Type type){
        this.currentType = type;
        this.amountOfCaffeine = type.getValue();
    }
    public Type getType(){return this.currentType;}
    public int getCaffeine(){return this.amountOfCaffeine;}

}
