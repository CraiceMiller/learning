package animals;

public class Duck extends Animal {
    public Duck(String name){
        super(name);
    }

    @Override
    void makeSound() {
        // TODO Auto-generated method stub
        if(this.isSleeping){
            System.out.println(this.SLEEPING_MESSAGE);
            return ;
        }
        System.out.println(this.name + " says: Cuack!" ); 
    }

}
