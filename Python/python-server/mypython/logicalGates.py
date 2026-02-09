def OR(a,b)->bool: 
    return a or b

def AND(a,b)->bool:
    return a and b 


def NOT(a)->bool: 
    return not a 

def NAND(a,b)->bool: 
    return  NOT(AND(a,b))

def NOR(a,b)->bool: 
    return  NOT(OR(a,b))

def XOR(a,b)->bool: 
    return a != b

def NXOR(a,b)->bool:
    return NOT(XOR(a,b))



text1:str="""
#19/08/2025
    My conclusion of 'Logical Gates':

a:bool=True 
b:bool=False


The AND gate only will be True (1) if a and b are True
unique value: 
    True AND True = True

    anything else False

Example: 

--------------------------------------
|          AND                       |
--------------------------------------
| False     |False     |False        |
| True      |False     |False        |
| False     |True      |False        |
| True      |True      |True         |
---------------------------------------

The OR gate will be True if at least there is ONE True Value. For me I see this gate like:"will only be False if both are False, True otherwise!"
unique value: 
    False OR False = False

    anything else True

Example: 

--------------------------------------
|          OR                        |
-------------------------------------
| False     |False     |False       |
| True      |False     |True        |
| False     |True      |True        |
| True      |True      |True        |
-------------------------------------

The NOT gate will only reverse the value. Treu becomes False and False Becomes True 
True -> False
Example: 

--------------------------
|          NOT           |
--------------------------
| False     ||True       |
| True      ||False      |
| False     ||True       |
| True      ||False      |
--------------------------

The NAND gate is the same of AND but the other way around. For me, it will be False if both value are True, True otherwise
unique value: 
    True NAND True = False

    Anything else True 

Example: 

-------------------------------------
|          NAND                     |
-------------------------------------
| False     |False     |True        |
| True      |False     |True        |
| False     |True      |True        |
| True      |True      |False       |
-------------------------------------

The NOR gate is the oppisite of OR. For me will be True if both are False
unique value: 
    False NOR False = True

    anything else False

Example: 

---------------------------------------
|          NOR                        |
--------------------------------------
| False     |False     |True         |
| True      |False     |False        |
| False     |True      |False        |
| True      |True      |False        |
--------------------------------------

The XOR gate will be True if there are ONLY one single True.For me it will be False if both value are equals
True XOR True = False
False Xor False = False

Example: 
--------------------------------------
|          XOR                       |
-------------------------------------
| False     |False     |False       |
| True      |False     |True        |
| False     |True      |True        |
| True      |True      |False       |
-------------------------------------

The NXOR gate will be True if both value are the same: 
True  NXOR True = True
False NXor False = True


Example: 
--------------------------------------
|          NXOR                      |
--------------------------------------
| False     |False     |True         |
| True      |False     |False        |
| False     |True      |False        |
| True      |True      |True         |
--------------------------------------



Ultimately, if a want to compare unique values i can use wheter AND or NOR. I mean if 
I want to check if both are exclusive False i can use NOR: 

name=None
age=None

using NOR

    if not (name or age): 
        print('please write at leat one value' )

If i want to check the both value must be true i can use AND

    if name and age:
        print(f'Hello {name}' you are {age} years old')

I can use OR to check if there is at lest one value
    if name or age: 
        print('Hello')

I can use NOT no reversed the truehness of the value.
     if not name: 
        print('It seems you did not write your name')
  
Regards to NAND, XOR, NXOR i don't know where shoul i used these ones



"""

text2:str="""
Currently I have this structure in my computer
today 19/08/2025

Learning_Python:
    Attempt.png
    Bye world!.docx
    Bye world!.docx.docx
    Hello json.json
    Hello world.asdf
    Hello world.xlsx
    Hello.txt
    I got lost.xlsx
    Learning new thing everyday.txt
    My trying.docx
    my_first_database.db
    my_first_json.json
    PAS.png
    Prueba_T.png
    Sale and Purchase Management.xlsx
    Sales.xlsx
    Sale_Management.json
    __init__.py


    Proyects: 
        alarm_clock.py
        banking_program.py
        calculator.py
        Compound interet calculator.py
        concession stand.py
        countdown timer programer.py
        Dice roller program.py
        encryption_program.py
        g.py
        hangman.game.py
        list_words.py
        new countdown.py
        new_slot_machine.py
        number guessing.py
        quiz game.py
        random number.py
        rock, paper, scissors.py
        shopping cart.py
        slot_machine.py
        tempeture.py
        weight converte.py
        __init__.py
       

    Topics:
        2d collections.py
        another data types.py
        colletion.py
        conditiona expression.py
        date_time.py
        decorated_operator.py
        default arguments.py
        duck_typing.py
        example_modules.py
        exception.py
        for.py
        format_specifiers.py
        funtion_def.py
        good_habits.py
        higher_order_funtions.py
        If.py
        ifname.py
        ifname_2.py
        indexing.py
        inheritance.py
        Input.py
        iterables.py
        lamba.py
        list comprehension.py
        Logical_operations
        match statement.py
        math.py
        modules.py
        multiple_inheritance.py
        nested loops.py
        nested method.py
        polymorphism.py
        property.py
        string methods.py
        test.py
        Textbox.py
        Typecasting.py
        Variables.py
        While.py
        __init__.py
                        


    whatever: 
        __init__.py
        Calculator.py
        classes_in_python.py
        classes_to_use.py
        classes_variables.py
        exercise 1.py
        exercise 2.py
        exercise 3.py
        exercise 4.py
        exercise 5.py
        exercise 6.py
        exercise 7.py
        exercise9.py
        exercise_10.py
        exercise_8.py
        file_detection.py
        functions_to_use.py
        help_from_gemini.py
        help_from_gemini2.py
        interes compuesto.py
        iterables_to_use.py
        logicalGates.py
        my_attempt_class.py
        my_calculator.py
        my_ocs.py
        my_original_character.py
        My_Statistics.py
        my_translator_class.py
        pandas_functions.py
        patterns.py
        product_cart2.py
        pyproject.toml
        python_object_oriented_program.py
        qr_code_converter.py
        School_form.py
        squidgame.py
        student record system.py
        weight converte.py
        what_ever.py
        youtube_video_downloaded.py
        _0_analizing_code.py
        _1.py
        _10_dataclass.py
        _11.py
        _13_json_attempt.py
        _14_customtkinter.py
        _15_pandas.py
        _16.py
        _18.py
        _19_functions.py
        _2.py
        _20_recurtion.py
        _21.py
        _3.py
        _4.py
        _6.py
        _7.py
        _8.py
        _9.py
        _a.py
        _b.c
        _c.py
        _e.py
        _f.py
        _g.py
        _h.py
        _i.py
        _j.py
        _k.py
        _l.py
        _m.py
        _n.py
        _o.py
        _p.py
        _q.py
        _r.py
        _s.py
        _t.py
        _u.py
        _v.py
        _w.py
        _x.py
        _y.py
        _z_.py
   
  

        Classes_Use:
            __init__.py
            clock.py
            iterables_to_use.py
            my_mini_bank.py
            my_mini_store.py
            person.py
            __init__.py

            
    



"""


if __name__ == "__main__": 
    x:bool=False
    y:bool=True 
    logic=XOR

    values:list=[x,y,x,y]
    values2:list=[x,x,y,y]
    logicalfunctions:list=[AND,NAND,OR,NOR,NOT,XOR,NXOR]



    for func in logicalfunctions: 
        print("-"*40)
        print("|" +" "*10 + func.__name__ + " "*10 + "|" )
        print("-"*40)

        for a,b in zip(values,values2): 
 

            if func.__name__ != "NOT":
                print(f"| {str(a):<10}|{str(b):<10}|{func(a,b)}        |") #type: ignore
                continue 

            print(f"| {str(a):<10}||{func(a)}        |") #type: ignore

    














