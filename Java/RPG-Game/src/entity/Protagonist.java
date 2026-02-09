package entity;

import java.awt.Graphics;

import main.GamePanel;
import main.KeyHandler;



public class Protagonist extends Entity{
    protected GamePanel gamePanel; 
    public final KeyHandler keyH ; 

    
    public Protagonist(GamePanel gamePanel, KeyHandler keyH )
    {
        this.gamePanel = gamePanel; 
        this.keyH = keyH;
    }
    
    /**
     * update the info such as chracter position.
     * This one of our main method that will be called the the run() method... 
     * # the Change 
     * with this method we only adding or subtrading our X or Y axes. based
     * on  the current key pressed. Since the right-top corner is X=0, Y=0. we
     * can easily move our object based on our axis. 
     * for instance if the user type up (key W), the axis Y will be subtract by one 1.
     * if it press down (key S) 10 times, it will be added by 10. so easy.
     * 
     * Now what happed if our axis  reach zero , this mean, it arrived to a corner
     * 
     */
    public void update()
    {


        if(this.keyH.upPressed == true)
        {
            if (this.y >=0)
            {
                this.y -= this.speed;
            } 
        }
        else if(this.keyH.downPressed == true)
        {
            this.y += this.speed; 
        }
        else if (this.keyH.rightPressed == true)
        {
            this.x += this.speed; 
        }
        else if (this.keyH.leftPressed == true)
        {
            this.x -= this.speed; 
        }

    }

    public void paintComponent( Graphics g2)
    {
        //Setting the color of our sqaure
        g2.setColor(this.color);
        //The size, the width , and the height
        g2.fillRect(this.x,this.y,this.gamePanel.tileSize,this.gamePanel.tileSize  );
        g2.dispose();
    }
    

}
