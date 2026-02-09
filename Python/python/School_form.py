#27/07/2025
#update 05/08/2025: display_student()
#update 07/08/2025...
#Proyect: my mini form...
import tkinter as tk
from tkinter import ttk
from datetime import datetime
import speech_recognition as sr #type: ignore
from typing import Any
import customtkinter as ctk #type: ignore 





#cretinhg the window...
window=tk.Tk()
window.geometry("800x500")
window.config(bg="#C2C2C2")
window.title("School Form")


#creating tk variables 
id_number=tk.IntVar()
names=tk.StringVar()
lastnames=tk.StringVar()
age=tk.StringVar()
grade=tk.StringVar()
section=tk.StringVar()
phone_number=tk.StringVar()
gender=tk.StringVar()
email=tk.StringVar()


spanish_=tk.IntVar()
english_=tk.IntVar()
germany_=tk.IntVar()


id_number.set(1120)



#creating normals variables 
Students:list[dict]=[]
Grades_list:list[str]=["Computer bachelor","Bussiness Management","Chartered Accountant"]


#creating funtions 
def adding_new_students()->None:
    Languagues:dict={"Spanish":spanish_.get(),"English":english_.get(),"Germany":germany_.get()}
    

    if not all((names.get(),age.get(),grade.get(),gender.get())):
        verifyting.config(text="You need to type the important info")
        return 

    if not age.get().isdigit():
        verifyting.config(text="The age Must be a integer number")
        return 
    
    Students.append(
        {
        "ID": id_number.get(),
        "Names": names.get(),
         "Age": int(age.get()),
         "Last names":lastnames.get(),
         "Grade": grade.get(), 
         "Section": section.get(),
         "Phone number":phone_number.get(), 
         "Gender":gender.get(),
         "Email":email.get(),
         "Languages":[lan for lan in Languagues if Languagues[lan]==1],
         "Extra info": adding_more_info.get("1.0","end-1c"),
         }
    )
    verifyting.config(text=f"The student {names.get()}, has been added successfully")
    id_number.set(id_number.get()+1)
    delate_all()
    return 

def delate_all()->None:
    names.set("")
    names.set("")
    lastnames.set("")
    age.set("")
    grade.set("")
    section.set("")
    phone_number.set("")
    gender.set("")
    email.set("")
    spanish_.set(False)
    english_.set(False)
    germany_.set(False)
    adding_more_info.delete("1.0","end")

def display_student()->None:
    """For the moment being this only display it in the terminal"""
    if Students == []:
        print("No students here....")
        return 
    
    for student in Students:
        for key,value in student.items():
            if not value:
                continue

            print(f"{key}: {value}")
        print()


recognized:sr.Recognizer=sr.Recognizer()

    

def get_speech_input()->str: 
    """
    \nDescription: 
    \nThis only get what the user is trying to say, and display it in the console
    """
    

    with sr.Microphone() as source:
        verifyting.config(text="I'm listening, so say something....")
        recognized.adjust_for_ambient_noise(source)
        audio:Any=recognized.listen(source)

    try:
        text=recognized.recognize_google(audio)
        return text.lower()
    except sr.UnknownValueError:
        return "Sorry could you speak up, I couldn't make that out"
    except sr.RequestError as e:
        return f"Could not request the result: {e}"




def speak()->None:
    text=get_speech_input()
    adding_more_info.insert("1.0",text)


#creating the date
tk.Label(window,text=f"{datetime.now().strftime("%d/%m/%Y")}",bg="#C2C2C2").pack(side="top",pady=10)

#creating the feature of the main window
#1. Main Label
tk.Label(window,width=40,bg="black",font=("Helvetica",20,"bold"),fg="white",text="Welcome to Shinomiya High School.S.A").pack(pady=10)

#2. Names, Last names and age
frame=tk.Frame(window,bg="#C2C2C2")
frame.pack(pady=10)

tk.Label(frame, text="ID:",bg="#C2C2C2", fg="Black",font=("Helvetica",10,"bold")).pack(padx=1,side="left")
tk.Entry(frame,textvariable=id_number, state="disabled" ).pack(padx=5,side="left")

tk.Label(frame, text="Names:",bg="#C2C2C2",fg="black",font=("Helvetica",10,"bold")).pack(padx=1,side="left")
name_entry=tk.Entry(frame,textvariable=names )
name_entry.pack(padx=5,side="left")

tk.Label(frame, text="Last Names:",bg="#C2C2C2", fg="Black",font=("Helvetica",10,"bold")).pack(padx=1,side="left")
tk.Entry(frame,textvariable=lastnames ).pack(padx=5,side="left")

tk.Label(frame, text="Age:",bg="#C2C2C2", fg="Black",font=("Helvetica",10,"bold")).pack(padx=1,side="left")
tk.Entry(frame,textvariable=age ).pack(padx=5,side="left")


#3. grades, section, phones 
frame=tk.Frame(window,bg="#C2C2C2")
frame.pack(pady=10)

tk.Label(frame, text="Grade:",bg="#C2C2C2", fg="Black",font=("Helvetica",10,"bold")).pack(padx=1,side="left")

ttk.Combobox(frame,
    values=Grades_list,
    textvariable=grade,
    state="readonly"
).pack(padx=5,side="left")

tk.Label(frame, text="Section:",bg="#C2C2C2", fg="Black",font=("Helvetica",10,"bold")).pack(padx=1,side="left")
tk.Entry(frame,textvariable=section ).pack(padx=5,side="left")

tk.Label(frame, text="Phone Number:",bg="#C2C2C2", fg="Black",font=("Helvetica",10,"bold")).pack(padx=1,side="left")
tk.Entry(frame,textvariable=phone_number ).pack(padx=5,side="left")


#4. gender, email, langugues (check button)
frame=tk.Frame(window, bg="#C2C2C2")
frame.pack(pady=10)
tk.Label(frame, text="Gender:",bg="#C2C2C2", fg="Black",font=("Helvetica",10,"bold")).pack(padx=1,side="left")
tk.Radiobutton(frame, text="Female",variable=gender, value="Female",bg="#C2C2C2").pack(side="left",padx=5)
tk.Radiobutton(frame, text="Male",variable=gender, value="Male",bg="#C2C2C2").pack(side="left",padx=5)

tk.Label(frame, text="Email:",bg="#C2C2C2", fg="Black",font=("Helvetica",10,"bold")).pack(padx=1,side="left")
tk.Entry(frame,textvariable=email ).pack(padx=5,side="left")

tk.Label(frame, text="Languagues:",bg="#C2C2C2", fg="Black",font=("Helvetica",10,"bold")).pack(padx=1,side="left")
tk.Checkbutton(frame,text="Spanish",bg="#C2C2C2",variable=spanish_).pack(padx=10,side="left")
tk.Checkbutton(frame,text="English",bg="#C2C2C2",variable=english_).pack(padx=10,side="left")
tk.Checkbutton(frame,text="Germany",bg="#C2C2C2",variable=germany_).pack(padx=10,side="left")








#5. Extra info, (using microphone)
tk.Label(text="Extra Information:",bg="#C2C2C2").pack()

frame=tk.Frame(window, bg="#C2C2C2")
frame.pack(pady=10)

adding_more_info=tk.Text(frame,width=80,height=3)
adding_more_info.pack(padx=10,side="left")
tk.Button(frame,text="Speak",width=5,height=3,command=speak).pack(padx=10,side="left")



#Creating buttons 
frame=tk.Frame(window, bg="#C2C2C2")
frame.pack(pady=10)
tk.Button(frame,text="Save info",command=adding_new_students).pack(padx=5,side="left")
tk.Button(frame,text="Delete",command=delate_all).pack(padx=5,side="left")
tk.Button(frame,text="Count of students",command=lambda:verifyting.config(text=f"There are {len(Students)} here...")).pack(padx=5,side="left")
tk.Button(frame,text="Display students",command=display_student).pack(padx=5,side="left")



#just a label that will tell us the info needed 
verifyting=tk.Label(window,text="Dear user please enter all the info neded...",width=40, bg="#C2C2C2")
verifyting.pack(pady=10)


if __name__=="__main__":
    window.mainloop()