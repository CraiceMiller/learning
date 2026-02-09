
/**
 * With this class i tried to use Polymoriphsom, since it's where differents 
 * objects share sames properties or methods...
 */

import character.Character;
import exceptions.CharacterException;


public class Game {
    private Character currentCharacter; 
    public void setCharacter(Character c){
        this.currentCharacter = c; 
    }

    public void run( Character rival ){
        Character c = this.currentCharacter;

        try{
            System.out.println(c.getName() + " the " + c.type() + " is attacking " + rival.getName() );
            this.currentCharacter.attack(rival);
        }
        catch(CharacterException e)
        {
            System.out.println(e);
        }
        finally {
            c.displayStadisctics();
            rival.displayStadisctics();
        }
    }
}
