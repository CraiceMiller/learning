import tkinter as tk


#funtions 
def display_numbers(number_str_var:tk.StringVar)->None:
    # 1. Get the current text 
    current_display_text:str = text_inside.get()

    # 2. Get the digit/symbol 
    digit_or_symbol:str = number_str_var.get()

    # 3. Concatenate them
    new_display_text:str = current_display_text + digit_or_symbol

    # 4. SET the new combined string back into the display label's StringVar
    text_inside.set(new_display_text) 

def display_parenthesis()->None:
    

    current_display_text:str = text_inside.get()

        

    if current_display_text.find("(")==-1:
            new_display_text:str = current_display_text + "("
            text_inside.set(new_display_text)
            return 
    else:
            new_display_text2:str = current_display_text + ")"
            text_inside.set(new_display_text2)
            return 


    
    
   





def delate_last_character()->None:
    current_text:str = text_inside.get() 
    if current_text: 
        new_text:str = current_text[:-1] 
        text_inside.set(new_text) 


def get_total()->None:
    current_text:str = text_inside.get() 
    try:
        result:str=str(eval(current_text))
        text_inside.set(result)
    except SyntaxError as e:
        text_inside.set(f"{e}")
    except ZeroDivisionError as e:
        text_inside.set(f"{e}")
    except TypeError as e:
        text_inside.set(f"{e}")


def delate_all_characters()->None:
    text_inside.set("")




#creating the main window
window:tk.Tk=tk.Tk()
window.title("Calculatror")
window.geometry("500x700")
window.config(bg="black")


#creating the variable 
text_inside=tk.StringVar()

#for numbers 
zero_ = tk.StringVar(value="0")
one_ = tk.StringVar(value="1")
two_ = tk.StringVar(value="2")
three_ = tk.StringVar(value="3")
four_ = tk.StringVar(value="4")
five_ = tk.StringVar(value="5") 
six_ = tk.StringVar(value="6")
seven_ = tk.StringVar(value="7")
eight_ = tk.StringVar(value="8")
nine_ = tk.StringVar(value="9")
# operators/dot/clear
dot_ = tk.StringVar(value=".")
plus_ = tk.StringVar(value="+")
minus_ = tk.StringVar(value="-")
times_ = tk.StringVar(value="*")
divide_ = tk.StringVar(value="/")

porcentage_=tk.StringVar(value="%")



#settle the main label 
label_1=tk.Label(window,bg="white",width=75, height=3, textvariable=text_inside, font=("Helvetica",40,"bold") )
label_1.pack(pady=5)


#tk.Entry(window, textvariable=text_inside, width=10).pack(pady=5)


#creating the buttons 
frame_space=tk.Frame(window,bg="black")
frame_space.pack(pady=2)

tk.Button(frame_space, height=1, width=3, text="AC", font=("Arial",40,"bold"),bg="#A5A5A5",fg="white", command=delate_all_characters).pack(padx=5, side="left")
tk.Button(frame_space, height=1, width=3, text="()", font=("Arial",40,"bold"),bg="#A5A5A5",fg="white",command=display_parenthesis).pack(padx=5, side="left")
tk.Button(frame_space, height=1, width=3, text="%", font=("Arial",40,"bold"),bg="#A5A5A5",fg="white",command=lambda: display_numbers(porcentage_)).pack(padx=5, side="left")
tk.Button(frame_space, height=1, width=3, text="/", font=("Arial",40,"bold"),bg="orange",fg="white", command=lambda: display_numbers(divide_)).pack(padx=5, side="left")





#creating the buttons 
frame_space=tk.Frame(window,bg="black")
frame_space.pack(pady=2)

tk.Button(frame_space, height=1, width=3, text="7", font=("Arial",40,"bold"),bg="#333333",fg="white", command=lambda: display_numbers(seven_)).pack(padx=5, side="left")
tk.Button(frame_space, height=1, width=3, text="8", font=("Arial",40,"bold"),bg="#333333",fg="white", command=lambda: display_numbers(eight_)).pack(padx=5, side="left")
tk.Button(frame_space, height=1, width=3, text="9", font=("Arial",40,"bold"),bg="#333333",fg="white",command=lambda: display_numbers(nine_)).pack(padx=5, side="left")
tk.Button(frame_space, height=1, width=3, text="*", font=("Arial",40,"bold"),bg="orange",fg="white",command=lambda: display_numbers(times_)).pack(padx=5, side="left")




#Second block 
frame_space=tk.Frame(window,bg="black")
frame_space.pack(pady=2)

tk.Button(frame_space, height=1, width=3, text="4", font=("Arial",40,"bold"),bg="#333333",fg="white",command=lambda: display_numbers(four_)).pack(padx=5, side="left")
tk.Button(frame_space, height=1, width=3, text="5", font=("Arial",40,"bold"),bg="#333333",fg="white",command=lambda: display_numbers(five_)).pack(padx=5, side="left")
tk.Button(frame_space, height=1, width=3, text="6", font=("Arial",40,"bold"),bg="#333333",fg="white",command=lambda: display_numbers(six_)).pack(padx=5, side="left")
tk.Button(frame_space, height=1, width=3, text="-", font=("Arial",40,"bold"),bg="orange",fg="white",command=lambda: display_numbers(minus_)).pack(padx=5, side="left")


#Third block
frame_space=tk.Frame(window,bg="black")
frame_space.pack(pady=2)

tk.Button(frame_space, height=1, width=3, text="1", font=("Arial",40,"bold"),bg="#333333",fg="white",command=lambda: display_numbers(one_)).pack(padx=5, side="left")
tk.Button(frame_space, height=1, width=3, text="2", font=("Arial",40,"bold"),bg="#333333",fg="white",command=lambda: display_numbers(two_)).pack(padx=5, side="left")
tk.Button(frame_space, height=1, width=3, text="3", font=("Arial",40,"bold"),bg="#333333",fg="white",command=lambda: display_numbers(three_)).pack(padx=5, side="left")
tk.Button(frame_space, height=1, width=3, text="+", font=("Arial",40,"bold"),bg="orange",fg="white",command=lambda: display_numbers(plus_)).pack(padx=5, side="left")

#fourth block
frame_space=tk.Frame(window,bg="black")
frame_space.pack(pady=2)

tk.Button(frame_space, height=1, width=3, text="0", font=("Arial",40,"bold"),bg="#333333",fg="white",command=lambda: display_numbers(zero_)).pack(padx=5, side="left")
tk.Button(frame_space, height=1, width=3, text=".", font=("Arial",40,"bold"),bg="#333333",fg="white",command=lambda: display_numbers(dot_)).pack(padx=5, side="left")
tk.Button(frame_space, height=1, width=3, text="=", font=("Arial",40,"bold"),bg="#333333",fg="white", command=get_total).pack(padx=5, side="left")
tk.Button(frame_space, height=1, width=3, text="C", font=("Arial",40,"bold"),bg="orange",fg="white", command=delate_last_character).pack(padx=5, side="left")







#running the code
if __name__ == "__main__":
    window.mainloop()