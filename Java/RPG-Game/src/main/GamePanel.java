package main;

import java.awt.Dimension;
import java.awt.Graphics;
import java.awt.Graphics2D;

import javax.swing.JPanel;

import entity.Protagonist;

import entity.Protagonist;


/**
 * A class that handle the UI at hand. in short it is the html...
 * 1.With this one i am using the Inherentance due its father is JPanel
 * the JFrmae only create the window... The JPanel create the paper, canvas or the 
 * place where i can put all my things. 
 * 
 * #The Runnable interface
 * i guess , we must use this interface whenever we need to use threads. in this gamePanel 
 * we indeed using a thread ...
 * 
 * @since 12-01-2026, Monday, 13:00 - 17:00hrs 
 * @update 13-01-2026 Tuesday 10:00hrs - 15:00hrs
 */
public class GamePanel extends JPanel implements Runnable
{
    /**2. Encapsulation all the data only "Me " can change them */
    //  SCREEN SETTINGS
    /**This is the same as the HTML root size... In other words the main size messuare*/
    private final int originaltileSize = 16;
    /**scale is the data that let us change the size of different object easily */
    private final int scale = 2;

    /**it is the size of the square */
    public final int tileSize =  originaltileSize * scale;
    /**this one will set the max of columns we want */
    private final int maxScreenCol = 16; 
    /**this one will set the max of rows we want */
    private final int maxScreenRow = 12; 
    /**with the comination of the columns and the tileSize it gives us the Width size */
    private final int screenWidth = tileSize * maxScreenCol;
    /**with the comination of the rows and the tileSize it gives us the Height size */
    private final int screenHeight = tileSize *maxScreenRow;
    /**The frame per seconds; How many time the square will be paint for every second */
    private final double FPS = 60;

 

    /**3. This is Constructions, we are using "Another" class to work. My "GamePanel" has a  "Dimension"*/

    /**This object let us  */
    private final Dimension dimension = new Dimension(this.screenWidth, this.screenHeight);
    /**It create something you can start and stop. it keep the program running until the program sttoped*/
    private Thread gameThread ;
    /**This object will help us to handle all the keyboard events*/
    private KeyHandler keyH = new KeyHandler(); 
    /** */
    private Protagonist protagonist = new Protagonist(this,keyH); 


    //This is call whenever i create a new object, GamePanel game = new GamePanel(); 
    //it inizitiale our game
    public GamePanel()
    {
        //Settinty the UI configuration
        this.setPreferredSize(this.dimension);
        this.setBackground(Config.BACKGROUND_COLOR);
        this.setDoubleBuffered(true);
        this.addKeyListener(this.protagonist.keyH);
        this.setFocusable(true);
    }

    //TODO: ask if this method is call automatly
    /**
     *I dunno when this method is called :(

     However i do know what it does, it only draw, create, a simple square, and that
     pretty much it...
     */
    @Override
    public void paintComponent( Graphics g)
    {
        //i dunno what it does :( 
        super.paintComponent(g);
        Graphics2D g2 = (Graphics2D) g;
        this.protagonist.paintComponent(g2);
        //in simple terms, this will clean all this
        g2.dispose();
    }




    /** 
     * For me, we need to call manually this method due we need to init our thread. 
     * but what is the purpose of this thread anyways. i already know that threads are several 
     * methods running at the same time to save time and be more effiecient or the large task 
     * 
     * 
    */
    public void startThreadGame()
    {
        this.gameThread = new Thread(this);
        this.gameThread.start();
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
    private void update()
    {
        this.protagonist.update();
    }

    //creating the methods
/** 
    @Override
    public void run() 
    {
        //using the sleep method
        
        double drawInterval = 1000000000/this.FPS; 
        double nextDrawTime = System.nanoTime() + drawInterval; 

        while ( this.gameThread != null)
        {
            
            //Updating our square
            this.update();
            this.repaint();

            //
            try 
            {
                double remainingTime = (nextDrawTime - System.nanoTime()) / 1000000 ;
                
                //verifying if the number is less than zero, to prevent any negative number
                if(remainingTime < 0)
                {
                    remainingTime = 0; 
                }

                Thread.sleep((long) remainingTime );
                nextDrawTime += drawInterval;
                
            } 
            catch (InterruptedException e) 
            {
                e.printStackTrace();
                
            }

        }
        
        
    }

*/
    

 

    /**
     * This is one of our method tha we implement due our "Runnable interface"
     * I dunno when this it call
     * 
     * And this is where all the logic is connected togther. and create the game loop. 
     * Fothermore, in game developer there are two main techines to use it. 
     * this is  one of them. But i dunno what is going on here :( 
     * # delta
     * it is the 
     * 
     */
    public void run() 
    {
        /**The amount of seconds I want  */
        long seconds = 1_000_000_000 ;
        /**The period of seconds we want to wait to draw the next pixel */
        double drawInterval = seconds /this.FPS; // 1000000000 / 60 = 16,666,666.666667
        /**the most important variable; 
         * the min value is 1;
         * i've noticed that not every loop the delta will be 1, it must happen a few
         * loops to delta reach 1. 
         * but what is its purpose anyways ?
         */
        double delta = 0;
        /**we use this value to have a reference of the last time, is a holder
         * we have 5 frames
         * the lastTime was 3000 or so
         * and current is 6000. 
         * and ends the loop. then the current time is forgotten. but the lasTime 
         * remember it to the next operation
         * 
         */
        long lastTime = System.nanoTime(); //if this 901675774953300
 
        /**Only storage the current time in nanoseconds */
        long currentTime = 0;
        /**the max value is 1 */
        long timer = 0;
        /**the max value is 1 */
        int drawCount = 0;
        /**it calculate the period of time pass betewn the current and the last time  */
        long operation ;

        while ( this.gameThread != null)
        {
           
            
            
            currentTime = System.nanoTime(); // and then this 901675780404000
    
            /**the operation would be : 901675774953300 - 901675780404000 = 5450700 */
            operation = currentTime - lastTime ; // 5450700

            delta += operation / drawInterval; //this would be 5450700 / 16,666,666.666667 = 0.327042

            timer += operation ;//this would be 0 + 5450700 = 5450700

            lastTime = currentTime; //this would be901675780404000


            //0.327042 >= 1 ?
            if (delta >=1)
            {
                //then update the square and repaint it
                this.update();
                this.repaint();
                //1.327042 - 1 = 0.327042
                delta--;
                // 0 + 1 = 1
                drawCount++; 
            }

            /**
             * last Time: 903855851344100
                Current Time: 903855851344100
                Delta: 1.8000005640006478E-5
                Operation: 400
                Current Timer: 1000000300
                Current  FPS: 60
                            */
            

            // 5450700 >= 1_000_000_000 ?
            if(timer >= seconds)
            {
                System.out.println("last Time: "+ lastTime);
                System.out.println("Current Time: "+ currentTime);
                System.out.println("Delta: "+  delta);
                System.out.println("Operation: "+  operation);
                System.out.println("Current Timer: "+ timer);
                System.out.println("Current  FPS: "+ drawCount);
                drawCount = 0;
                timer = 0; 
            }
            
        }
        //this is my lame attempt, i know i guess i misundertood several things, but what are they anyways ? 
        
    }


}
//why it is so complicated it, i literally created only four methods and i have been find it increadibly hard :(, what is wrong with me ...
