import customtkinter as ctk #type: ignore

from tkinter import messagebox
from tkinter import ttk
import os 
from datetime import datetime 
import subprocess
import numpy as np 


"""
well, with this tiny project, i show you everythin i learned regards to 
customtkinter, for the moment only that, sorry ...

"""



#2.2 creaing funtions
def greet()->None:
    name=entry_var.get()
    person=person_var.get()
    gender=gender_var.get()

    if all((name,person,gender)):
        string_var.set(value=f"Hello dear {name}, you are a {gender} {person} Nice to meet you ")
        return 
    
    if name and person: 
        string_var.set(value=f"Hello dear {name}, you are a  {person} Nice to meet you ")
        return 
    
    if name and gender:
        string_var.set(value=f"Hello dear {name}, you are a {gender}, Nice to meet you ")
        return 
    
    if name: 
        string_var.set(value=f"Hello dear {name}, Nice to meet you ")
        return 


    string_var.set(value="Hello dear User, Nice to meet you ")

def afterwards()->None:
    name=entry_var.get()
    if name:
        string_var.set(value=f"Bye dear {name} ")
        return 


    string_var.set(value="Bye dear user")

def dark_mode()->None:
    messagebox.showinfo("Dark mode","Dark mode activated")
    ctk.set_appearance_mode("dark")

def light_mode()->None:
   ctk.set_appearance_mode("light") 



#here is where i set the dark mode
ctk.set_appearance_mode("system")
#and i think this method that the default color of every widget i creat (eg. button) has this color
ctk.set_default_color_theme("blue") 

# 0. Create the main application window, same like tkinter
app = ctk.CTk()
app.title("Learning new things every day :)")
app.geometry("400x500")
#app.set_appearance_mode("dark") #but i have a question why i cannot do this?

#1. creating the ctk variable like a do in a normal tkinter
string_var= ctk.StringVar()
person_var= ctk.StringVar()
entry_var= ctk.StringVar()
gender_var= ctk.StringVar()

string_var.set("Hi :3")
#craing normal variables 
my_list:list[str]=["student","teacher","parent"]

#2. creating the thing i already know
#label 
label_=ctk.CTkLabel(app,width=10,textvariable=string_var)
label_.pack(pady=20)

#entry
frame=ctk.CTkFrame(app)
frame.pack(pady=10)
ctk.CTkLabel(frame,width=10,text="Entry your  name: ").pack(padx=10,side="left")
ctk.CTkEntry(frame,width=80, height=10,textvariable=entry_var).pack(padx=10,side="left")

#button and frame
frame=ctk.CTkFrame(app)
frame.pack(pady=10)




ctk.CTkButton(frame,command=greet,text="Greet").pack(padx=10,side="left")
ctk.CTkButton(frame,command=afterwards,text="Afterwards").pack(padx=10,side="left")

#radiobutton
frame=ctk.CTkFrame(app)
frame.pack(pady=10)


ctk.CTkRadioButton(frame,value="Female",variable=gender_var,text="Female").pack(padx=10,side="left")
ctk.CTkRadioButton(frame,value="Male",variable=gender_var,text="Male").pack(padx=10,side="left")

#combobox
# combobox
ctk.CTkComboBox(app,
                values=my_list,
                state="readonly",
                variable=person_var).pack(pady=10)

#
frame=ctk.CTkFrame(app)
frame.pack(pady=10)


ctk.CTkButton(frame,command=dark_mode,text="dark mode").pack(padx=10,side="left")
ctk.CTkButton(frame,command=light_mode,text="light mode").pack(padx=10,side="left")

#

canvas = ctk.CTkCanvas(app)
canvas.pack(pady=10)
ctk.CTkSwitch(app,text="Swith",command=dark_mode).pack()




#Run the main application loop, like i always do in the normal tkinter
app.mainloop()







