package com.desktop.individual;

import com.desktop.items.Coffe;
import com.desktop.items.Cup;
import java.util.Queue;
import java.util.LinkedList;



public class ProgrammingLearner extends Person implements LivingBeing {
    private Cup coffe; 
    private boolean hasTaskToDo = false;
    private Queue<String> tasks = new LinkedList<String>();

    public ProgrammingLearner(String name,Integer age)
    {
        super(name,age);
        this.setDefaultTask();
    }

    private void code(){
        if (this.tasks.isEmpty()){
            System.out.println("The programmer end all the task :3");
            this.hasTaskToDo = false;
            return;
        }

        String currentTask = this.tasks.remove();
        System.out.println("Doing "+ currentTask);
    }

    public void study()
    {
        while(this.hasTaskToDo)
        {
            this.code();
            this.eat(); 
        }
        this.sleep();
    }

    @Override
    public void eat() {
        if(this.coffe ==null){
            System.out.println("The programemr has no a cup! :(");
            return ;
        }

        if(this.coffe.isEmpty()){
            System.out.println("Oh no, the programmer has no coffe! :|");
            this.coffe.fillAll();
            return;
        }

        this.coffe.use();
        System.out.println(this.name +" is drinking coffe! yummy :)");
    }

    @Override
    public void sleep() {
        if(hasTaskToDo){

            return;
        }
        System.out.println(this.name + " is sleeping!");
    }

    void setDefaultTask()
    {
        this.tasks.add("Learn Aggregation" );
        this.tasks.add("Learn Composition" );
        this.tasks.add("Debbug the algorithm" );
        this.tasks.add("Learn Association" );
        this.tasks.add("Refact the issue at hand" );
        this.tasks.add("Update the repository" );
        this.tasks.add("Debbug the task" );
        this.tasks.add("Debbug the task" );
        this.tasks.add("Complete the structure" );
        this.hasTaskToDo = true;

    }

    public void setCoffe(Cup c){
        this.coffe = c;
    }
}
