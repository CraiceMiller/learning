
import time 
#import pygame
import datetime 
from time import sleep


     
class MyWatch:
    """
    DESCRIPTION: 
        This class will do basic thing of a watch 
    
    """

   
    @staticmethod
    def int_to_time(num:int|float)->tuple[int,int,int]:
        """Description: I creted this method to help the create_time method, cuz i don't 
        want to write hour, minutes, seconds individually everytime"""
        seconds:int=int(num%60)
        minutes:int=int((num//60)%60)
        hours:int=int(num//3600)
        return hours, minutes, seconds

 


    @staticmethod 
    def myclock():
        """Description: this only gives when do you started and  the current time"""
        start_time=datetime.now().strftime("%H:%M:%S")
        print("\nI started at: {}".format(start_time))
        try: 
            while True: 
                now=datetime.now().strftime("%H:%M:%S")
                print("\rCurrent Time: {}".format(now), end="")
                sleep(1)

        except KeyboardInterrupt as e:

            print("\nYou have stop the clock")


    def get_local_hour(self)->str: 
        """just get the local hour"""
        return datetime.datetime.now().strftime("%H:%M:%S")

    def create_date(self,day:int,month:int, year:int)->datetime.date:
        """create date in, day, month, year"""
        try: 
            return datetime.date(int("20"+f"{year}" ),month,day)
        except ValueError: 
            return datetime.date(1,1,1)
    
    def today(self): 
        return datetime.date.today()
    
    def create_time(self,hour:int,minutes:int, seconds:int)->datetime.time:
        """create time in, hour, minutes, seconds"""
        try:  
            return datetime.time(hour,minutes,seconds)
        except ValueError: 
            return datetime.time(0,0,0)

    def create_appointment(self,day:int,month:int,year:int,hour:int,minutes:int,seconds:int)->datetime.datetime: 
        """Create date and time"""
        return datetime.datetime(int("20"+f"{year}" ),month,day,hour,minutes,seconds)


class Alarm(MyWatch): 
    sound_file:str="my_music.mp3"

    def set_alarm(self): 
        pass

def static(list_:list): 
    result=[]

    for value in list_:
        age,freq=value
        result.append(freq)

    total_freq=sum(result)
    freq_rel=[round(x / total_freq,3 )for x in result]

    fp=[round(y * 100,2) for y in freq_rel]

    result2:list=[]
    for e,fr,fp_ in zip(list_,freq_rel,fp):
        result2.append((*e,fr,fp_))

    return result2





if __name__=="__main__": 
    clock=MyWatch()
    current:tuple=clock.int_to_time(60)
    print(clock.create_time(*current))


    #values=[(20,32),(21,80),(22,98),(23,142),(25,86),(28,58)]




    pass

