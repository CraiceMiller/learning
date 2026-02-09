package com.desktop.technology.computer;


public class ActionHandler {
    public static enum ACTION {
        WALK,JUMP,RUN,SIT,SLEEP,WATCH;
    }

    
    public void sleep(){
        System.out.println("the character has sleep on the bed");
    } 
    public void watch(){
        System.out.println("the character has watch th eclock");
    } 
    public void sit(){
        System.out.println("the character has sit on the chair");
    }
    public void walk(){
        System.out.println("the character has walk in park");
    }
    public void jump(){
        System.out.println("the character has Jump on the pool");

    }
    public void run(){
        System.out.println("the character has run to not arrive late due the boss would get mad at him :3");

    }

}
