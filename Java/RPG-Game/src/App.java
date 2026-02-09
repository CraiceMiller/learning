/**
 * @start 12-01-2026
 */

 //This is the same library in python "tkinter" :)
import javax.swing.JFrame;

import main.GamePanel;



public class App {
    public static void main(String[] args) throws Exception {
        //Settings the properties 
        JFrame window = new JFrame();
        GamePanel gamePanel = new GamePanel();
        
         

        //Settings the window configuration

        window.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        window.setResizable(false); 
        window.setTitle("RPG Games!");

        // 1. ADD the panel first
        window.add(gamePanel); 
       


        // 2. PACK the window (this calculates the sizes)
        window.pack();

        // 3. Set location and visibility LAST
        window.setLocationRelativeTo(null);
        window.setVisible(true);

        System.out.println("The game has started"); 
        // 4. Start the heart of the game
        gamePanel.startThreadGame();

        System.out.println("The game has end !!!");
    }
}
