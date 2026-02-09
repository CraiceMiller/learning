from types import UnionType
from classes_to_use import Bank,MyWatch

from typing import Self,Any


class Fruit:
    def __init__(self,name:str,grams:float) -> None:
        self._name=name
        self._grams=grams

    def __str__(self) -> str:
        return f'Name: {self._name}'

    def __eq__(self, __value: object) -> bool:
        return self.__dict__ == __value.__dict__
    
    def __format__(self, __format_spec: str) -> str:
        match __format_spec:
            case 'kg':
                return f'{self._grams/1000:.2f}kg'
            case 'desc':
                return f'{self._name} has {self._grams}g'
            case _:
                return 'Unkwon format specifier...'
    
    def __lt__(self,__value)->bool:
        return self._grams < __value._grams
    
    def __gt__(self,__value)->bool:
        return self._grams > __value._grams
    
    def __add__(self,__value)->int|float:
        return self._grams + __value._grams

    def __or__(self, __value: Any):
        new_name:str=f"{self._name} and {__value._name}"
        new_grams:float=self._grams + __value._grams
        return Fruit(name=new_name, grams=new_grams)
    
    def __repr__(self) -> str:
        return f'Fruit( name={self._name}, grams={self._grams})'
    
    def __getitem__(self,key:str)->str:
        if key == 'name':
            return self._name
        if key == 'grams':
            return str(self._grams)
        return 'N/A'
    
  




def main()->None:
    fruit1:Fruit=Fruit('apple',100.05)
    fruit2:Fruit=Fruit('orange',150.45)
    fruit3:Fruit=Fruit('apple',100.05)
    
    print(fruit1==fruit2)
    print(fruit1==fruit3)
    print(f'{fruit1:kg}')
    print(f'{fruit1:desc}')
    print(f'{fruit1:g}')
    print(fruit1)
    print(repr(fruit1))
    print(fruit2['name'])
    print(fruit2['grams'])
    print(fruit2['pizza'])

   

    #union of classes
    combined_fruits:Fruit= fruit1 | fruit2 | fruit3
    
    print(combined_fruits)
    print(combined_fruits._grams)




    #information 
    lists_fruits:list[Fruit]=[
        Fruit('strawberry',25000),
        Fruit('banana',1000),
        Fruit('cocounuts',1500)
    ]

    for  fruit in lists_fruits:
        print(f"str: {fruit}")

    for  fruit in lists_fruits:
        print(f"repr: {repr(fruit)}")




if __name__ =='__main__':
    main()


""" 
user1:Bank=Bank(500,20,"Craice")
user2:Bank=Bank(250,30,"Craice")
user3:Bank=Bank(75,5,"Ashley")
user4:Bank=Bank(123,20,'sthepahy',20)

watch=MyWatch()


print(user1)
print(user2)
print(user1==user2)
print(user1<user2)
print(user1>user2)
print(user1+user2)
print("craice" in user1)
print(user1['user'])
print(user1.name)


print(type(user1))
#print(user1>user2)

"""

