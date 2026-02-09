package com.desktop.items;

public class Cup implements IConsumible 
{
    //meaning the person can only drink 5 times
    private final int MAX_AMOUNT_OF_FILL = 5;

    
    protected IDrinkable currentContent;
    protected int amount = 0;

    public void fill() {
        if(this.amount ==this.MAX_AMOUNT_OF_FILL)
        {
            System.out.println("the cup has been backfill. oh no!. you have statin the floor!");
            return;
        }
        
        this.amount++;
        System.out.println("You have fill the cup");
    }

    public void fillAll(){
        for(int times = this.amount;times <= this.MAX_AMOUNT_OF_FILL;times++){
            this.fill();
        }
    }

    public void use() {
        if(this.currentContent == null){
            System.out.println("The cup is empty");
            return;
        }
        

        System.out.println("You have drank");
        this.amount--;
        if(this.isEmpty()){
            this.currentContent = null;
        }
    }
    
    public void setContent(IDrinkable c){
        this.currentContent = c;
    }


    public int seeAmountOfContent(){return this.amount;}
    public boolean isEmpty() {return this.amount <=0 || this.currentContent == null;}
}
