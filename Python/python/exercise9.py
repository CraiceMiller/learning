
def manage_event_data(*args:tuple,**kwargs:dict)->None:
    if not args and not kwargs:
        print('This function is empty')
        return 
    

    from datetime import datetime
    from colorama import Fore, Style

    print("-"*40 + "EVENT" + '-'*40)
    #this just print the names of the attenders
    if not args:
        print('\nThere is no attenders')
    else:
        names = filter(lambda x: x.strip() != "", args)
        attenders = list(map(lambda attender: attender.capitalize(),names))
        print(f"Attenders : {" ".join(list(attenders))}")
       
      
    
    #this just print a list of the details of the event
    if not kwargs:
        print('NO details')
    else:
        if kwargs.get('event_name'):
            print(f"\nEvent Name: {kwargs.get('event_name')}")
        else:
            print('\nEven Name: Unkwon')

        print('\nEvent Details')
        for index,(key,value) in enumerate(kwargs.items(),start=1):
            if  key not in ('event_name','date', 'urgency'):
                print(index, f".{key:.<20}{value}")
            
    
    combined_list=zip(list(attenders),kwargs.values())
    print(f"\n{'ATTENDERS':<15}{'EVENT'}")
    for index,(person,info) in enumerate(combined_list,1):
        print(index, f"{person:<10}", index,f"{info}")
    
    #this will give us the current time and the event time
    print(f"\nToday is:  {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    if kwargs.get('date'):
        print(f"The date of the event: {kwargs.get('date')}")
    else:
        print('This event has no date')
    
    print(f"Numbers of attenders in total: {len(list(attenders))}")
    if kwargs.get('urgency'):
        print(Fore.RED + 'THIS EVENT IS URGENCY'+ Style.RESET_ALL )
        print('-'*80)
    


   



manage_event_data('hersy',"", 'criace','ashley', "",
                  event_name='Video Game Party',
                  date='12/7/2025',
                  hour='14:00 hrs',
                  location='Mall Center',
                  urgency=True)

manage_event_data()