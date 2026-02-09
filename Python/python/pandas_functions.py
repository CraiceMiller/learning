
from tkinter import messagebox
import pandas as pd 
import os
from typing import Any

def add_more_rows_excel(file_name:str,
                        sheet_name_:str='sheet1',
                        add_row:dict[Any,Any] |None=None,
                        with_index:bool=False)->None:
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
    if not add_row:
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

        
            messagebox.showinfo("Complet", "the modification was sucefully done!")

    #if a problem occurs, this except blocks will run 
    except PermissionError:
        messagebox.showerror("Permission Error", "Maybe you forgot to close the current file?")
    except Exception as e:
        print(e)
        messagebox.showerror("Error", f"Something went wrong: {e}")














if __name__ == '__main__22': 

    """
    add_more_rows_excel('My attempt.xlsx','Products',new_product5)
    add_more_rows_excel('My attempt.xlsx','More_products',new_product5)
    add_more_rows_excel('My attempt','Products',new_product5)
    add_more_rows_excel('My attempt','I dunno why ...',new_product5)
    """
    #df=pd.read_excel('My attempt.xlsx',sheet_name='Numbers')
    #list_= pd.DataFrame({'y':[10,20,30],'z':[90,80,70]})
    #df=pd.concat([df,list_])

    df=pd.DataFrame()
    try: 
        with pd.ExcelWriter('I got lost.xlsx', mode='w', engine='openpyxl') as writer: 
            df.to_excel(writer,sheet_name='Why')
    except: 
        pass
        

    #and how to create new sheets in the same file 
    df =pd.DataFrame()
    with pd.ExcelWriter('I got lost.xlsx', mode='a',engine='openpyxl',if_sheet_exists='overlay') as writer: 
        df.to_excel(writer,sheet_name='How')

    #and how to insert a table 
    df= pd.DataFrame({'a':[1,2,3],'b':[7,8,9]})
    with pd.ExcelWriter('I got lost.xlsx', mode='a',engine='openpyxl',if_sheet_exists='overlay') as writer: 
        df.to_excel(writer,sheet_name='Who')

    #and how to modifify existing sheets
    df=pd.read_excel('I got lost.xlsx', sheet_name='How')
    list_= pd.DataFrame({'y':[10,20,30],'z':[90,80,70]})
    df=pd.concat([df,list_],ignore_index=True)

    with pd.ExcelWriter('I got lost.xlsx', mode='a',engine='openpyxl',if_sheet_exists='overlay') as writer: 
        df.to_excel(writer,sheet_name='How')

    with pd.ExcelWriter('I got lost.xlsx', mode='a',engine='openpyxl',if_sheet_exists='overlay') as writer: 
        df.to_excel(writer,sheet_name='What')

    df=pd.read_excel('I got lost.xlsx', sheet_name='Who')
    list_= pd.DataFrame({'c':[11,22,33],'d':[99,88,77],'a':[4,5,6]})
    df=pd.concat([df,list_],ignore_index=True)
    
    with pd.ExcelWriter('I got lost.xlsx', mode='a',engine='openpyxl',if_sheet_exists='overlay') as writer: 
        df.to_excel(writer,sheet_name='Who')



    print("What is wrong with me !!")
    #sorry for be so lame .. 