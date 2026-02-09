# indexing = accesing elmetns of a seqence using [] (indexing operator)
#            [start: end: step]

# string indexing, we can access elements of a sequends using the indexing operator, 
# you can use starting position, endind position and even step if yo want to skip over characters

credit_number = "132-456-789-147"
print(credit_number [4])
print(credit_number [ 2 : 4 ])
print(credit_number [ : 4 ])
print(credit_number [ 2 :  ])
print(credit_number [-5])
print(credit_number [::2])

last_digital = credit_number[-4:]
print(f"xxx-xxx{last_digital}")

print("let's work with another one. shall ?")

list = "orange, apple, pear, grapes"
print(list[0:6])
print(list[8:])
