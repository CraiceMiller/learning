package com.desktop;

import com.desktop.technology.computer.*;
import com.desktop.individual.ProgrammingLearner;
import com.desktop.items.*;

/**
 * important and simple things, like Intenger, Exception...
 */
import java.lang.*;
/**
 * Simple UI classes
 */
import java.awt.*;
/**
 * Simples and fundamentals structures and algorithms like Queue, Maps...
 */
import java.util.*;
/**
 * Very precise values to work with math operations 
 */
import java.math.*;
/**
 * 
 */
import java.time.*;
/**
 * 
 */
import java.applet.*;
/**
 *classes to work with Input and Output, 
 */
import java.io.*;

import java.awt.Dimension;


/**
 * <h1>How to use concurrency <strong>Thread</strong></h1>
 * <p>
 * 
 </p>
 */
class Test implements Runnable
{
    //TODO: why is this operation ?
    static final int  CAPACITY = 1 << 30;

    //propeties                                                                      
    private String value;
    private Thread thread;
    private ArrayList<String> list = new ArrayList<String>(10);
    private HashMap<String,Integer> map = new HashMap<String,Integer>();

    //private Clock clock = new Clock();

    //TODO: Why we use final in methods too, i thought it was only for properties ...
    public final int getNumber() { return 0;}
    public String getString(){return "hello";}
    //TODO: what is this. why we use the ? symbole here..
    //static Class<?> comparable(){return "";}


    private void test()
    {
        this.list.add("Hersy");
        Clock.systemUTC();
       this.map.clear();
       
       


        long num=0;
        int times = 0;
        System.out.println(this.value);
        do {
            times++;
            System.out.println(times+". Please dont give up yet!");
            

            if(num>=times){this.value="some value";}
            num++;
            

        } while (times < 5);
        System.out.println(this.value);
        System.out.println(times);


    }

    public void startThread()
    {
        this.thread = new Thread(); 
        this.thread.start();
    }

    public void run() {
        System.out.println("The Test Thread is running :3");
        while(this.thread != null)
        {
            System.out.println("Just do it!");

        }
       
        this.test();
    }

}


/**
 * <h1>Main App</h1>
 *
 *
 # Association
 i dunno

 # Aggregation:
 Represent a "has-a" realationship between object. One object contains another object as a part of its structure. but the containced object/s can exist independently
 

 # Composition:
 Respresent a "part-of" realationship between objects. Allows complex Object to be Constructed From smaller Object. fro example an Engine is part of a Car. 

 
 *@url https://stackoverflow.com/questions/76336221/vs-code-java-maven-lambda-expressions-are-allowed-only-at-source-level-1-8-o
 */
public class App 
{
    
    public static void main( String[] args )
    {
        //Creating the objects,instaces
        //Test test = new Test();
        // Monitor monitor = new Monitor(100,200);
        //Table table = new Table();
        Coffe coffe = new Coffe(Coffe.Type.AMERICANO);
        Cup cup = new Cup();

        ProgrammingLearner person = new ProgrammingLearner("Geroge",19);


        //TODO:How the instanceof keyword works ?
        /** */
       // boolean result = test instanceof Runnable;

        
       //person.setCoffe(coffe);
       cup.setContent(coffe);
       cup.fillAll();
       person.setCoffe(cup);
       person.study();

        //running the methods here :)
        //test.startThread();
        //monitor.turnOff();


        //System.out.println(result);
    }
}
