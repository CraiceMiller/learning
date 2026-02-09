
/** 
my attempt of create my very first program in Java in order to learn Object- Orineted Program 
start : 30-12-2025 at 7:00hrs Tuesday 
*/
public class Person
{
    public static int people = 0 ;

    public String name;
    final public static String value ="";
    public int age;

    public Person(String name, int age)
    {
        this.name = name;
        this.age = age ;
        Person.people +=1;
    }
    

    /**This just greet the person */
    public void greet()
    {
        System.out.println("Hello, my name is " + this.name);
    }
}