
def get_name(name:str):
        
    def countdown(number:int) -> None:
        import time
        from colorama import Style, Fore
        for x in range(number,0,-1):
            seconds: int = x % 60
            minutes: int = int(x / 60) % 60
            hours: int = int((x / 3600))
            print(f"{hours:02}:{minutes:02}:{seconds:02}")
            time.sleep(1)
    

        print(Fore.RED +  f"{name} your is UP!!!" + Style.RESET_ALL)



    return countdown

   


def main()->None:
    
    name:str='Hersy Helton'
    money:float|int=25.5
    bag:dict={'books':3,'bottle of water':10,'Snacks':{'candies':7,'chocolate':5}}
    debt:int|float=0
    my_dict:dict={}

    #chosse=input("How many minutes: ")
    #minutes=60 * int(chosse)

    user_name=get_name(name)
    user_name(3)
    
  

main()

