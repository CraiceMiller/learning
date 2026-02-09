# len(), x.find(), 

name = input("enter your full name: ")


#result= len(name) #will give us the length of the string, how many characters is in
result =  name.find(" ") #will return the first occurence of a whaterver character you want to put in ("l") otherwise will print -1
#result = name.rfind("e") #will return the last occurence of a whatever characteer you want to put in
#result =  name.capitalize() #this only make the first letter a capital letter
#result = name.upper() #this only converts  all worlds to capital letters 
#result = name.lower() #this only converts  all worlds to lowercase letters 
#result = name.isdigit()  #this is true if only there numbers
#result = name.isalpha() #this is true if only there are characters
#result = name.count("e") #we can count how many characters are within a sting
#result = name.replace(" ", "_")
print(result)



