# polymorphism = Greek word that means to "have many forms or faces"
  #  poly = Many 
   # Morphe = Form

#5/8/25

"""
MY CONCLUTIONS: 
    -So, the abstractmethod tell us that every class based of the class that 
    have a abstractmethod,it MUST have their own method, It'll raise an TypeError otherwise

    - if we dont write the abstractmethod, it will only add more info base of the previous one..

    -ABC enforce the class that the others classes have the requeried method.
    if we dont type ABC, python will ignore the @abstractmethod and it won't raise a TypeErorr,
    Therefore it is a useful tool that ensure the developer write the method needed of each 
    subclases (childclasses)
        i this one like the english grammar. We use 'must' to tell people important things (it is 
        mandatory). We use 'should' to tell people advice (it could be done or not)

        The same applies here, we use ABC and @abstractmethod to tell 'must', 'should 'otherwise

    -Pizza class works due it child of Circle and circle has the area method, therefore, Pizza
    inheritance everything from Circle class

    -In my Dimon class, in the method name(), it won't raise a TypeErrorr because it is not a 
    abstractmethod...

"""

from abc import ABC, abstractmethod
from typing import Union
from collections import Counter


class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    def name(self)->str:
        return "I am a shape"

    def __init__(self) -> None:
        super().__init__()


class Circle(Shape):

    def __init__(self, 
                 radius:int|float) -> None:
        super().__init__()
        self._radius=radius

    def area(self)->Union[int,float]:
        return 3.14 * self._radius **2
    
    def name(self)->str:
        return super().name() + " I am a Circle"

    pass
 
class Triangle(Shape):

    def __init__(self,
                 base:int|float,
                 height:int|float) -> None:
        super().__init__()
        self._base=base
        self._height=height

    def area(self)->int|float:
        return self._base * self._height * 0.5
    
    def name(self)->str:
        return super().name() + ", I am a Triangle"

class Square(Shape):

    def __init__(self, side:int|float) -> None:
        super().__init__()
        self._side=side

    def area(self) -> Union[int,float]:
        return self._side **2
    
    def name(self)->str:
        return super().name() + ", I am a Square"

class Pizza(Circle):

    def __init__(self, topping, radius) -> None:
        super().__init__(radius)
        self._topping=topping

    def name(self) -> str:
        return super().name() + ". and I am a pizza, too!!"


class Dimond(Shape):
    def __init__(self, side) -> None:
        super().__init__()
        self._side=side

    def area(self) -> Union[int,float]:
        return self._side **2




def main()->None:
    circle=Circle(20)
    square=Square(20)
    triangle=Triangle(20,10)
    pizza=Pizza("tomatoes", 15)
    dimond=Dimond(25)
    square2=Square(20)

 

    shapes:list=[circle,square,triangle,pizza,dimond,square2]


    for shape in shapes:
        print(f'{shape.area()}cm^2')
        print(shape.name())



if __name__ == '__main__':
    main()