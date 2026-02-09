#31/082025
from time import perf_counter
from functools import wraps
from typing import (Any,Callable,TypeVar,cast)


_Function=TypeVar("_Function",bound=Callable[...,Any]) 

def time(___function:_Function)->_Function:
    """This is my first decorator. 

    Description. 
        This decorator will allow me to track the time needed of every funtion i provide

    Return: 
        return a funtion call wrapper in order to pass all the funtion needed
    
    """
  

    @wraps(___function)
    def wrapper(*args:Any,**kwargs:Any)->Any: 
        #count the beggening of the operation 
        start:float=perf_counter()

        #The main funtion that will be executed
        result:Any=___function(*args,**kwargs)

        #count the end of the operation 
        end:float=perf_counter()
        final:float=end-start

        print()
        print(f"The function ' {___function.__name__}' was executed in {final:.4f} seconds\n")

        #return the result provided
        return result
    
    return cast(_Function,wrapper)


async def asyncTime(___function:_Function)->_Function:
    """This is my first decorator. 

    Description. 
        This decorator will allow me to track the time needed of every funtion i provide

    Return: 
        return a funtion call wrapper in order to pass all the funtion needed
    
    """
  

    @wraps(___function)
    def wrapper(*args:Any,**kwargs:Any)->Any: 
        #count the beggening of the operation 
        start:float=perf_counter()

        #The main funtion that will be executed
        result:Any=___function(*args,**kwargs)

        #count the end of the operation 
        end:float=perf_counter()
        final:float=end-start

        print()
        print(f"The function ' {___function.__name__}' was executed in {final:.4f} seconds\n")

        #return the result provided
        return result
    
    return cast(_Function,wrapper)


    

    
