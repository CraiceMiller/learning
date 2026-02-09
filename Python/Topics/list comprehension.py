import random

#normal 
doubles:list[int] = []

for x in range(1,10+1):
    doubles.append(random.randint(1,30))

doubles.sort()
print(doubles)

#list comprehension 

# intergers

doubles=[z * 2 for z in range(random.randint(1,16))]
triples = [ y  * 3 for y in range(random.randint(1,11))]
squares=[a * a for a in range(random.randint(1,11))]
print(doubles)
print(triples)
print(squares)

#strings

animes:list[str] = ["Nazo no kanojo X", "Jojo's", "Nichijou", "Azumanga", "domestic no kanojo"]
animes:list[str] = [anime.upper() for anime in animes]
animes.sort()
print(animes)

# 
numbers = [1, -2, 3, -4, 5, -6, -7, 8, 9, 10, -11,12,13,14]
possitives_num=[num for num in numbers if num >= 0]
negative_num=[num for num in numbers if num <= 0]
even = [num for num in numbers if num % 2 == 0 and num >= 0]
odd = [num for num in numbers if num % 2 == 1]
print(possitives_num)
print(negative_num)
print(even)
print(odd)

#
grades = [35, 44, 75, 88, 56, 61, 13, 90, 100]
passing_grades = [passing for passing in grades if passing >= 60]
print(passing_grades)

# my turn 

#create a dict of courses
# create dicts of each courses
# write the grades of each students in each courses
# print the name and the grade of just the passing students in math 
# create a if or def statement  to ask the person which grade of a course wants to see
# and convert the grades into the A, B, C category
passing_note = 75

coursses:dict = {
    "language": {
        "hersy": 90,
        "Cracie": 99,
        "Ashley": 88,
        "Drawned": 85,
        "Stephania": 79, 
        "Julia": 78

    }, 

    "math": {
        "hersy": 80,
        "Cracie": 90,
        "Ashley": 74,
        "Drawned": 76,
        "Stephania": 91, 
        "Julia": 60

    }, 

    "art": {
        "hersy": 77,
        "Cracie": 89,
        "Ashley": 78,
        "Drawned": 75,
        "Stephania": 85, 
        "Julia": 100

    }, 

    "accounting": {
        "hersy": 47,
        "Cracie": 82,
        "Ashley": 78,
        "Drawned": 75,
        "Stephania": 85, 
        "Julia": 88

    }


}

print("\n")
def letter(score):
    if score >= 90:
        return "A" 
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"



print("\n")
def passing_students(course):
    beca=[]
    print(f"passing students in: {course} ")

    if course == "math":
        for key, value in coursses["math"].items():
            if value >= passing_note:
                change = letter(value)
                print(f"{key:.<20} {value} = {change}")
                if change == "A":
                    beca.append(key)

                

    elif course == "language":
        for key, value in coursses["language"].items():
            if value >= passing_note:
                
                change = letter(value)
                print(f"{key:.<20} {value} = {change}")
                if change == "A":
                    beca.append(key)

    elif course == "art":
        for key, value in coursses["art"].items():
            if value >= passing_note:
                change = letter(value)
                print(f"{key:.<20} {value} = {change}")
                if change == "A":
                    beca.append(key)
    
    elif course == "accounting":
        for key, value in coursses["accounting"].items():
            if value >= passing_note:
                change = letter(value)
                print(f"{key:.<20} {value} = {change}")
                if change == "A":
                    beca.append(key)



    print()
    
       
    if beca == []:
        print("in this course there are no students with becas")
    elif len(beca) == 1:
        print(f"Congratulation!!, Just {beca[0]} is the only student with beca  ")
    else:
        print(f"These are the students with becas: ")
        for i in beca:
            print(i, end=",")

    print()

    

    

print("What course do you want to see?: ")
print(coursses.keys())
chose =input().lstrip().lower()

while chose not in coursses.keys():
    print('please write a valide input')
    print()
    print("What course do you want to see?: ")
    print(coursses.keys())
    chose =input().lstrip().lower()

passing_students(chose)

print()
print("do you want to see all the courses?")
answer = input().lstrip().lower()
if answer == "yes":
    for key, value in coursses.items():
        print(f"this is the course of: {key}")
        print()
        print(F"{"STUDENT":<20}{"GRADE"}")
        for a,b in value.items():
            print(f"{a:.<20}{b}")
        print()
else:
    print("ok")


# second try using the metho i learned today 'list comprehension'
print()
attempt = {key: value for key, value in coursses.get(chose).items() if value >= passing_note }
print(f"passing studntes in: math ")
for a, b in attempt.items():
    print(f"{a:.<20} {b}")