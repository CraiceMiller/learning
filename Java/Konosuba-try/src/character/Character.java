/**
 1. Abstraction: is where we hide certain data from the outsideword 
 it could be reache from abstract methods and interfaces. Abstrac class Character
 where belong to a certain group

 2. Encaplutaion: when i have fully control of the data,propeties, at hand. meaing only me
 can chage the data

 3.Compostion: where i use other classes to create a "has a" relaticon. 
 here character has an invertory.

 Notes:
 what i learn within this 8 months is every properties must fullfil only one single
 responsability; likewise in methods, or function, must only do one single thing. 
 */
package character;

import exceptions.CharacterException;
import models.IBasics;
import models.Inventory;
import models.MathHelper;

//1.
/**
 * An abstract class where storge all the meaniful data of every character
 */
public abstract class Character implements IBasics {
    //TODO PROPETIES
    //2.
    protected String name;
    private int age;

    private int maxLevel = 10;
    private int minLevel = 0;
    protected int currentLevel;
    protected double experience = 0;

    private double minHealth = 0; 
    private double maxHealth = 50;
    protected double health = 10;

    protected boolean isAlive = true;

    protected double attackPower = 3;
    protected double defendsLevel = 0; 

    //3.
    protected final Inventory inventory = new Inventory();
    protected static final MathHelper math = new MathHelper();



    //TODO CONCRETE METHODS THAT WILL BE INHERETANCE
    protected Character(String name,int age,int currentLevel){
        this.name = name;
        this.currentLevel = currentLevel;
        try{
            this.changeAge(age);
        }catch (CharacterException e){
            this.age = 18;
        }
    }

    /**Just a simple function that change the current age of the character */
    protected void changeAge(int newAge)throws CharacterException 
    {
        if(newAge <=0){throw new CharacterException("The character age must be greate than zero!"); }
        this.age = newAge;
    }

    /**just increased the current level by one
     * it does  nothing if the current experienc it is below by 100
    */
    protected void increasedLevel(){
        if(this.experience < 100){return ;}
        System.out.println(this.name + " level up!!" );
        this.currentLevel++;
    }

    protected void increaseHealth(double amount){
        this.health += amount;
    }

    protected void increaseExperience(Character rival){

        this.experience += 0; 
    }

    public void displayStadisctics(){
        System.out.println("Name: " + this.name); 
        System.out.println("Health: " + this.health);

    }

    private void reciveAttack( double attackPower){
        double finalAttack = attackPower - this.defendsLevel;
        this.health -= finalAttack; 
        if (this.health <=0){
            this.isAlive = false;
        }
    }

    public  void attack(Character rival )throws CharacterException{
        //TODO think in a better way to calculate the experience
        rival.reciveAttack(this.attackPower);
        double experienceAdquire = this.math.increaseExperience(this.attackPower);
        this.experience += experienceAdquire;
    }


    //TODO ABSTRACT METHODS
    /**A very simple method that make this current character attack 
     *another character. 
     It must increase the experience every time the character defeat the enemy
     *@param rival who will attack
     @throws CharacterException if the character is not alive or another fact is happening;
     */
    public abstract void specialAttack(Character rival )throws CharacterException;


    //TODO OVERRIDE METHODS IMPLEMENT BY THE INTERFACE
    //overidde
    @Override
    public String getName() {
        return this.name;
    }
    @Override
    public double getCurrentHealth() {
        return this.health;
    }

}
