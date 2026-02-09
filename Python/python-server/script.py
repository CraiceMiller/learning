from mypython.decorators import time #type: ignore
from typing import Callable, Coroutine,overload,Literal
import pandas as pd #type: ignore
import json  
import asyncio
from concurrent.futures import Future
import requests as r  #type: ignore
from  flask import Flask,jsonify
import flask 



#Read json ------------------------------------------------------------------------------->

@overload
async def read_json(self, filePath:str,data_frame:Literal[False],/)->list[dict]: 
        ...

@overload
async def read_json(self, filePath:str,/)->pd.DataFrame: 
        ...

async def read_json(self, filePath:str,data_frame:bool=True): 
    """
        This methos will attempt to open a file in read mode('r') and return base of paramter given. 
        if a problem occurs, it will raturn an empty object based of the second parameter provided. 

        Return: 
            if data_frame is True, it will return a DataFrame object.
            if data_frame is False, it will return a list of dictionaries storage of the in the file
    """
        
    if data_frame: 
        data=pd.DataFrame()
    else: 
        data=[] #type:  ignore 

    try: 
            with open(file=filePath,mode="r",encoding='utf-8') as file: 
                #self.storage_historial(filePath,"Read")
                try: 
                    if data_frame:

                        return pd.read_json(file)
                    
                    else: 
                        return json.load(file)

                
                except Exception :
                    return data
              
    except Exception as e: 
            print( "Problem at: " +  self.read_json.__name__)
            print(e)
            return data



#FUTURES ------------------------------------------------------------------------------->
def complet(done=False, text=""): 
    return Future( )


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


def display(list_:list[dict]):
    for x in list_: 
        for key,value in x.items():
            print(key,"= ", value)
        print()

    print("Done")



@time
async def main ()->None:
    path= r"C:\Users\Usuario Pc\Desktop\programming\data\User Accounts.json"
 
    await doTask(read_json,
                 display,
                 path,False)
    
asyncio.run(main())


#LEARNING HOW TO USE AN API ___________________________________________________________________________________


