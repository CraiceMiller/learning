#GUI Loops
import tkinter as tk 

window = tk.Tk()
window.geometry("300x300")
window.title("Simple Counter")

number: int = 10 
id_: str| None = None 

#normal loop
        
#the for keyword the new variable(i) and the iterable: in this case is range()
for i in range(number,0,-1): 
    #the code will be here 
    print(f"Number No {i}") 
#this for funtion will stop automatly untill the iterable has nothing left 


#GUI loop 
# the def keyword the name of the function (my_loop)
def my_loop()->None:
    global number #stablish the global variable 
    global id_ #stablish the glocal variable that will storage the .after() method

    #the code will be here 
    number -= 1
    label_.config(text=f"Number No {number}") 

    #storaging the unique id that will have our after method 
    #and for me, i think it'll be way easy if we write this in the last line of our funtion
    id_=label_.after(1000,my_loop) 

#and we need to stop the  GUI loop manually with another funtion 
def stop_loop()->None:
    global id_
    #with this if statement we are ensuring that the id_ has storage something
    #if it doesn't have anything this will never occur
    if id_:
        label_.after_cancel(id_)

#i think the adventage og gui loop is we can code a lot of this here, like new if statements, so on
#and the disadventage is it needs more code (a little more complexting)
    
    
  

label_ = tk.Label(window, width=30, height=5, bg="black", fg="cyan", 
                   text=f"Number No. {number}", font=("Helvetica", 24)) 
label_.pack(pady=10, fill="both", expand=True)


start_button = tk.Button(window, command=my_loop, width=15, text="Start Counter")
start_button.pack(pady=5)

stop_button = tk.Button(window, command=stop_loop, width=15, text="Stop Counter")
stop_button.pack(pady=5)

window.mainloop()