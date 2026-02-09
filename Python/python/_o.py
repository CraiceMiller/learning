def display_user_info(*args,**kwargs:dict)->None:
    print('-'*20+'PERSONAL INFORMATION'+'-'*20)
    info_needed:tuple[bool]=(bool(kwargs.get('name')),bool(kwargs.get('age')),bool(kwargs.get('country')))
    
    if kwargs != {}:

        name,age,country = kwargs.values()
        

        if all(info_needed):
            print(f'Name: {name.capitalize():<10}')
            print(f"Age: {age}")
            print(f"Country: {country}")

        
        elif kwargs.get('name'):
            if kwargs.get('age'):
                print(f'Name: {name.capitalize():<10}')
                print(f"Age: {age}")
                
            elif kwargs.get('country'):
                print(f'Name: {name.capitalize():<10}')
                print(f"Country: {country}")
                
            
        elif kwargs.get('age') and kwargs.get('country'):
            print('This person doesnt give their name yet...')
            print(f"Age: {age}")
            print(f"Country: {country}")
            

        else:
                index=info_needed.index(True)
                info = name,age,country
                value = info[index]
                print(f'{value}')
    else:
        print('This person has no personal info ')         
  

    if args == (None,):
        print('There is no extra info here...')
    else:
        print('-'*20+ 'Extra info' + '-'*20)
        for informartion in args:
            for key,value in informartion.items():
                print(f'{key}: {value} ')
            break


isinstance()
       
            

  
               
   
    

a = {'personal': {'country':'altisora','age':18,'name':'hersy'},'extra': {'languges':('spanish,english'),'high':68.5}}
b={'personal': {'age':17,'name':'Ashley'}}
c={'extra': {'languges':('Japoness,english'),'music':('pop','rock'),'year':2025}}
d={'personal': {'country':'Germany','age':25}}
e = {'personal': {'country':'altisora','age':19,'name':'Craice'},'extra': {'languges':('spanish,english,Italian'),'high':68.5,'weight':132.75,'likes':['plushies','movies','study'],'hate':'Phony people','school':{'year':2025,'Average Notes':91,'Has Friends':True}}}
f = {'personal':{'country':'altisora'}}
g = {}

#  

all_people = a,b,c,d,e,f,g

for person in all_people:
    print('\n')
    if person.get('personal')==None:
        display_user_info(person.get('extra'))
        continue

    display_user_info(person.get('extra'),
                    name=person.get('personal').get('name'),
                    age=person.get('personal').get('age'),
                    country=person.get('personal').get('country'),
                    )
   