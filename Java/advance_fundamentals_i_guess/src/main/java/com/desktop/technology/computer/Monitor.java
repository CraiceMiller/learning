package com.desktop.technology.computer;


import javax.swing.JPanel;
import javax.swing.JFrame;
import java.awt.Dimension ; 
import java.awt.Color;
import java.awt.event.KeyEvent; 

//here i am using composition i guess ?
public class Monitor {
    //normal propeties here 
    private boolean isActive = false;

    //this is composition i guess
    private Dimension dimension;
    private Color color = Color.WHITE;
    private JFrame window = new JFrame();
    private String monitorName = "My Pc :3";
    private JPanel panel = new JPanel();

    private KeyBoard keyBoard = new KeyBoard(
        new Key(KeyEvent.VK_A, ActionHandler.ACTION.JUMP),
        new Key(KeyEvent.VK_S, ActionHandler.ACTION.SIT),
        new Key(KeyEvent.VK_W, ActionHandler.ACTION.SLEEP),
        new Key(KeyEvent.VK_D, ActionHandler.ACTION.RUN)
    );
    
    public Monitor(int high,int width )
    {
        this.changeDimension(high, width);
        //panel config
        this.panel.setPreferredSize(this.dimension);
        this.panel.setBackground(this.color);
        this.panel.setDoubleBuffered(true);
        this.panel.setFocusable(true);
        

        //window seetings 
        this.window.setDefaultCloseOperation( JFrame.EXIT_ON_CLOSE);
        this.window.setTitle(this.monitorName);
        
        this.window.addKeyListener(this.keyBoard);
        this.window.setLocationRelativeTo(null);
        this.window.add(this.panel);
        this.window.pack();
    }

    public void changeDimension(int high, int width)
    {
        this.dimension = new Dimension(high,width);
    }

    public void changePanel(JPanel p){
        this.panel = p;
    }

    public void changeMonitorName(){

    }

    public void turnOn()
    {
        this.window.setVisible(true);
        this.window.pack();
        this.isActive = true;
    }
    public void turnOff()
    {
        this.window.setVisible(false);
        this.isActive = false;
    }
}
