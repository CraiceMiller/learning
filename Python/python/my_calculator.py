from tkinter import Label,Button,Entry,StringVar,Tk,Frame

#Here are the principal functions at hand....
"""
i think that number1.get() the only thing it does is 
unpacking the string inside the StringVar variable
"""

def multiplication()->None:
    try:
        x:float=float(number1.get())
        y:float=float(number2.get())
        product:float=x * y

        result.config(text=f"Result is: {product:,}")

    except ValueError: 
        result.config(text="Please write only numbers...")

def Subtraction()->None:
    try:
        x:float=float(number1.get())
        y:float=float(number2.get())
        product:float=x - y

        result.config(text=f"Result is: {product:,}")

    except ValueError: 
        result.config(text="Please write only numbers...")


def Addition()->None:
    try:
        x:float=float(number1.get())
        y:float=float(number2.get())
        product:float=x + y

        result.config(text=f"Result is: {product:,}")

    except ValueError: 
        result.config(text="Please write only numbers...")

def Division()->None:
    try:
        x:float=float(number1.get())
        y:float=float(number2.get())
        product:float=x / y

        result.config(text=f"Result is: {product:,}")
    except ZeroDivisionError as e:
        result.config(text=f"An error has occured {e}")
    except ValueError: 
        result.config(text="Please write only numbers...")



#Creting the form that i will use 
form:Tk=Tk()
form.title("My Calculator ")
form.geometry("400x400")


number1:StringVar=StringVar()  
"""
i think this is the like a normal variale 
name:str='hersy'
age:int=18

and when we use GUI, I think it acts the same:
number1:StringVar=tk.StringVar()

name:StringVar=tk.StringVar()

both are varible that we can use whatever we want.
however, StringVar will only be a string... 

"""

number2:StringVar=StringVar()

number1.set("0")# i thin this is a default value we want to storage


#this just create a label 
Label(form, text="Number NO.1 ",font=("Arial",15)).pack(pady=10)
#this only create a textbox
Entry(form, textvariable=number1, width=20).pack()


#this just create a label Number 2
att:Label=Label(form, text="Number NO.2 ", font=("Arial",15))
att.pack(pady=10)
#this only create a textbox
Entry(form, textvariable=number2, width=20).pack()




#creating buttons 


button_frame:Frame = Frame(form)
button_frame.pack(pady=20) 

Button(button_frame, text="Multiplication", command=multiplication, bg="orange",fg="white", width=6, height=3).pack(side="left", padx=5)
Button(button_frame, text="Subtraction", bg="red", fg="white", command=Subtraction).pack(side="left", padx=5)
Button(button_frame, text="Addition", bg="blue", fg="white", command=Addition).pack(side="left", padx=5)
Button(button_frame, text="Division", bg="black", fg="white", command=Division).pack(side="left", padx=5)



"""
i think the parameter command=, only storage that funtion we want...
and it becomes the purpose of the button....

"""




# i think this is just a label :|
result:Label= Label(form,text="Result: ", font=("Helvetica", 20, "bold"))
result.pack(pady=25)



#Initilazing the window
form.mainloop()