name_1 = 'hersy'
name_2 =  'craice'
name_3 = 'miseru'

# list
students = [name_1, name_2, name_3]

# dictionaries
personal_data_1 = {
    'name': name_1,
    'age': 18,
    'courses': ('math', 'sports', 'psychologict'),
    'hobbies': {'play videogames', 'hang out with friends', 'animes'}
}

personal_data_2 = {
    'name': name_2,
    'age': 19,
    'courses': ('math', 'computer scinces', 'management'),
    'hobbies': {'watch movies', 'read mangas', 'ride her bike', 'play videogames'}
}

personal_data_3 = {
    'name': name_3,
    'age': 18,
    'courses': ('art', 'accounting', 'programing'),
    'hobbies': {'play videogames', 'learning new stuff', 'animes'}
}

# list
student_records = [personal_data_1, personal_data_2, personal_data_3]

# full records
print('------- student full records-------')
for student in student_records:
    print(f"\n record:")
    for key, value in student.items():
        print(f"{key}: {value}")

# student's names
print(f'\n ------- student names-------')
for student in student_records:
    i = student['name'].capitalize()
    print(f"student: {i:^15}")


# add new value
new_hobby = 'coding'
print(f'\n ------- new hobbie -------')
for student in student_records:
    student['hobbies'].add(new_hobby)
    print(f"\n {student['name'].capitalize()} has updated. hobby: {student['hobbies']}")
    

# chek math
print(f'\n ------- math course -------')
for student in student_records:
    if 'math' in student['courses']:
        print(f" indeed {student['name'].capitalize()} has math")
    else:
        print(f" no, {student['name'].capitalize()} doesn't have math")

#student remove
i = student_records.pop(2)
print(f"\n the student {i['name'].capitalize()}, is not a students anymore ")

print('\n ------these students remain:------- ')
for student in student_records:
    print(f"\n Student: {student['name'].capitalize():^10}")
    for key, value in student.items():
        print(f"{key}: {value}")


print('\n ------ attempts:------- ')
# when i was doing this, i have been noticing some of stuff. 
#if i want to see just the name of the second studend i could do this:
print(student_records[1]['name'].capitalize())
#and if i want to union all hobbies i could do this:
student_records = [personal_data_1, personal_data_2, personal_data_3]
h = student_records[0]['hobbies']
o = student_records[1]['hobbies']
b = student_records[2]['hobbies']
union = h.union(o, b)
print(union)
#if i just want to add one single new value i can do this:
student_records[0]['dislike'] = {'loliness', 'complex things'}

for student in student_records:
    for key, value in student.items():
        if student == personal_data_1:
            print(f"{key}: {value}")
        else:
            break
            
#if i want to delate everuthing i can do this
student_records.clear()

if student_records == []:
    print('\n there are not any students left')
else:
    print('\n -----STUDENTS------')
    for student in student_records:
        print(f"\n {student['name'].capitalize()}")
        for key, value in student.items():
            print(f"{key}: {value}")