package models; 

import java.util.ArrayList; 

/**
 * This will handle and storage all the itme given to it
 * start: 1-1-2026 at 11:11
 */
public class Inventory {

    //without acces modified, visible
    String message = "Hello :3";
    //public acces, visible
    public int amount = 0;
    //private acces, invisible 
    private ArrayList<Item> itemsList;
    //protected acces, visible
    protected String pro = "This is just a value to work with "; 
    
    public Inventory(){
        this.itemsList = new ArrayList();
    }
    /**
     * This method will only add one single item into the invetory list
     * @param item The item to storage 
     * @@return void 
     */
    public void addItem(Item item){
        this.itemsList.add(item);
    }
    public void displayItems(){
        System.out.println(this.itemsList.toString());
        this.itemsList.forEach(value->
        System.out.println(value.toString())
        );
    }
}
