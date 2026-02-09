from collections import defaultdict
from typing import Any, Hashable,Mapping,Self,Iterable,overload
from itertools import zip_longest
from abc import ABC,abstractmethod


text="""
#29/08/2025
__hash__ method only declare the class itself as a Hashable.
all classes are hashables... Nonetheless, it the class has the __eq__ method, 
the class is not hashable anymore, untill you write the __hash__ method manually

__getitme__ method only help to use square bracket to acess a value within the class

__iter__ method only convert a value in the class in a Iterator (list)

"""




class Mydict(ABC,Mapping): 
    """
    My class to create dictionaries using two list. To acces the dictionary; use the property 
    Mydict().show
    
    """

    def __init__(self,default:Any=None,/) -> None:
        self._default:Any=default
        self._dictionary:defaultdict=defaultdict(lambda: self._default)
     
        
    def __getitem__(self,key)->Any: 
        """Get the value using square brackets"""
        return self._dictionary[key]
    
    def __len__(self)->int: 
        return len(self._dictionary)

    def __iter__(self): 
        return iter(self._dictionary)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__} (_default={self._default},self._dictionary={self._dictionary})"

    def __next__(self): 

        key= next(self.__iter__())
        value= self._dictionary[key]


        return (key,value)

    @abstractmethod
    def setvalues(self,keys,values,/):
        ...
   
    def setvalues(self,keys:list[Hashable],values:list[Any],/)->Self: #type: ignore
        """Here is where you can create the dictionary at hand.
        if there is not enough values for the key provided, it will storage with the default value
        of the class.

        parameters:
            keys: This must be a list of hashables objects, It will be the key of the dict
            values: Second list, this could anything value
        
        """
        
        for key,value in zip_longest(keys,values,fillvalue=self._default): 
            self._dictionary[key] = value 

                 
        print("The values was successully added")
        return self

   

    @property
    def  show(self)->dict: 
        """Use this property to get the dictionary"""
        return dict(self._dictionary)
    
    @property
    def defaultvalue(self)->Any: 
        return self._default
    
    @defaultvalue.setter
    def defaultvalue(self,value)->None:
        print(f"The default value '{self._default}' was turn into '{value}'")
        self._default =value

 


class CreateDictForPandas(Mydict):
    """
    This class will only help me to create automally a dict to work with pandas. 
    
    """



    @overload
    def setvalues(self,headers:list[str],*values:Iterable[Any])->Self:
        ...

    @overload
    def setvalues(self,headers:list[str],*values:Any)->Self:
        ...


    def setvalues(self,headers:list[str],*values:Iterable[Any])->Self:
        """The main logic
        The key will be
    the first list, and all the data will be a tuple.
    
    expected output: 
        CreateDictForPandas().setvalues(["ID","Name"],[100,101,102],["Hersy","Craice","Ashley"])\n
            {
                "ID": [100,101,102]
                "NAME":["Hersy","Craice","Ashley"],
            }
        """
        if isinstance(values[0],Iterable) and not isinstance(values[0],str):

            for index,keys in enumerate(headers):
                self._dictionary[keys] = values[index]

        else:
            for index,keys in enumerate(headers):
                self._dictionary[keys] = [values[index]]

        print("all the values was done")
        return self


    def convert(self,dictionary:Mapping)->Self: 
        """
        This method will convert all the values from a normal to a dict that pandas can undertant
        
        """

        for key, value in dictionary.items(): 
            if not isinstance(value,list):
                self._dictionary[key]=[value]
            else: 
                self._dictionary[key] = value


        return self


    def length(self)->Self: 
        """This method will arrange all the value to have the same lenght"""
   
        lengths=[len(x) for x in self._dictionary.values()]
        min_value:int=min(lengths)

        for key,value in self._dictionary.items(): 
            if len(value) == min_value: 
                self._dictionary[key]=value
            else: 
                self._dictionary[key]=[value[:min_value]]

        

        return self

    @property
    def show(self)->dict[Hashable,list[Any]]: 
        return dict(self._dictionary)


def print_values(items:Mapping[Hashable,Any])->None: 
    print()
    for index,(key,value )in enumerate(items.items(),1): 
        print(f"Items No.{index}, Key: {key:<20}, Value: {value}")



if __name__ == "__main__": 

    headers=["ID","Name","Country"]
    values:list=[101, "Craice","Altisora","Mailer",]
    ids=[100,101,102]
    names=["Hersy","Craice","Ashley"]
    country=["Altisora"]*3

    normal_dict={
            "name": "Hersy",
            "age":18,
            "lastname":["Helson"]
            }


    my_dict=Mydict().setvalues(headers,values)
    my_pandas=CreateDictForPandas().setvalues(headers,ids,names,country)
    my_pandas2=CreateDictForPandas().setvalues(headers,103,"Miseru","Altisora")
    my_pandas3=CreateDictForPandas().convert(normal_dict)


    print(my_dict.show)
    print(my_pandas.show)
    print(my_pandas2.show)
    print(my_pandas3.show)

    print(next(my_pandas2))
    print(next(my_pandas2))
   









