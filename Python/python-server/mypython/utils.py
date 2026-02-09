from typing import (Callable, Coroutine, Any, Iterable, Mapping,TypeVar)
from itertools import groupby
from collections import defaultdict


Value = TypeVar("Value")

#08/10/2025 at 9:00
def quickSort(array:list[Value], start:int=0, end:int|None= None)->list[Value]: 
    """
        Sorts a list in-place using the Quicksort algorithm.

        This is a recursive, comparison-based sorting algorithm with an average
        time complexity of O(n log n). The function modifies the input list 
        and returns a reference to the same list.

        @Parameters: 
            :param array: The list to be sorted. Elements must be comparable (e.g., numbers or strings).
            :type array: list
            :param start: The starting index of the subarray to be sorted (inclusive). Defaults to 0.
            :type start: int
            :param end: The ending index of the subarray to be sorted (inclusive). Defaults to the last index.
            :type end: int | None

        @Errors:
            :raises TypeError: If the 'array' is not a list.
            :raises ValueError: If 'start' or 'end' indices are invalid (e.g., outside the array bounds).

        @Return: 
            :return: A reference to the sorted input list.
            :rtype: list

        :Example:
        >>> data = [10, 7, 8, 9, 1, 5]
        >>> quickSort(data)
        [1, 5, 7, 8, 9, 10]
        >>> sub_array = [5, 2, 8]
        >>> quickSort(sub_array)
        [2, 5, 8]
    """
        


    if not isinstance(array, list):
        raise TypeError(f"Input must be a list, got {type(array).__name__}.")
    

    endIndex: int = len(array) - 1 if end is None else end

    #if not (0 <= start <= endIndex < len(array) or start == 0 and len(array) == 0):
    #    raise ValueError("Invalid 'start' or 'end' indices provided.")
    

    def swap(array:list,left:int,right:int|None = None)->None: 
        rightIndex:int = len(array) -1 if right is None else right
        array[left], array[rightIndex] = array[rightIndex], array[left]


    def split(array:list, low:int=0, high:int|None= None)->int:
        highIndex:int = len(array) - 1 if high is None else high

        pivot = array[highIndex]
        index = low -1 

        for i in range(low,highIndex + 1):
            element = array[i]
            if (element < pivot):
                index += 1
                swap(array, index, i)

        swap(array, index + 1, highIndex)
        return index + 1

    if (start < endIndex):
        index:int = split(array,start,end)
        quickSort(array,start, index -1 )
        quickSort(array, index + 1, endIndex)

    return array




#10/10/2025
def quickSortDict(array:list[dict[str,Any]],
                  key1:str,
                  key2:str|None = None ,
                  key3:str|None=None,
                  /,
                  start:int=0,
                  end:int|None= None)->list: 
    """
        Sorts a list in-place using the Quicksort algorithm.

        This is a recursive, comparison-based sorting algorithm with an average
        time complexity of O(n log n). The function modifies the input list 
        and returns a reference to the same list.

        @Parameters: 
            :param array: The list to be sorted. Elements must be comparable (e.g., numbers or strings).
            :type array: list
            :param start: The starting index of the subarray to be sorted (inclusive). Defaults to 0.
            :type start: int
            :param end: The ending index of the subarray to be sorted (inclusive). Defaults to the last index.
            :type end: int | None

        @Errors:
            :raises TypeError: If the 'array' is not a list.
            :raises ValueError: If 'start' or 'end' indices are invalid (e.g., outside the array bounds).

        @Return: 
            :return: A reference to the sorted input list.
            :rtype: list

        :Example:
        >>> data = [10, 7, 8, 9, 1, 5]
        >>> quickSort(data)
        [1, 5, 7, 8, 9, 10]
        >>> sub_array = [5, 2, 8]
        >>> quickSort(sub_array)
        [2, 5, 8]
    """
        


    endIndex: int = len(array) - 1 if end is None else end

    

    def swap(array:list,left:int,right:int|None = None)->None: 
        rightIndex:int = len(array) -1 if right is None else right
        array[left], array[rightIndex] = array[rightIndex], array[left]


    def split(array:list, low:int=0, high:int|None= None)->int:
        highIndex:int = len(array) - 1 if high is None else high

        if(key2 is not None ): 
            pivot = array[highIndex][key1][key2]
        elif (key2 is not None and key3 is not None): 
            pivot = array[highIndex][key1][key2][key3]
        else: 
            pivot = array[highIndex][key1]

        index = low -1 

        for i in range(low,highIndex + 1):

            if(key2 is not None ): 
                element = array[i][key1][key2]

            elif (key2 is not None and key3 is not None): 
                element = array[i][key1][key2][key3]

            else: 
                element = array[i][key1]

            


            if (element < pivot):
                index += 1
                swap(array, index, i)

        swap(array, index + 1, highIndex)
        return index + 1

    if (start < endIndex):
        index:int = split(array,start,end)



        quickSortDict(array,key1,key2,key3,start, index -1 )
        quickSortDict(array,key1,key2,key3, index + 1, endIndex)

    return array





# /08/2025 _______________________________________________________________________
def mergeSort(iterable_:list[Value])->list[Value]: 
    """
    DESCRICTION: 
        This is my attempt of create a merge algorithom. 
        This funtion will sorted the iterable in a very effiency way

    Return: 
        A list 
    """
    #1. Return if the Iterable is one
    if len(iterable_) <=1: return iterable_

    #2. getting the middle part of the iterable
    middle:int=len(iterable_) // 2

    #3. spliting the iterable and 4. Merging the list, I gues 
    leftSide:list=mergeSort(iterable_[:middle])
    rightSide:list=mergeSort(iterable_[middle:])



    i: int = 0
    j: int = 0
    k: int = 0

    while i < len(leftSide) and j < len(rightSide): 
 
       
       if leftSide[i] <= rightSide[j]: 
          iterable_[k]= leftSide[i]

          i += 1
           
       else: 
          iterable_[k] = rightSide[j]
          j += 1
       
       k += 1

    while i < len(leftSide): 
       iterable_[k] = leftSide[i]
       i +=1
       k += 1
 

    while j < len(rightSide): 
       iterable_[k] = rightSide[j]
       j += 1
       k += 1
       

  
    return iterable_


#28/09/205
#MY VESRSION OF HOW TO USE ASYNC, JSON, AWAIT,__________________________________________________________________________
async def doTask(task:Callable[...,Coroutine] ,callbackfn:Callable|None=None,*args,**kwargs):
    """
    DESCRIPTION: 
        this function only carry out an awaitable function and do another thing based of the result in the 
        previous function provided. This will not do the second tasks if :
            - The result of the firts task is None.
            - The callbackfn param is None
            - The callbackfn is not Callable

    PARAMETERS:
        task: The awaitable function to be executed
        callbackfn:  The another task to do later to complet the first one, it will do nothing if 
        is none
        args and kwargs: are only the params that first task needs


    """
    try: 
        result = await task(*args,**kwargs)

        if callbackfn is not None and isinstance(callbackfn,Callable ) and result is not None: #type: ignore
            callbackfn(result)

    except Exception as e : 
        print(e)


#28/08/2025
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



def Groupby(iterable:Iterable,key:str,reverse:bool=False)->groupby: 
    """This funtion will do the same as mygroupby, but more eficiency and return a groupby object"""
    sorted_keys=lambda k:k[key]
    sorted_list=sorted(iterable,key=sorted_keys ,reverse=reverse)
    new_group=groupby(sorted_list,key=lambda k:k[key])
    
    return new_group

#16/08/2025
def binarySearch(iterable:Iterable[Value],
             target:Value)->int:
  """
  This is my own attempt of doing binary search. 
  \nDescription: 
        This will give us only the index of the target value, return -1 if the value does
        not exist or occurs a problem.
        To make this funtiob more optimized, you need to give it a sorted list already
    \nReturn: 
        the index of the target at hand as a interget, -1 otherwise

    \nParameters: 
        iterable: this is the iterable to follow through
        target: this is the value you want to know the index

    \nExample: 
    >>> my_binary([1,2,3,4,5],3)
        output: 2

  
  """ 
  start:int= 0
  end:int=len(iterable) -1 #type: ignore

  try: 

    while start <= end: 
      mid:int = (start + end)//2 

      if iterable[mid]== target: return mid #type: ignore

      elif iterable[mid]< target: start= mid +1 #type: ignore
        
      else: end= mid -1

  except: return -1

  return -1


def binarySearchDict(dictionaries:list[dict[str,Any]],
                     target:Value,
                     key:str,
                     key2:str|None = None,
                     key3:str|None = None,
                      /)->int: 
    """
    Performs a binary search on a sorted list of dictionaries.
    
    NOTE: The list of dictionaries MUST be sorted by the given 'key'
    before calling this function.
    
    
    """
    
 
    start:int=0
    end:int=len(dictionaries)-1

    while start <= end:
        mid:int= (start + end) // 2

        try: 
            if (key2 is not None): 
                middle_value = dictionaries[mid][key][key2]
            elif (key2 is not None and key3 is not None): 
                middle_value = dictionaries[mid][key][key2][key3]
            else: 
                middle_value = dictionaries[mid][key]

        except KeyError: 
            return -1
            
        if middle_value == target: return mid

        if middle_value < target: start = mid +1

        else: end = mid -1


    return -1


    
    
