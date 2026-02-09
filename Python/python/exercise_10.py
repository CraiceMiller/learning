#How to use None once it for alll 

#NO.1
def greet_user(_user:str,
               _age:int|None=None,
               _country:str|None=None)->None:
    print(f"Hello {_user}")
    if _age is None or  _country is None:
        if _age is not  None:
            print(F"You're {_age} years old")
            
        if _country is not None:
            print(f"You're live in {_country}")
           
        print("_________")
        return 
    
    print(F"You're {_age} years old")
    print(f"You're live in {_country}")
    print("_________")
    return 
    
    

    


greet_user("Alice", 30)
greet_user("Bob")
greet_user('Craice',18,"Altisora")
greet_user('Ashly',_country='Altisora ')

#NO.2
phone_book = {"Alice": "123-4567", "Bob": "987-6543",'Craice': "965-456","Hersy": "852-147","Ashley":"123-987"}
def get_phone_number(number:str|None,
                     person:str)->str:
    if number is None:
        return f"Error 404: {person} was not found!"
    else:
        return f"{person} indeed exist. their number is {number}"


def find_phone_number(_person_name:str):
    searching_number:None|str=phone_book.get(_person_name)
    return get_phone_number(searching_number,_person_name) 


print(find_phone_number("Alice"))
print(find_phone_number("Charlie"))
print(find_phone_number('Craice'))
print(find_phone_number('Anthony'))

#NO.3
box:tuple=1,5,7,10,25,100,25
def get_value(value:str)->None|int:
    try:
        intvalue:int=int(value)
        if intvalue in box:
            return intvalue
        else:
            return None 
    except ValueError:
        return None
    
guess:int|None=None
while guess is None:
    atteempt=input('guess the number inside the box: ')
    tracking=get_value(atteempt)
    if tracking is None:
        print('An error has ocurred')
    else:
        guess:int|None=tracking
print(f"Congratualion, you did it, {guess} was in the box")


#NO.4
from iterables_to_use import _mixed_values_
from _collections_abc import Iterable
from statistics import mean
from typing import Any



def arrange_stuff(mixed_iterable:Iterable)->dict:
    none_list:list=list(filter(lambda none:none is None, mixed_iterable))
    int_list:list=[]
    str_list:list=[]
    float_list:list=[]
    list_list:list=[]
    tuple_list:list=[]
    dict_list:list=[]
    bool_list:list=[]


    for values in  mixed_iterable:
        if isinstance(values,str):
            str_list.append(values)
        if isinstance(values,bool):
            bool_list.append(values)
            continue
        if isinstance(values,int):
            int_list.append(values)
        if isinstance(values,float):
            float_list.append(values)
        if isinstance(values, list):
            list_list.append(values)
        if isinstance(values,tuple):
            tuple_list.append(values)
        if isinstance(values,dict):
            dict_list.append(values)

    arrange_dict:dict[str, list[Any]]={
        "int list":int_list,
        "str list": str_list,
        "float list":float_list,
        "bool list": bool_list,
        "list list": list_list,
        "tupple list": tuple_list, 
        "dict list": dict_list,
        "none list": none_list
    }

    return arrange_dict

values:dict=arrange_stuff(_mixed_values_)
nums=values.get("int list")
        



    