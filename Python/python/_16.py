import pandas as pd 


sales_data = {
    'Product_ID': ['P101', 'P102', 'P103', 'P104', 'P105', 'P106', 'P107', 'P108', 'P109', 'P110'],
    'Product_Name': ['Laptop', 'Mouse', 'Keyboard', 'Monitor', 'Webcam', 'Speaker', 'Headphones', 'Microphone', 'Router', 'Printer'],
    'Category': ['Electronics', 'Accessories', 'Accessories', 'Electronics', 'Peripherals', 'Audio', 'Audio', 'Audio', 'Networking', 'Peripherals'],
    'Price_USD': [1200.50, 25.99, 75.00, 350.75, 59.50, 89.99, 110.00, 79.99, 150.00, 250.25],
    'Quantity_Sold': [15, 120, 85, 30, 95, 45, 60, 55, 20, 10],
    'In_Stock': [True, True, True, False, True, True, True, False, True, False],
    'Rating': [4.5, 4.7, 4.3, 4.8, 4.6, 4.4, 4.9, 4.2, 4.1, 4.0]
}

#craing the dateframe object
df=pd.DataFrame(sales_data)


#creating the new columns 
df['Total_Revenue'] = df['Price_USD'] * df['Quantity_Sold']

#

# This is our new data, as a dictionary
new_product = {
    'Product_ID': ['P112'],
    'Product_Name': ['Phone'],
    'Category': ['Electronics'],
    'Price_USD': [651.50],
    'Quantity_Sold': [265],
    'In_Stock': [True],
    'Rating': [6.6]
}

new_product2 = {
    'Product_ID': ['P113'],
    'Product_Name': ['Webcam'],
    'Category': ['Peripherals'],
    'Price_USD': [59.50],
    'Quantity_Sold': [95],
    'In_Stock': [True],
    'Rating': [4.6]
}

new_product3 = {
    'Product_ID': ['P114'],
    'Product_Name': ['Table'],
    'Category': ['Electronics'],
    'Price_USD': [600.50],
    'Quantity_Sold': [100],
    'In_Stock': [True],
    'Rating': [8]
}

# Convert the new data to a DataFrame
new_row_df = pd.DataFrame(new_product)
new_row_df2 = pd.DataFrame(new_product2)
new_row_df3 = pd.DataFrame(new_product3)


"""
#addinf more data in a existing file 
df = pd.read_excel("Sale_Management.xlsx")


new_product4 = {
    'Product_ID': ['P115'],
    'Product_Name': ['MousePad'],
    'Category': ['Accessories'],
    'Price_USD': [60.50],
    'Quantity_Sold': [25],
    'In_Stock': [True],
    'Rating': [8]
}

new_row_df4= pd.DataFrame(new_product4)

df = pd.concat([df, new_row_df4], ignore_index=True)
df['Total_Revenue'] = df['Price_USD'] * df['Quantity_Sold']

try: 
    with pd.ExcelWriter("Sale_Management.xlsx", engine='openpyxl', mode='a', if_sheet_exists='overlay') as writer:
        df.to_excel(writer, sheet_name='Products', index=False)

except FileNotFoundError as e:
    print(e)
except PermissionError as e:
    print(e)
except ValueError as e :
    print(e)
"""

from typing import Any
from tkinter import messagebox
import pandas as pd 
def add_more_data_excel(file_name:str,
                        sheet_name_:str='sheet1',
                        add_row:dict[str,list] |None=None,
                        with_index:bool=False)->None:
    """
    DESCRIPTION:    
        This funtion will add new rows base of the info given, it will show a message if 
        occurs a problem or do nothing if without value is provied. 
    
    PARAMETERS:

        file_name: this only must be a string, since the .xlsx with be added automally
        sheet_name_: this only provided the sheet name, sheet1 otherwise
        with_index: if you want index or not, False as a default 
        add_row: this is the main info that you wanna add. it must be a dictionary
        with string as key, list as value

    
    RETURN: 
        Nothing..
    
    """
    
    if not add_row:
        return 
    
    file_name=file_name + ".xlsx"
    df= pd.read_excel(file_name)


    nw_row=pd.DataFrame(add_row)
    df = pd.concat([df,nw_row],ignore_index=True)

    try: 

        with pd.ExcelWriter(file_name,mode='a',if_sheet_exists='overlay',engine='openpyxl') as writer:
            df.to_excel(writer,sheet_name=sheet_name_,index=with_index)

        
            messagebox.showinfo("Complet", "the modification was sucefully done!")

            
    except FileNotFoundError as e: 
        messagebox.showerror(f'{e}',f"The file {file_name} was not found!  ")

    except PermissionError as e:
        messagebox.showerror(f'{e}',f"Maybe you forgot to close the current file?")
    
    except : 
        print("i dunno ")


new_product5:dict[str,list] = {
    'Product_ID': ['P116'],
    'Product_Name': ['Iphone!'],
    'Category': ['Electronics'],
    'Price_USD': [700.50],
    'Quantity_Sold': [1000],
    'In_Stock': [True],
    'Rating': [9]
}

add_more_data_excel("Sale_Management",'Products',new_product5)






#creting a new DataFrame
high_rated_products = df[df["Rating"] >= 4.5]


#the average of the high_rated_products
print(high_rated_products['Total_Revenue'].mean())

#storage all the info into a new sheet in the same file 

try:
    with pd.ExcelWriter(path="Sale_Management_.xlsx", engine='openpyxl', mode='a',if_sheet_exists='overlay') as writer:
        print("The file has oppened succefully")

        high_rated_products.to_excel(writer,sheet_name= 'high_rated_products',index=False)
        print("the currently table has save sucefully")
 
except FileNotFoundError as e:
    print(e)
except PermissionError as e:
    print(e)
except ValueError as e :
    print(e)