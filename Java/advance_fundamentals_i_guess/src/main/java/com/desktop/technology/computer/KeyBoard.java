package com.desktop.technology.computer;


import java.awt.event.KeyEvent; 
import java.awt.event.KeyListener; 
import java.util.Map;
import java.util.HashMap;


//using agreagation i guess , due my keyboard is using severals keys
//or is it composition, due it using the keys as part of its data, property
public class KeyBoard implements KeyListener{

    private Map<String,Key> keys = new HashMap<String,Key>();
    
    

    public KeyBoard(Key f, Key s, Key t, Key fourth)
    {
        this.keys.put("first-key", f);
        this.keys.put("second-key", s);
        this.keys.put("third-key", t);
        this.keys.put("fourth-key", fourth);
        
    }

    //for now i will only use this :3
   
    public void keyPressed(KeyEvent e) {
        try {
            int code = e.getKeyCode();
            
            //i know i know, this is very, very bad. but at least, it works :3
           this.keys.forEach((key,value)->{
            if(value.getActionCode() ==code)
                {
                    value.press();
                }
            } );

        }
        catch(Exception ex)
        {
            System.err.println(ex);
        }
        
    }

    public void keyReleased(KeyEvent e) {
        
    }
    public void keyTyped(KeyEvent e) {
        
    }
   

}
