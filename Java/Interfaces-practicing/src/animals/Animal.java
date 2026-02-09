package animals; 

abstract class Animal {
    protected String name;
    protected boolean isSleeping = false; 
    protected  final String SLEEPING_MESSAGE = "This animal is slepping, shh"; 

    public Animal(String name){
        this.name = name; 
    }

    /**sleep the animal  */
    public  void sleep(){
        if(this.isSleeping){
            System.out.println(this.SLEEPING_MESSAGE);

        }

        this.isSleeping = true; 
        System.out.println("This animal start to sleep!!");
    }

    /**wake up the animal */
    public void wakeUp(){
        if(this.isSleeping){
            System.out.println("This animal is already slepping, shh");

        }

        this.isSleeping = true; 
        System.out.println("This animal start to sleep!!");
    }

    abstract void makeSound();

    //Setter
    public String getName(){
        return this.name;
    }
    //getter
    public void setName(String newName){
        String oldName = this.name; 
        this.name = newName; 
        System.out.println(oldName+" Change name to " + newName);
    }


}
