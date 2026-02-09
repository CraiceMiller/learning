#this modules are mine
from my_original_character import hersy,craice,ashley
from classes_to_use import *
from My_Classes import person as p

#this ones are from pyton 
from copy import deepcopy
import inspect

#here is whre i will type all my progress...
#def show_progress_so_far():
    #start 5/7/25, everything new i learn i will use it here...
# update 12/07/2025
# update 18/07/2025
# update 01/08/2025

    #pass

#def things_i_already_use_here():
    #enumarte(), for, def, list, str, int, ditc, class, from, main(),typeanotations,
#filter, map, isinstance,

    #pass

#here is where goes the details of every character
characters:list[dict]=[hersy,craice,ashley]
copy_of_characters:list[dict]=deepcopy(characters)

#creating the class person for each of my oc
HERSY:p.Person=p.Person(name='Hersy', lastname='halston',age=19,
                        language=["spanish","english"],gender="male",profession='Student',
                        birthaday='April 12th', height= 70.50, weight= 135.50,
                        country='Altisora',temperament='sanguine-choleric',
                        likes=['play videogames', 'exercising', 'hang out with friends',
                            'animes', 'living', 'watch animes, series, doramas, movies, novels',
                              'female fashion', 'ethical classes', 'make up'],
                        dislikes=['spicy & salty food', 'feling lonely', 'bad habbits'],
                        weaknesses=['overcompensation', 'difficulty handing loneliness', 'problem avoidance'],
                        strenghts=['intiative', 'fun-loving', 'bold', 'not too fluent in a foreign language', 'leadership'],
                        beliefs=['god', 'health', 'her family & friends', 'education', 'himself'],
                        fears=['clowns'])

CRAICE:p.Person=p.Person(name='Craice', lastname='miler',age=19,
                        language=["spanish","english"],gender="female",profession='Student',
                        birthaday='May 15th', height= 67.50, weight= 130.60,
                        country='Altisora',temperament='phlegmatic',
                        likes=['cats', 'spiders', 'motocycles', 'loliness', 'wathc movies',
                            'plushies', 'music(rock)', 'listen to others', 'cooking', 'exercising',
                            'play videogames', 'read mangas', 'ethical classes', 'relax'],
                        dislikes=['math', 'hipocrites', 'spicy food', 'complex techonology', 'noisy environments',
                                'disorganization', 'imposed obligations', 'falsehood'],
                        weaknesses=['realism', 'overthinking things', 'concentrate'],
                        strenghts=['calm', 'modest', 'realible', 'fluent in a foreign language'],
                        beliefs=['god', 'truth', 'her family & friends'],
                        fears=['heights'])

#Here is where i'll taste everything i can ....
def presenting_my_ocs()->None:
    for index, i in enumerate(characters,start=1):
        print(index,i["name"].capitalize(),i["age"])

#Banking ....
def banking_acounts_my_ocs(indexing:int)->Bank:
    bank_acounts:list[dict]=[x['bank'] for x in characters]
    index:int=indexing-1
    try:
        return Bank(balance=bank_acounts[index]['balance'],
                wallet=bank_acounts[index]['wallet'],
                name=bank_acounts[index]['username'],
                debt= bank_acounts[index]['debt'])
    
    except IndexError as e:
        print(f"An error has ocurred: {e}")
        print(f"that person doesn't exist")
        return Bank()


#studing ...
def studing_my_ocs(indexing:int)->None:
    index = indexing-1
    try: 
        user=Student(name=characters[index]['name'],
                    age=characters[index]['age'],
                    is_student=characters[index]['is student'],
                    school_year=characters[index]['school year'])
        user.introduce()
        user.speak()
    except IndexError as e:
        print(f"An error has ocurred: {e}")
        print(f"that person doesn't exist")

def basic_information_ocs(indexing:int,*add_more_info)->PersonalAssistance:
    new_information:dict={}
    index:int= indexing-1
    try: 
    
        get_keys:list=list(filter(lambda x:characters[index].get(x) is not None,add_more_info ))
        for x in get_keys:
            new_information[x]=characters[index][x]

        if  new_information:
            return PersonalAssistance(new_information,                                   
            name=characters[index].get('name'),
            age=characters[index].get('age'),
            is_student=characters[index].get('is student'),
            height=characters[index].get('height'),
            weight=characters[index].get('weight'),
            gender=characters[index].get('gender'),

        )

        else:
            return PersonalAssistance(                                    
                name=characters[index].get('name'),
                age=characters[index].get('age'),
                is_student=characters[index].get('is student'),
                height=characters[index].get('height'),
                weight=characters[index].get('weight'),
                gender=characters[index].get('gender'),

            )
       
    except IndexError as e:
        print(f"An error has ocurred: {e}")
        print(f"that person doesn't exist")
        return PersonalAssistance()



def main()->None:
    """
    1.Hersy
    2.Craice
    3. Ashley
    """
    #for index in range(0,len(characters)):
     #   banking_acounts_my_ocs(index)
    
    #a= list(map(studing_my_ocs,(1,2,3)))

    _hersy:PersonalAssistance=basic_information_ocs(1) 
    _craice:PersonalAssistance=basic_information_ocs(2) 
    _ashley:PersonalAssistance=basic_information_ocs(3,"siblings","humor","deslikes")

    HERSY.speak()
    HERSY.introduce()
    CRAICE.introduce()
    HERSY.greet(CRAICE)
    HERSY.walk()

    print(HERSY._name)
    HERSY._name="armando paredes"
    print(HERSY._name)

    print(inspect.getmembers(p.Person,inspect.isfunction))
   
   
     
   
    

   


   


    pass
      



if __name__ == '__main__':
    main()