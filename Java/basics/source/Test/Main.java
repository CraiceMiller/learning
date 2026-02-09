package Test; 
import models.Item;
import models.Inventory;


public class Main  {
    public static void main(String[] args) {
        Item hammer = new Item("Hammer",2);
        Inventory myInventory = new Inventory(); 
        myInventory.addItem(hammer);
        myInventory.displayItems();
        
        System.out.println("The main method have been end!\n "+myInventory.amount);
    }
}
