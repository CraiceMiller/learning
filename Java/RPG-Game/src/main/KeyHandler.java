package main;

import java.awt.event.KeyEvent;
import  java.awt.event.KeyListener; 

public class KeyHandler implements KeyListener {
    public boolean upPressed, downPressed, leftPressed, rightPressed; 

    private void keyHelper(KeyEvent e, boolean isPressed )
    {
        int code = e.getKeyCode();
        if (code == KeyEvent.VK_W){
            this.upPressed = isPressed;
        }
        if ( code == KeyEvent.VK_S ){
            this.downPressed = isPressed;
        }
        if ( code == KeyEvent.VK_A ){
            this.leftPressed = isPressed;
        }
        if ( code == KeyEvent.VK_D ){
            this.rightPressed = isPressed;
        }
       
    }
    @Override
    public void keyTyped(KeyEvent e) {

    }

    @Override
    public void keyPressed(KeyEvent e) {
        this.keyHelper(e, true);
    }
    @Override
    public void keyReleased(KeyEvent e) {
        this.keyHelper(e, false);
    }

}
