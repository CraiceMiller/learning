
/**
 * a very simple project where i put in practice everything i learn regards to OOP
 * a simple Konosuba rpg game
 */
import character.Hero;
import character.Mage;
/**
  To learn: 
  native
    strictfp
    synchronized
    enum
    Record 
    Annotation 
    java.utils

   
 
 */


//Composition over inherentance
public class App {
    

    
    public static void main(String[] args) throws Exception {
        Mage megumin = new Mage( "Megumin",17,2) ;
        Hero kazuma = new Hero("Kazuma",18,3);
       


    
        Game game = new Game();
        game.setCharacter(kazuma);
        game.run(megumin);
        System.out.println("And Kazum steal Megumin's panties"); 
        System.out.println("Megumin: Give my panties back!!!");


        System.out.println("Finished the program :3"); 

    }
}
