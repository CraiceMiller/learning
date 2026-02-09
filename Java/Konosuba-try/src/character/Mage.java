package character;

import exceptions.CharacterException;

public class Mage extends Character{
    public Mage(String name,int age,int currentLevel) {
        super(name,age,currentLevel);
    }

   
    @Override
    public void specialAttack(Character rival) throws CharacterException {
        
    }
    @Override
    public String type() {
        // TODO Auto-generated method stub
        return "Mage";
    }
    

}
