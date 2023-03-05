package com.tutorialspoint;

import java.math.*;
  
public class BigDecimalDemo {

    public static void main(String[] args) {

    // create 2 BigDecimal objects
    BigDecimal bg1, bg2;

    MathContext mc = new MathContext(4);// 4 precision

    // assign value to bg1
    bg1 = new BigDecimal("40.1264");

    // assign negate value of bg1 to bg2 using mc
    bg2 = bg1.negate(mc);

    String str = "Negated value, rounded to 2 precision is " +bg2;

    // print bg2 value
    System.out.println( str );
    }
}