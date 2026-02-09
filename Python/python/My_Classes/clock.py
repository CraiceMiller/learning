import tkinter as tk 
from time import strftime

#CREATING THE CLOCK CLASS
class DigitalClock:
    """
    NOTES:
        Here i will code everything new I'll learn in the future. 

    DESCRIPTION: 
        This is basically a simple watch, here you can wacth the currently time 

    UPDATE: 
        01/08/2025
    """

    def __init__(self,
                 master,
                 font_:tuple[str,int]=("Helvetica",40),
                 background:str="black",
                 foreground:str="cyan",
                 name:str="clock 1"
                 ) -> None:
        self._name=name

        #creaing the frame
        frame=tk.Frame(master,bg=background)
        frame.pack(anchor="center", fill="both")


        #creating the labels
        self._clock_label=tk.Label(frame,
                                   font=font_,
                                   bg=background,
                                   fg=foreground,
                                
                                   )
        self._description_label=tk.Label(frame,font=font_, bg=background,fg="#55FF00",text="Currently Hour: ")

        #packing the labels
        self._description_label.pack(anchor="center", fill="both",side="left")
        self._clock_label.pack(anchor="center", fill="both",side="right",)

        #creating the instance that will storage the after method
        self._update_id:str|None=None

    #creaing dunder methods
    def __str__(self) -> str:
        return f"Name: {self._name}"
    
    def __eq__(self, __value) -> bool:
        return self._name == __value._name

    #creating methods
    def get_time_str(self,)->str:
        return strftime("%H:%M:%S")
    
    def display_time(self,):

        currently_time:str=self.get_time_str()
        self._clock_label.config(text=currently_time)

        self._update_id=self._clock_label.after(1000,self.display_time)

    def start(self)->None:
        self.display_time()

    def stop(self)->None:
        if self._update_id:
            self._clock_label.after_cancel(self._update_id)
            self._update_id=None



class CountDown(DigitalClock):
    def __init__(self, master, variable:tk.StringVar,font_: tuple[str, int]=("Helvetica",40), background: str = "black", foreground: str = "cyan",  name: str = "countdown") -> None:
        super().__init__(master, font_, background, foreground, name)
        self._variable=variable
        self._remaining_seconds:int=0

        self._is_running:bool=False
        self._description_label.config(text="Countdown: ")
        self._clock_label.config(text="00:00:00")
        
   

    def _get_numbers(self, time:int )->str:
        if time <=0:
            return "00:00:00"
  
        seconds= time % 60
        minutes= (time // 60) % 60
        hours= time // 3600
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}"
    
    def _display_time(self):
        #ensure that the clock is indeed runing 
        if not self._is_running:
            return 
        
        #ensure that the clock is more than 0
        if self._remaining_seconds <= 0:
            self._clock_label.config(text="Times is up!! ")
            self.stop() 
            return
        
        #here is wher we are going to subtract every seconds 
        self._remaining_seconds -= 1
        self._clock_label.config(text=self._get_numbers(self._remaining_seconds))

        # i think this will be my for loop...
        self._update_id=self._clock_label.after(1000,self._display_time)
        


    def start(self)->None:
        #we are going to ensure that clock is already running 
        if self._is_running:
            return 
        
        variable_str:str=self._variable.get()

        try:
            variable_int:int=int(variable_str)

            self._remaining_seconds=variable_int
            self._is_running=True
            self._variable.set("0")

            self._clock_label.config(text=self._get_numbers(variable_int))
            self._update_id=self._clock_label.after(1000,self._display_time)


        except ValueError:
            self._clock_label.config(text="Select a number")
            self.stop()
    


 

    def stop(self) -> None:
        super().stop()
        self._is_running=False
        self._variable.set("0")
    
        



def main()->None:
    #creating the window 
    window=tk.Tk()
    window.title("Digital clock")
    window.geometry("900x200")

    #Creating variables 
    count=tk.StringVar(value="60")
    count_2=tk.StringVar(value="60")


    #CREATING THE CLOCK OBJECT
    clock:DigitalClock=DigitalClock(window,("Helvetica",40),"black","cyan")
    countdown:CountDown=CountDown(window, count, ("Helvetica",40),"black","cyan")
    countdown_2:CountDown=CountDown(window,count_2)

    
   
    #creating the button 
    frame=tk.Frame(window)
    frame.pack()
    tk.Button(frame,command=clock.start,width=10,text="Start clock").pack(padx=10,side="left")
    tk.Button(frame,command=clock.stop,width=10,text="Stop clock").pack(padx=10,side="left")




  
   #first countdonw 
    frame=tk.Frame(window)
    frame.pack(pady=5)
    tk.Entry(frame,textvariable=count,width=20).pack(padx=10, side="left")
    tk.Button(frame,command=countdown.start,width=10,text="start countdown").pack(padx=10, side="left")
    tk.Button(frame,command=countdown.stop,width=10,text="stop countdown").pack(padx=10, side="left")

    
   #second countdonw 
    frame=tk.Frame(window)
    frame.pack(pady=5)
    tk.Entry(frame,textvariable=count_2,width=20).pack(padx=10, side="left")
    tk.Button(frame,command=countdown_2.start,width=10,text="start countdown").pack(padx=10, side="left")
    tk.Button(frame,command=countdown_2.stop,width=10,text="stop countdown").pack(padx=10, side="left")






    clock.start()
    window.mainloop()
    



if __name__ == "__main__":
    main()