package com.desktop.technology.computer;


/**this will only storage the key evetn code and the action nothing more :) */
public class Key {
    public static enum KEYS_TO_PRESS {
        A,S,D,F,G,H,J,K,L;
    }
    

    private int currentKey;
    private ActionHandler.ACTION currentAction;
    private ActionHandler actionH = new ActionHandler();
   
    public Key(int k,ActionHandler.ACTION action){
        this.currentKey  = k;
        this.currentAction = action;
    }

    /**only do the acton*/
    public void press()
    {
        
        
        switch (this.currentAction) {
            case JUMP:this.actionH.jump();break;
            case RUN:this.actionH.run();break;
            case SIT:this.actionH.sit();break;
            case SLEEP:this.actionH.sit();break;
            case WALK:this.actionH.walk();break;
            case WATCH:this.actionH.watch();break;
            default: break;
        }

        


    }
    
    /**only retrive the action */
    public ActionHandler.ACTION  getAction(){
        return this.currentAction;
    }
   
    public int getActionCode(){
        return this.currentKey;
    }

}
