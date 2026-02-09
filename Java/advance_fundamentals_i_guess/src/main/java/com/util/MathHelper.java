package com.util; 

public class MathHelper {


    public static double average(double[] nums){
        double result =0;
        for (double n:nums)
        {
            result +=n;
        }
        return result /nums.length ;
    }



}
