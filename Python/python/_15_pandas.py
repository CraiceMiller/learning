#1. we need to import pandas as pd
import pandas as pd 
#09/08/25

sales_data = {
    'Product_ID': ['P101', 'P102', 'P103', 'P104', 'P105', 'P106', 'P107', 'P108', 'P109', 'P110'],
    'Product_Name': ['Laptop', 'Mouse', 'Keyboard', 'Monitor', 'Webcam', 'Speaker', 'Headphones', 'Microphone', 'Router', 'Printer'],
    'Category': ['Electronics', 'Accessories', 'Accessories', 'Electronics', 'Peripherals', 'Audio', 'Audio', 'Audio', 'Networking', 'Peripherals'],
    'Price_USD': [1200.50, 25.99, 75.00, 350.75, 59.50, 89.99, 110.00, 79.99, 150.00, 250.25],
    'Quantity_Sold': [15, 120, 85, 30, 95, 45, 60, 55, 20, 10],
    'In_Stock': [True, True, True, False, True, True, True, False, True, False],
    'Rating': [4.5, 4.7, 4.3, 4.8, 4.6, 4.4, 4.9, 4.2, 4.1, 4.0]
}
#this only will create a DateFrame of the local script, like my sale_data dictionary
data_frame=pd.DataFrame(sales_data)

#i don't need this method anymore cuz i already save it
#data_fame.to_excel("Sale_Management.xlsx",index=True) 


#When i already create a file, or if a want to work with a exist file
# i can use the method .red_excel(), or another file i want to read
#and this will be treaet as a DataFrame, Therefore it wil have all the methods
# a nomral DataFrame have
df = pd.read_excel("Sale_Management.xlsx","Sheet1")
df_2= pd.read_excel("my_friends.xlsx",'New_Friends')
df_3= pd.read_json("Sale_Management.json")
df_4= pd.read_json("my_first_json.json")
df_5= pd.read_excel("my_friends.xlsx")

#i see this syntax like a if statement...
print(df[df["Category"]=='Electronics'])

#Some of methods of DataFrame object: 
#this only will show us the first 5 data in our file... but we add how many we want to watch
print(df.head(n=2))
print()

#to see the last ones
print(df.tail(n=3))
print()

#i think this will give us data in a random way
print(df.sample(4))
print()

#i dunno
print(df.sample(frac=0.2,random_state=7))
print()
#this only will give us the names of the columns i guess, but i dunno what it returns
print(df.columns)
print()

#i dunno
print(df.index)
print()

#a summary of the all the info storage in the file 
df.info()
print()

#a summary but more summary
df.info(verbose=False)
print()

#i dunno, i guess, this will give us basic statistics info like the max or min or average
#but only of the colums that has numbers
print(df.describe())
print()

#the same but with non-numeral columns
print(df["Category"].describe())
print()

#i dunno 
print(df.shape)
print(len(df))
print()

#Subsettings a DataFrame 
"""
i think that this one is like we do in a normal dict
example
my_dict={"a":2,"b":3}
print(my_dict["a"])
output: 2

the same logic applies here, but we need to use double square brackets
"""
print(df[["Category",'Price_USD']])
print()

#so far, what i can undertand is a DataFrame object resembles a dictionary in pyton, 
#in the majority at least...
print(df[df.columns[:2]])
print()

#list conprehesion using DataFrame
#i dunno how this list works
print(df[[c for c in df.columns if 'Quantity_Sold' in c]])
print()

#i dunno what is the differents yet
print(df['Product_Name'])
print()
print(df[['Product_Name']])

#Rolling methods 
#i dunno 
print(df[['Quantity_Sold']].rolling(window=6).mean())
print()

#i dunno 
print(df[['Quantity_Sold']].clip(100,200))
print()

#i dunno 
print(df.groupby('Quantity_Sold')[['Product_Name']])
print()

#NEW COLUMNS 
#i dunno
df["Country"]= None #i have an issue here, why this column doesn't add in my excel file?
print()

#i dunno 
df.assign(Average = None)
print(df)
print()

#Soring data
#what heck i going on here... my mind ...
print(df[['Product_Name','Quantity_Sold']].sort_values('Product_Name',ascending=False)\
      .reset_index(drop=True))


#Well this is pretty much it , i guess , to be honest, i still find so hard undertand the 
#majority of info here, and how should i use them....

import pandas as pd
from datetime import datetime

# 1. Load the existing Excel file into a DataFrame
try:
    df = pd.read_excel("Sale_Management.xlsx")
    print("DataFrame loaded successfully.")

    # 2. Create a new column with a calculation
    # We are calculating the total sales for each product
    df['Total_Sales_USD'] = df['Price_USD'] * df['Quantity_Sold']
    
    # 3. Create another new column with a constant value
    # Let's add a date when the data was processed
    df['Date_Processed'] = datetime.now().strftime('%Y-%m-%d')
    df['Country']= None
    df['Clients']=['hersy','craice','sthephany','hersy','craice','ashley','sthephany','misery','craice','craice']
    
    # Let's print the DataFrame to see the new columns
    print("\n--- DataFrame with New Columns ---")
    print(df.head())
    
    # 4. Save the updated DataFrame back to the SAME Excel file
    # This will overwrite the old file with the new data
    # We use index=False so we don't save an extra column with the row numbers
    df.to_excel("Sale_Management.xlsx", index=False)
    
    print("\nDataFrame saved successfully with new columns to 'Sale_Management.xlsx'.")
    
except FileNotFoundError:
    print("Error: The file 'Sale_Management.xlsx' was not found.")
except ValueError as e:
    print(e)
except PermissionError as e:
    print(e)
    