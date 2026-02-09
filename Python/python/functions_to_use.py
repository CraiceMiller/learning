from typing import( Optional,Iterable,Mapping,Any,Iterable)
from collections import Counter
import random 
import speech_recognition as sr #type: ignore
from iterables_to_use import Currency_  #type: ignore
from itertools import groupby
from collections import defaultdict


"""
HOW TO WRITE BETTER FUNTIONS (by indently.io_):
    1. Write short and concise 
        Examples:
        - get_number
        - display_number
    
    2. Specify a return type 
        Example:
        -> None
        -> str
        -> int

    3. Make as simple and reusable as possible 
        Example:
        A function that only do one single task

    4. Document all your functions: 
        Example: 
        Write the core purpose of the funtion, what it does, what paremeter takes
        what it returns, an example.
        >>> get_number()
            output: 2

    5. Handles the errors appropriately:
        Example:
        raise ValueError
        raise TypeError
    

"""


#21/06/2025
def coumpond(capital:float = 200, interes:float=0.05, years:int=3)->float:
    result = capital *(1+interes) ** years
    return round(result,2)
    
def simple(capital:float = 200, interes:float=0.05, years:int=3)->float:
    result = capital + (capital * interes * years)
    return round(result,2)

#i dunno what were the date of these

def my_division(num:int,
                num2:int)->int|None:
    """This only return the divison as a integer number"""
    return num // num2

def my_counter(_iterable: Iterable,
               )->int:
    """This only return the numbers of object within  the iterable object"""
    return 2

def show_list_items(*items)->tuple|None:
    """
    Details:
    this funtions only will give you a list of iterover items; 
    separate by single, two or much.
    And you Must give it only single variables...
    Update: 10/07/2025
    """

    if items==():
         return None


    try: 
        first,*middle,last = items
        if  not middle:
            print(f"Two items: {first,last}")
            return None
        print(f'first item: {first}')
        print(f"Middles items:")
        for i in middle:
            print(f"-{i}")
        print(F"Last item: {last}")
        return None
    except ValueError:
            print(f"Single item: {items}")
            return None

def get_user_info(_user_id:int, 
                  _user_name:str,
                  _user_mail:str|None=None,
                  )->dict[str, (str|int)]:
    """This only will give us a dict of user's info"""
    if _user_mail is None:
        return {'Name': _user_name, 'ID': _user_id}
    else:
        return {'Name': _user_name, 'ID': _user_id, 'Email': _user_mail}
  
def find_user_by_id(_userid:int|str|None=None
                    )->Optional[str|int]:
    """
    This funtion will search the ID of the couster. 
    will return 'None' if it doesn't find anything
    """
    return _userid


def calculate_area(_length:float|int,
                   _width:float|int,
                   )->float|int:
    """This only will give us the  area"""
    return _length * _width


#challenge: create a funtion that tracks and diplay the top three most 
# frequent words in a given list
def get_top_three(string_list:Iterable)->list:
    """Description: this only will give us the top three words in an iterables"""
    count:Counter=Counter(string_list)
    top_words=[words for words in count.most_common(3)]
    return [item[0] for item in top_words]  
  
#

#challenge: 
def arrange_list(_list1:list[Any]|tuple[Any],
                 _list2:list[Any]|tuple[Any],
                 *_lists:Any,
                 _reversed:bool=False,
                 _repeated:bool=True)->list[Any]:
    """Description: A funtion that combined 
        two list and return an  ordered list """
    combined_list = list(_list1) 
    combined_list.extend(_list2) 

    if _lists:
        for item in _lists:
            if isinstance(item, Iterable) and not isinstance(item, str):
                combined_list.extend(item)
            else:
                combined_list.append(item) 
           
          

      
    if not _repeated:
        combined_list=list(set(combined_list))
        

    if _reversed:
        return sorted(combined_list,reverse=True)
    else:
        return sorted(combined_list)

#
def coin_flip()->str:
    """This only return a string of heads or tails"""
    num = random.randint(0, 1) 

    if num > 0.5:
        return 'Heads'
    else:
        return 'Tails'


#
    
def evaluating_passing_students(course:dict[str,int|float],
                                approved_note:int=60
                                )->list[str]:
    """\nDescription: 
    \nThis only will return a list of students who passed a certain note..."""
    passing_students:list=[]
    for key,value in course.items():
        if value > approved_note:
            passing_students.append(key)
 
    return passing_students


def currency_to_dollars(currency:str,
                        amount:int|float)->int|float:
    if not currency in Currency_:
        print("sorry, but we don't have that value")
        return amount
    
    dollars=  amount / Currency_[currency] 

    return round(dollars,2)

def dollars_to_currency(currency:str,
                        dollars:int|float)->int|float:
    if not currency in Currency_:
        print("sorry, but we don't have that value")
        return dollars
    
    currency_change=   Currency_[currency] * dollars

    return round(currency_change,2)



#


def get_speech_input()->str: 
    """
    \nDescription: 
    \nThis only get what the user is trying to say, and display it in the console
    """
    recognized:sr.Recognizer=sr.Recognizer()

    with sr.Microphone() as source:
        print("I'm listening, so say something....")
        recognized.adjust_for_ambient_noise(source)
        audio:Any=recognized.listen(source)

    try:
        text=recognized.recognize_google(audio)
        return text.lower()
    except sr.UnknownValueError:
        print("Sorry could you speak up, I couldn't make that out")
        return ""
    except sr.RequestError as e:
        print(f"Could not request the result: {e}")
        return ""

#2/8/25

def palindrome(variable:str)->bool:
    """
    Description: 
        this only will return True if the word is palindrome, False otherwise"""
    nw_var=variable.lower()
    return nw_var == nw_var[::-1]

def get_target_number(list_:Iterable[int],
                      target:int)->tuple:
    """
    DESCRIPTION:
        this funtion will return two value that when we add them, it will be the same as the target 
        number, return () otherwise
    """
    #yeah, I know this is NOT the best solution but at leat it works :)

    result=None
    for num in list_:
        for i in list_:
            if ( num  + i)==target:
                result = (num,i)
                break

    if result is not None:
        return result
                

    return ()


# 3/08/2025

def get_discount(prices: Iterable[float],
                 percent: float
                 )->float:
    """
    DESCRIPTION:
        A function that calculate the total of the sum of prices in the provided list and 
        applies a discount based on the given discount rate. If the discount is invalid (eg., 
        negative or greater than 1), the funtion raise a ValueError.

    RETURN:     
        (a float object) The total of the price later to apply the discount

    EXAMPLE: 
        >>> get_discount({2,32,50,86},0.25)
        output: 127.5
    
    """
    
    if not ( 0 <= percent <= 1):
        raise ValueError(f"Invalid discount rate: {percent}. Must be between 0 and 1")
    
    if  not all(isinstance(price, (int,float)) and price >= 0 for price in prices):
        raise ValueError("All prices must be non-negative numbers")
    
    total: float = sum(prices)

    return total * (1-percent)

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

def my_dict_binary(dictionaries:list[dict[str,Any]],
                   key:str,
                   target:str)->int: 
    """
    Performs a binary search on a sorted list of dictionaries.
    
    NOTE: The list of dictionaries MUST be sorted by the given 'key'
    before calling this function.
    
    Example: sorted_dicts.sort(key=lambda d: d['age'])
    """
    
 
    start:int=0
    end:int=len(dictionaries)-1

    while start <= end:
        mid:int= (start + end) // 2

        try: 

            middle_value = dictionaries[mid][key]

        except KeyError: 
            return -1
            
        if middle_value == target: return mid

        if middle_value < target: start = mid +1

        else: end = mid -1


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

    
    

#29/08/2025
def get_most_common_dict(dictionaries:list[dict[str,Any]],_key:Any,n:int=3,/)->list:
    """
    This funtion will count the most common in a series of dictionaries based of a certain 
    provided key. It will raise a KeyError if the key provided does not exist...
    you can decided how many vaues using the parameter n, it will be 3 as a default
    
    """
    if len(dictionaries) <=0: 
        raise ValueError("The list is empty ")
    


    new_list:list=[values[_key] for values in dictionaries if values.get(_key) is not None]

    counter=Counter(new_list)
    top_:list=[x for x,z in counter.most_common(n)]


    return top_