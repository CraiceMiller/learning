import datetime 
from time import sleep



#19/08/2025
class MyWatch:
    """
    DESCRIPTION: 
        This class will do basic thing of a watch 
    
    """
    @staticmethod
    def countdown(num:int)->None:
        """Description: This is the basic countdown like always"""
        print("_"*30)
        for count in range(num,-1,-1):
            seconds:float|int=count%60
            minutes:int|float=(count//60)%60
            hours:int|float=count//3600

            now=f"{hours:02}: {minutes:02}: {seconds:02}"
            print("\rCountdown: {}".format(now),end="")
            sleep(1)
            
        print("\nTime is up")

   
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

    @staticmethod 
    def get_local_hour()->str: 
        """just get the local hour"""
        return datetime.datetime.now().strftime("%H:%M:%S")
    
    @staticmethod
    def get_local_time()->str:
        return datetime.datetime.now().strftime("%d/%m/%Y")

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

   
  