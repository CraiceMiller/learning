from typing import Any, Iterable

def my_binary(iterable:Iterable,
             target:Any)->int:
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

def mergeSort(iterable_:list)->list: 
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

    
    


"""
Firt what the f*** this works: 
    leftSide:list=mergeSort(iterable_[:middle])
    rightSide:list=mergeSort(iterable_[middle:])
i know this is call recursion, but why it works, i mean, when i call this one:
mergeSort(value)
it automally call others two mergeSort function. so why i dont get a Recurtion error?
since this will always be calling each other: 
how i see it: 
     if i call it once. leftSide will call it again, inside this another call, lefiSide will it 
     again. for me this will call it over and over again . 


second question: 
how this even posible: 
i=j=k=0

third question: 
why i need to do three loops

four question: 
why am i so stupid that i can solve this problem for myself and i needed help to do it?



"""





