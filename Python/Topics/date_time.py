import datetime 
from time import sleep


     
class MyWatch:

   
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
        return datetime.datetime.now().strftime("%H:%M:%S")

    def create_date(self,day:int,month:int, year:int)->datetime.date:
        try: 
            return datetime.date(int("20"+f"{year}" ),month,day)
        except ValueError: 
            return datetime.date(1,1,1)
    
    def today(self): 
        return datetime.date.today()
    
    def create_time(self,hour:int,minutes:int, seconds:int)->datetime.time:
        try:  
            return datetime.time(hour,minutes,seconds)
        except ValueError: 
            return datetime.time(0,0,0)

    def create_appointment(self,day:int,month:int,year:int,hour:int,minutes:int,seconds:int)->datetime.datetime: 
        return datetime.datetime(int("20"+f"{year}" ),month,day,hour,minutes,seconds)


if __name__ == "__main__": 
    clock=MyWatch()
    print(clock.get_local_hour())
    print(clock.create_date(18,8,25))
    print(clock.today())
    print(clock.create_time(10,25,5))
    print(clock.create_appointment(18,8,25,10,25,5))




    pass