from mypython.utils import (quickSort, mergeSort,binarySearch)
from mypython.decorators import time
from typing import Generator
import mypython 
def counter()->Generator[int,int,int]:
    num:int = 0
    while (True):
        yield num
        num += 1


@time
def qui(n)->None: 
    quickSort(n)

@time
def mer(a)->None: 
    mergeSort(a)

@time 
def main()->None: 
    from random import randint 
    numbers = [0,1,10,2,9,3,8, 4, 8, 3, 5,5,3]
    assert  not all(numbers)
    ran_Number = [randint(0,150) for _ in range(800)]
    ran_Number2 = [randint(0,150) for _ in range(800)]
    qui(ran_Number)
    mer(ran_Number2)

    @time
    def f():
        binarySearch(ran_Number,75)

    f()
    print("This is pretty much it i guess. ")
    print(ran_Number)
    print("------------------>")
    print(ran_Number2)

main()

 


