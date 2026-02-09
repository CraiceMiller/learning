package main;

import java.awt.Color;

public class Config {
    static final Color BACKGROUND_COLOR = Color.BLACK;
    static final Color COMPONENT_COLOR = Color.white; 

}

/**
 * package main; 
import java.awt.Color;

//no public due i wnat it to make it private, only the packge can know 
enum Config {
    BACKGROUND_COLOR(Color.LIGHT_GRAY );

    private final String currentValue;
    private Config(String v){
        this.currentValue = v;
    }

    private Config(Color v){
        this.currentValue = v;
    }

    public String gettValue()
    {
        return this.currentValue;
    }

}

 */