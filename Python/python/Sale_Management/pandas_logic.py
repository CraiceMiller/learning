import pandas as pd
import os 
import subprocess
from tkinter import messagebox
from typing import Any

def add_more_rows_excel(file_name:str,
                        sheet_name_:str='sheet1',
                        add_row:dict[Any,Any] |None=None,
                        with_index:bool=False,
                        display_message:bool=True)->None:
    """
    DESCRIPTION:    
        This funtion will add new rows base of the info given, it will show a message if 
        a problem occurs or do nothing if without value is provied. 
    
    PARAMETERS:

        file_name: this only must be a string,could can chose whether to writer 
         .xlsx or not because  the .xlsx with be added automally
        sheet_name_: this only provided the sheet name, sheet1 otherwise
        with_index: if you want index or not, False as a default 
        add_row: this is the main info that you wanna add. it must be a dictionary
        with string as key, list as value

    
    RETURN: 
        Nothing..
    
    """
    #1. write the documentations


    #2. do nothing if there is no data
    if  add_row is None:
        return 
    
    #3. this is a filter if the file name have xlsx in the end of the name, ro provide any erros 
    if not file_name.endswith(".xlsx"):
        file_name=file_name + ".xlsx"


    

    try: 
        #4. if the file indeed exist 
        if os.path.exists(file_name):
            all_sheets: dict =pd.read_excel(file_name, sheet_name=None, engine='openpyxl')

            #Get the specif sheet we want, or it will create a new empty DateFrame object
            df:pd.DataFrame = all_sheets.get(sheet_name_,pd.DataFrame())
     

        #4.1. if the file does not exist, will create a new empty DateFrame object
        else: 
            all_sheets:dict={} #type: ignore
            df = pd.DataFrame()

        #5. create a new DateFrame with the data provide: add_row
        nw_row=pd.DataFrame(add_row)

        #6. this method will add a new ROW in the sheet at hand
        df = pd.concat([df,nw_row],ignore_index=True)

        #7.Here is update the value ( is the same like a normal dict)
        all_sheets[sheet_name_] = df
        
        #The main code of the function: 
        #this will create a new file if the file is not found or modify the file and the sheet
        #provided
        with pd.ExcelWriter(file_name,mode='w',engine='openpyxl') as writer:#type: ignore
            for name, dataframe in all_sheets.items():
                dataframe.to_excel(writer, sheet_name=name, index=with_index)

            if display_message:
                messagebox.showinfo("Complet", "the modification was sucefully done!")

    #if a problem occurs, this except blocks will run 
    except PermissionError:
        messagebox.showerror("Permission Error", "Maybe you forgot to close the current file?")
    except Exception as e:
        print(e)
        messagebox.showerror("Error", f"Something went wrong: {e}")

def get_code_excel(file_name:str,
                   sheet_name_:str)->int:
    """
    DESCRIPTION: 
        This funtion will only attempt to get the last number of code in a existend excel 
        file. And if the file does not exist, there is no a colum call 'Code' or the Code 
        colum is None (null), it will reaturn 2400 as a default 
    RETURN:
        An integer object 
        The last code plus one in a existing excel file, 2400 otherwise
    
    """
    
    if not file_name.endswith(".xlsx"): 
        file_name= file_name +".xlsx"

    if os.path.exists(file_name):
        try: 
            df= pd.read_excel(file_name,sheet_name=sheet_name_)

            if "Code" in df.columns and not df["Code"].isnull().all(): 
                return int(df["Code"].max()) + 1
            
        except: 
            pass

    return 2400
