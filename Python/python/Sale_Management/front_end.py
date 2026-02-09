#11/08/2025
#1. importing the modules needed 
from tkinter import messagebox
from datetime import datetime 
import customtkinter as ctk #type: ignore
from tkinter import ttk
from pandas_logic import add_more_rows_excel,get_code_excel
import os
from tkinter.ttk import Treeview
from typing import Any,Literal


#2. i decided to create a class for this project
class ManagementApp(ctk.CTk):
    """
    DESCRIPTION: 
        This class create an little management app. 
    """

    Products: list[str] = [
    "Nintendo Switch","Nintendo Switch OLED","Nintendo Switch Lite","Wii U","Wii",
    "Nintendo 3DS","Nintendo DS","GameCube","Nintendo 64","SNES","NES","Game Boy",
    "The Legend of Zelda: Breath of the Wild","The Legend of Zelda: Tears of the Kingdom",
    "Super Mario Odyssey","Super Smash Bros. Ultimate","Mario Kart 8 Deluxe","Animal Crossing: New Horizons",
    "Pokémon Scarlet and Violet","Metroid Prime Remastered","Pikmin 4","Kirby and the Forgotten Land","Splatoon 3",
    "Fire Emblem Engage",
    "Xenoblade Chronicles 3","Mario Oddisy",
    "The Legend of Zelda","Pokémon","Metroid","Pikmin","Kirby","Amiibo",
    "Joy-Con controllers","Pro Controller"
    ]
    
    Storage_data:dict[str,list]={"Product":[],
                                "Customer":[],
                                "Distributor":[],
                                "Description":[],
                                "Price":[],
                                "Quantity":[],
                                "Total":[],
                                "Date":[],
                                "Code":[]}
    
    Distributors: list[str] = ["Amazon","Walmart", "FedEx", "Steam","Nintendo.com"]
    def __init__(self,
                 excel_file:str,
                 sheet_name:str,
                 aspect:Literal["dark","light","system"] = "dark"
                 ):
        super().__init__()
        
        #3. setting the CTK features
        ctk.set_appearance_mode(aspect)
        ctk.set_default_color_theme("green")
        self.title('Sale and Purchases Management app')
        self.geometry("1050x1000")
        window_color=self.cget("fg_color")

        #4. creating the varaibles needed
        self._excel_file:str=excel_file if excel_file.endswith(".xlsx") else excel_file + ".xlsx"
        self._sheet_name:str=sheet_name
        self._date=ctk.StringVar()
        self._total=ctk.StringVar()

        self._date.set(value=self.get_date())
        self._total.set(value="0.00")

    
        #5. creating the widgets
        
        #creating the main frame of the upper part 
        main_frame=ctk.CTkFrame(self, fg_color=window_color)
        main_frame.pack(padx=30, pady=10, fill="both")


        #5.1.Frames, combobox,Description and date
        frame=ctk.CTkFrame(main_frame, fg_color=window_color, width=300)
        frame.pack(pady=5, padx=20, side="left")

        self.product_combo= ctk.CTkComboBox(frame,values=ManagementApp.Products,state="readonly")
        self.product_combo.pack(pady=5, side="top",fill="x")

        self._description_entry=ctk.CTkEntry(frame,placeholder_text="Description")
        self._description_entry.pack(pady=5, side="top",fill="x")

        ctk.CTkEntry(frame,placeholder_text="Date",textvariable=self._date).pack(pady=5, side="top",fill="x")
        
        
        #5.2 Client, Deliver 
        main_frame2=ctk.CTkFrame(main_frame, fg_color=window_color)
        main_frame2.pack(pady=5, padx=20, side="left")

        frame=ctk.CTkFrame(main_frame2, fg_color=window_color)
        frame.pack(pady=5,padx=20, fill="x", side="top")

        self.customer_entry =ctk.CTkEntry(frame, width=190,placeholder_text="Customer/Phone" )
        self.customer_entry.pack(padx=15, side="left", fill="x")

        self.distributors_combo= ctk.CTkComboBox(frame,values=ManagementApp.Distributors,state="readonly",width=190)
        self.distributors_combo.pack(padx=15, side="left", fill="x")

        #5.3. Entry: Price, Quantity, Total 
        frame=ctk.CTkFrame(main_frame2, fg_color=window_color)
        frame.pack(pady=5,padx=20, fill="x", side="top")

        self.price_entry =ctk.CTkEntry(frame, width=190,placeholder_text="Price" )
        self.price_entry.pack(padx=5, side="left",)

        self.quantity_entry =ctk.CTkEntry(frame, width=190,placeholder_text="Quantity" )
        self.quantity_entry.pack(padx=5, side="left",)

        ctk.CTkEntry(frame, width=190,textvariable=self._total,state="disable").pack(padx=5, side="left",)


        #5.4. buttons
        frame=ctk.CTkFrame(main_frame2, fg_color=window_color)
        frame.pack(pady=5,padx=20, fill="x", side="top")

        ctk.CTkButton(frame, text="Save",command=self.save_data, corner_radius=50).pack(padx=5, side="left")
        ctk.CTkButton(frame, text="Clean",command=self.clean_data, corner_radius=50).pack(padx=5, side="left")
        ctk.CTkButton(frame, text="Open Excel",command=self.open_excel, corner_radius=50).pack(padx=5, side="left")



        #6. Creating the table i guess
        main_frame=ctk.CTkFrame(self, fg_color=window_color)
        main_frame.pack(padx=30, pady=10, fill="both")

        keys_:list[str]=list(ManagementApp.Storage_data.keys())

        self.table=Treeview(main_frame, columns=keys_, show='headings')

        for value in keys_:
             self.table.heading(value, text=value)
        self.table.pack(pady=10)


        
        
        #7. Creating the middle part
        main_frame=ctk.CTkFrame(self, fg_color=window_color)
        main_frame.pack(pady=10,padx=20,fill="x")

        """#7.1. labels, combobox, year and month
        ctk.CTkLabel(main_frame,text="Month").pack(padx=5,side="left")
        self.month_combo=ctk.CTkComboBox(main_frame)
        self.month_combo.pack(padx=5,side="left")
        """

        ctk.CTkButton(main_frame,corner_radius=50,width=50,
        text="Get Total", command=self.get_total).pack(padx=20,side="left")

        #ctk.CTkButton(main_frame,corner_radius=50,width=50,
        #text="Save data in excel", command=self.data_to_excel).pack(padx=20,side="right")
     

  
       
       
    #8. creating the functions
    @staticmethod
    def get_date()->str:
         return datetime.now().strftime("%d/%m/%Y")
    

    def display_data(self,list_:list)->None:
        """This will only display the info at the table"""
        self.table.insert(parent='',index=0,values=list_)

    def verifying_amount(self)->bool: 
         return self.price_entry.get().isdigit() and self.quantity_entry.get().isdigit()
 
        
    def open_excel(self)->None: 
            """
            DESCRIPTION: 
                This mehtod only open the excel file. Nontheless, if the file does not 
                exist will ask you want to create a blank excel file, with the given name
            """


            if os.path.exists(self._excel_file):
                os.startfile(self._excel_file)
                return 
            


            create:bool=messagebox.askyesno("No file was found","The file doesn't exist. "\
                                                "However, do you want to create a new blank excel file?")
                
            if create: 
                add_more_rows_excel(self._excel_file,self._sheet_name,{})
                return 

    def clean_data(self,display_message:bool=True)->None:
        """
        DESCRIPTION: 
            This method will only clean all the entries,and comboxes
        """
        if display_message: 
            if not messagebox.askyesno("Clean","Are you sure you want to clean all the info?"):
                return 

        self.product_combo.set(value="")
        self._description_entry.delete(0,"end")
        self._date.set(value=self.get_date())
        self.customer_entry.delete(0,"end")
        self.distributors_combo.set(value="")
        self.price_entry.delete(0,"end")
        self.quantity_entry.delete(0,"end")
        self._total.set(value="0.00")
         
    def save_data(self)->None:
        """
        DESCRIPTON: 
            This method will get all the info provide in the upper part of the application,
            and storage in a dictionarry. with the aim of Only display it in the consele,
            It does  NOT save th content into a excel file. 

            If all the needed info was not given it will show an error message. 
        """
        if not self.verifying_amount():
            messagebox.showerror("Error","The Price and Quantity Must be a number!")
            return 

        if self._total.get() == "0.00":
            messagebox.showerror("Error","Did you forgot to press the calculate button, perphas?")
            return 
        


        new_data:dict[str,Any]= {"Product":self.product_combo.get(),
                                "Customer":self.customer_entry.get(),
                                "Distributor":self.distributors_combo.get(),
                                "Description":self._description_entry.get(),
                                "Price":float(self.price_entry.get()),
                                "Quantity":int(self.quantity_entry.get()),
                                "Total":float(self._total.get()),
                                "Date":self._date.get(),
                                "Code":get_code_excel(self._excel_file,self._sheet_name)}



        if not all(new_data.values()):
             messagebox.showerror("Error", "You need to provide the info needed")
             return 
        
        new_data:dict[str,Any]= {"Product":[self.product_combo.get()], #type: ignore
                                "Customer":[self.customer_entry.get()],
                                "Distributor":[self.distributors_combo.get()],
                                "Description":[self._description_entry.get()],
                                "Price":[float(self.price_entry.get())],
                                "Quantity":[int(self.quantity_entry.get())],
                                "Total":[float(self._total.get())],
                                "Date":[self._date.get()],
                                "Code":[get_code_excel(self._excel_file,self._sheet_name)]}
   
        
        add_more_rows_excel(self._excel_file,self._sheet_name,new_data,False,False)
        self.display_data(list_=list(new_data.values()))
        self.clean_data(False)

        
    def get_total(self)->None: 
        if not self.verifying_amount():
            messagebox.showerror("Error","The Price and Quantity Must be a number!")
            return 
        
        
        
        price=float(self.price_entry.get())
        quantity=int(self.quantity_entry.get())

        total=price * quantity

        self._total.set(value=f"{total}")

    def data_to_excel(self)->None:
         """
         DESCRIPTION:
            This will crate a new excel file if there is no any, or will storage the data on it. 
            this will not do nothing if there is not any data in Storage_data dictionary 
         """
         if not all(ManagementApp.Storage_data.values()): 
            messagebox.showerror("Error","There is no data to storage!")
            return 
         
         add_more_rows_excel(self._excel_file,self._sheet_name,ManagementApp.Storage_data)
         ManagementApp.Storage_data.clear()
         all_items=self.table.get_children()
         self.table.delete(*all_items)
    
 



