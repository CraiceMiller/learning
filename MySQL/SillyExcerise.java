import java.util.HashMap;

/**
 * my uml structure attempt
 * intefaces:
    - attacktable 
    alivale
    ieffect 

    structure: 
    Kazuma,Megumin,Slime --composition -<> Main
    ieffect --- realisation --> EXPLOSION 
    ieffect -- aggregation -- > attack 
    attack --- composition -- > megumin
    attackable , alivable -- relisation --> slime
    attack -- dependecy ---> HashMap,MathHelper
    Kazuma -- association -- Megumin
    ieffect -- association -- attackble 


    and that pretty much it
 */

class MathHelper{
    public static int random(int min, int max){
        return (int)(Math.random() * (max - min + 1)) + min;
    }
    /**
     * this is based on the formula "deried outcome = number of outcomes / total number of automes"
     * i guess i need i litle help here :( 
     * @return
     */
    public static boolean calculateProbability(double probability ){
        return  Math.random() <= probability ;

    }
}

// Custom Exception now has a message constructor
class MeguminTiredException extends Exception {
    public MeguminTiredException(String message) {
        super(message);
    }
}

interface Attackble{
    abstract void reciveAttack(IEffect[] damage);
}
interface Alivable {
    abstract boolean isAlive();
    abstract double getLife();
    abstract void changeLife(double amount);
}

interface IEffect{
    abstract void applyEffect(Alivable enemy);
}
class Attack {
    private final int staminaAmount; 
    private final String name;
    private double probability;
    private IEffect[] effects;

    public Attack(String name,int stamina,double probability, IEffect[] effects){
        this.name = name; 
        this.staminaAmount= stamina;
        this.probability = probability;
        this.effects = effects;
    }

    public void attack(Attackble enemy)
    {
        

        if(!MathHelper.calculateProbability(this.probability)){
            System.out.println("The attack was miss!!");
            return ;
        }
        enemy.reciveAttack(this.effects);
    }

    /**the amount of statima needed to use this attack  */
    public int getStamina(){return this.staminaAmount;}
    public String getName(){return this.name;}
   
}





class Slime implements Attackble,Alivable {

    private double life = 100;
    private String name = "Slime";
    private Attack simple = new Attack("Attack",15,0.70,new IEffect[]{new Damage(23)}  );

    @Override
    public void reciveAttack(IEffect[] damage) {
        for(IEffect effect:damage){
            effect.applyEffect(this);
        }
    }
    @Override
    public double getLife() {
        return this.life;
    }
    @Override
    public void changeLife(double amount) {
       
        if (amount <0){
            System.out.println("cannot give negative number ");
            return ;
        }
        this.life += amount; 
        if(life <0)this.life=0;
        
    }
    @Override
    public boolean isAlive() {
        return this.life >0;
    }
    public String getName(){return this.name;}

}

class Damage implements IEffect
{
    private double damage; 
    public Damage(double damage){
        this.damage= damage;
    }
    @Override
    public void applyEffect(Alivable enemy) {
        enemy.changeLife(-this.damage);
    }
}

class EXPLOSION implements IEffect  {
    private final int staminaAmount =100 ; 
    private int damageAttack;
    

    public EXPLOSION(int damage){
        this.damageAttack = damage;
    }

    @Override
    public void applyEffect(Alivable enemy) {
        System.out.println("the enemy was damage... ");
        enemy.changeLife(  -this.damageAttack );
    }

}
/**
 * since 2026-01-31
 */
public class SillyExcerise {
    public static void main(String[] args) {
        Megumin megumin = new Megumin();
        Kazuma kazuma = new Kazuma();
        Slime slime = new Slime();
        
        if (!megumin.pantsu) {
            System.out.println("Give my panties back kazuma!!!");
        }

        while (megumin.stamina > 0) {
            try {
                megumin.castSpell("EXPLOSION",slime);
                kazuma.giveAPiggyRideBackToMeguminLaterToSpell(megumin);
            } catch (MeguminTiredException e) {
                e.printStackTrace();
                break;
            }
        }
        System.out.println("Kazuma: Watch out, there it a slime ");

        try {
            megumin.castSpell("EXPLOSION",slime);
        } catch (MeguminTiredException e) {
            e.printStackTrace();
        }

        if(slime.getLife() >0){
            System.out.println("what, that this is still alive!!!!, quick megumin do something");
            System.out.println( "i cant kazuma jerk!1!");

        }
    }
}

class Megumin {
    public boolean pantsu = false;
    public String name = "Megumin";
    public int stamina = 100;

    
    public HashMap<String,Attack> spells = new HashMap<String,Attack>() ;

    public Megumin(){
        this.spells.put("EXPLOSION",
        new Attack("EXPLOSION", 100, 0.10, new IEffect[]{ new  EXPLOSION(100) })

        );
    }

    private void doAttack(String spellName,Attackble enemy) throws MeguminTiredException {
        if (this.stamina <= 0) {
            throw new MeguminTiredException("oh no, megumin is so tired right now :o");
        }
         
        

        Attack spell  = this.spells.get(spellName);
        if(spell == null){
            System.out.println("That spell does not exist");
            return ;
        }

        if (this.stamina < spell.getStamina()) {
            throw new MeguminTiredException("Not enough stamina");
        }
        
        
        if(enemy == null){
             System.out.println(this.name + " casts " + spellName + "!!!");
        }

        else{
            spell.attack(enemy);
        }

       
        
        this.stamina -= spell.getStamina();

        if (this.stamina <= 0) {
            System.out.println(this.name + " has collapsed!");
        }

    }

    public void castSpell(String spellName) throws MeguminTiredException {
        this.doAttack(spellName,null);
    }

    public void castSpell(String spellName,Attackble enemy) throws MeguminTiredException {
        this.doAttack(spellName,enemy);
    }
}

class Kazuma {
    public String name = "Kazuma";
    public boolean isAMoron = true; 
    public boolean hasEqualGenderTreat = true; 
    public boolean isInMoodToday = true; 

    public void giveAPiggyRideBackToMeguminLaterToSpell(Megumin megumin) {
        if (!this.isInMoodToday) {
            System.out.println("omg, what the heck your problem, im not going to do such a thing like that!!!");
            return;
        }
        System.out.println(this.name + " is giving a lift to " + megumin.name);
    }
}
