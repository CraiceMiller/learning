#Importing the modules needed i guess
from itertools import groupby
from typing import Mapping,Any,Iterable
from collections import defaultdict
from time import perf_counter 
learn="""
#28/28/2025
defaultdict:
    so every new key i will provided it automally become a list (or the value i provide)
    if i do this

    my_defaultdict=defaultdict(set)
    my_defaultdict[key].add(value)

    It is the same to type:
    my_dict={}
    but this do not raise a key error, instead it will create a new key using this value i provided

Sorted: 
    so what i am doing here:

    sorted(people, key=lambda person: person["age"])
    
    In short, key needs a rule to apply to each item, not the result of that rule on a single, non-existent item.
    im telling that i want the new list sorted by the key age of each dict, right?
"""


def mygroupby(values:Iterable[Mapping],target:str)-> dict[str,list[dict[str,Any]]]:
    """"
    DESCRIPTION: 
        This method will join all the dict of a iterable of dicts, and return a new dictionary 

    RETURN : 
        A dictionary, where the key is the target provided and the value is a 
        list of each dictionaries where the target appears
    
    """
    

    if values[0].get(target) is None: #type: ignore
        raise ValueError("Type a valid target")


    new_dict:dict=defaultdict(list)

    for dicts in values:
        key = dicts.get(target)

        if key is not None: 
            new_dict[key].append(dicts)



    sorted_list=sorted(new_dict.keys())

    sorted_dict={key:new_dict[key] for key in sorted_list}
   

           
    return sorted_dict



#creating the functiuon with mapping
def print_items(items:Mapping)->None: 
    print("Name: ", items.get("name","N/A"))
    print("Age: ", items.get("age","N/A"))


def groupby_(iterable:Iterable,key:str,reverse:bool=False)->groupby: 
    sorted_keys=lambda k:k[key]
    sorted_list=sorted(iterable,key=sorted_keys ,reverse=reverse)
    new_group=groupby(sorted_list,key=lambda k:k[key])
    
    return new_group




#Creaing the list of dictionaries
my_list:list[dict]=[
    {
        "name": "Hersy",
        "age":18
    },
    {
        "name": "Craice",
        "age":19
    },
    {
        "name": "Ashley",
        "age":17
    },
    {
        "name": "Misery",
        "age":18
    },
        {
        "name": "Sthepany",
        "age":17
    },
        {
        "name": "Craice",
        "age":19
    },
    {
        "name": "Ashley",
        "age":17
    },
            {
        "name": "Craice",
        "age":19
    },
    {
        "name": "Mark",
        "age":20
    },
    {
        "name": "Anthony",
        "age":21
    },
]



#printing the values
#mygroupby
start=perf_counter()
nw_list4= mygroupby(my_list,"age")

for x,y in nw_list4.items(): 
    print(x,y)
end=perf_counter()
final=end-start

print()
print()


#groupby
start2=perf_counter()
nw_list=sorted(my_list,key=lambda name:name["age"])
nw_list2= groupby(nw_list,key=lambda name:name["age"])
for a,b in nw_list2: 
    print(a,list(b))
end2=perf_counter()
final2=end2-start2


print()
print()

#groupby 2
start3=perf_counter()
new_list_=groupby_(my_list,"age")
for a,b in new_list_: 
    print(a,list(b))
end3=perf_counter()
final3=end3-start3


print()
print("Time groupby class: ", final2 )
print("Time mygroupby: ", final )
print("Time Second groupby_: ", final3 )





   





