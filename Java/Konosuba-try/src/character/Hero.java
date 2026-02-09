package character;

import exceptions.CharacterException;

public class Hero extends Character{
    public Hero(String name,int age,int currentLevel) {
        super(name,age,currentLevel);
    }

   
    @Override
    public void specialAttack(Character rival) throws CharacterException {
          
    }

    @Override
    public String type() {
        return "Hero" ;
    }

}
