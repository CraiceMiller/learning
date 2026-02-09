import tkinter as tk
from tkinter import ttk
window=tk.Tk()
window.geometry("400x500")
window.config(bg="black")
window.title("Learning new things today :3")

#creating the tkinker variables
str_var=tk.StringVar()
int_var=tk.IntVar()
bool_var=tk.BooleanVar()
double_var=tk.DoubleVar() 


#trying to create radiobutton
tk.Radiobutton(window,width=10,variable=str_var,text="Credit Card",value="Credit Card").pack(pady=10)
tk.Radiobutton(window,width=10,variable=str_var,text="Debit Card",value="Debit Card").pack(pady=10)

#creating the label
Label_=tk.Label(window,textvariable=str_var,font=("Helvetica",10,"bold"))
Label_.pack(pady=10)

tk.Label(window,textvariable=int_var, width=10).pack(pady=10)
tk.Label(window,textvariable=bool_var, width=10).pack(pady=10)
tk.Label(window,textvariable=double_var, width=10).pack(pady=10)

#creating checkbutton
tk.Checkbutton(window,variable=bool_var,text="Study math").pack(pady=10)
tk.Checkbutton(window,text="Watch Anime",variable=double_var).pack(pady=10)




#Buttons
numbers=tk.Frame(window,width=10)
numbers.pack()

tk.Button(numbers,command=lambda:int_var.set(int_var.get()+1),text="Add number",width=10,bg="blue").pack(pady=10,side="left")
tk.Button(numbers,command=lambda:int_var.set(int_var.get()-1),text="Delate number",width=10,bg="red").pack(pady=10,side="left")


#entry
tk.Entry(window,textvariable=int_var,width=10).pack(pady=10)


#starting the main window
if __name__ =="__main__":
    window.mainloop()