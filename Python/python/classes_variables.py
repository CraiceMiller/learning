from classes_to_use import Student

def main():
    #the variables at hand...
    st1 = Student("Hersy",18,3,True)
    st2 = Student("Ashley",17,3,True)
    st3 = Student("Craice",19,3,True)
    st4 = Student("Sthepahy",18,3,True)
    st5 = Student("geroge",19,3,True)
    #this will show how many students are...
    Student.show_num_students()

    #this are filters i wanna try
    all_students = [st1,st2,st3,st4]
    #this will add only adult students 
    adult_students = [students for students in all_students if students.is_adult]
    #this reportedly will print their status
    for status in adult_students:
        status.show_status()

if __name__ =='__main__':
    main()