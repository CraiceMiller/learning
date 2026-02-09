import tkinter as tk
from tkinter import ttk
#Creating the window
window=tk.Tk()
window.geometry("400x500")
window.config(bg="black")
window.title("Learning new things today :3")

#creating the tkinker variables
str_var=tk.StringVar()
int_var=tk.IntVar()
bool_var=tk.BooleanVar()
double_var=tk.DoubleVar() 




#4. creating funtions
def get_current_item(event)->None:
    display_text.config(text=f"You pick: {str_var.get()}")

def guess_fv_anime()->None:
    if str_var.get() =="Nazo no Kanojo X":
        second_label.config(text="Yes, Nazo no Kanojo X is my favorite anime!!!")
    else:
        second_label.config(text=f"No, {str_var.get()} is not my favorite anime, try agian ")



#1. creting normal variables 
my_anime_list=["Nichijou","Re:Zero","No Game No Life","Lucky Star","Nazo no Kanojo X","Jojo's","Pokemon","Full Metal Alchemist"]

#2. creting ComboBox
anime_combox=ttk.Combobox(window,
             textvariable=str_var,
             values=my_anime_list,
             state="readonly"
             )
anime_combox.pack(pady=10)


#anime_combox.current(1)
#3. creating the, well, i see this like a button...
anime_combox.bind("<<ComboboxSelected>>",get_current_item)


#5.creating the label 
display_text=tk.Label(window,text="Pick an anime",width=25,height=3)
display_text.pack(pady=10)


#6. creting button and second label 
tk.Button(window,command=guess_fv_anime,width=10,height=2,text="Guess").pack(pady=10)
second_label=tk.Label(window,text="Guess my favorite anime",width=35,height=4)
second_label.pack(pady=10)



#starting the main window
if __name__ =="__main__":
    window.mainloop()