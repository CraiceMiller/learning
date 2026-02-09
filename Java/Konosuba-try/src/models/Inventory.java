package models;

import java.util.ArrayList;

import items.Item;

/**this is where you can storage all your items :3 */
public class Inventory {
    private ArrayList<Item> items = new  ArrayList<Item>();

    public void addItem(Item item)
    {
        this.items.add(item);
    }

    /**Just print the whole list of item */
    public void displayItems()
    {
        for (Item i:this.items)
        {
            System.out.println(i.toString());
        }
    }

}
