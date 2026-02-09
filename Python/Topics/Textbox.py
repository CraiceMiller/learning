from tkinter import *



# Create the main window
root = Tk()
root.config(bg="black")
root.title("Everyting's gonna be okay :)")

text = Text()

text.pack()


# just create a texbox
entry = Entry()
entry.config(bg="blue", fg="white", font=("Open Sans", 20), relief="sunken", width=30)

entry.pack(pady=2)
print()
#


#



def submit():
    guess = entry.get() 
    if guess == "":
        print("please write someting")
    elif guess == "0001":
        print("correct the answer was: " + guess)
    else:
        print("Wrong guess again!!")

#
mit = Button(root,text="submit",command=submit)
mit.pack(side=BOTTOM)

root.mainloop()