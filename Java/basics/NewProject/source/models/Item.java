package models;

/**
 * An overal Class to create several kinks of object. eg. swords hammer, so on.
 */
public class Item {
    private String name;
    private int quantity;

    public  Item(String name, int quantity) {
        this.name =name;
        this.quantity= quantity;
    }

    public String getName(){
        return this.name;
    }
    public int getQuantity(){
        return this.quantity;
    }

}
