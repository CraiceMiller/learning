#exercise No1
print('-'*20+'Args'+'-'*20)
def my_sum(*args:int)->float|int:
    return sum(args)

a = my_sum(1,2,3)
print(a)        #output: 6
print(my_sum()) #output: 0
print(my_sum(2.5,2.5)) #output: 5

#exercise No2
print('-'*20+'Kwargs'+'-'*20)
def user_detail(**kwargs:dict)->None:
    if not kwargs:
        print('There is no info here...')
        return 
    print('-'*10+'Info Details'+'-'*10)
    for index,(key,value) in enumerate(kwargs.items(),start=1):
        print(index, f". {key}: {value}")

name,age,likes='Ashley',17,('spend time with friends','make up')
user_detail(
    name=name,
    age=age,
    likes=likes
)

user_detail()
user_detail(product='Laptop',stock=20)

#Exercise No.3
print('-'*20+'*'+'-'*20)

favorite_animes='Nazo no Kanojo X','Stain Gate','Nichijou','Dangaronpa','No game No life','Re:Zero'
a,*b,c=favorite_animes
print(f'The BEST ! animes for me is {a}')
print('the rest is: ')
for i in b:
    print(f"-{i}")
print(F"The last one is {c}")

nums=[700,200,300,200,400,800,500,200,900,300,500,600,100,400,200,100,500,200,100,200,800]
nums.sort()

x,*y,z=nums
print(f"the first numbers is {x}")
print(f"the rest is { set(y)}")
print(f"the last number is {z}")



    
        



