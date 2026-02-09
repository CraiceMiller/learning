from fractions import Fraction
import functools 


def is_a_real_progression(numbers)->bool:
    #a*r**n-1
    a=int(numbers[0])
    r=int(numbers[1]/numbers[0])
    #a_=numbers[0]*(numbers[1]/numbers[0])**(3-1)

    is_progression=[a*r**(n-1) for n in range(1,5)]
    if numbers == is_progression:
        return True
    else:
        return False


def geometric_progression(numbers:list[int])->None:
    print("-----------------------------------------")
    a=int(numbers[0])
    r=int(numbers[1]/numbers[0])

    is_progression=[a*r**(n-1) for n in range(1,5)]
    print(f"the real proggres: {is_progression} "  )
    print(f"the numbers given: {numbers} \n" )


    print("it is a geometric progression")
    print(f"The reason is: '{r}' \n")
    print("-----------------------------------------")
     
   


def reals_geometrics(f1,f2,f3,f4):
    a=is_a_real_progression(f1)
    b=is_a_real_progression(f2)
    c=is_a_real_progression(f3)
    d=is_a_real_progression(f4)
    indeed=[a,b,c,d]
    nums=[f1,f2,f3,f4]
    see_list=0

    for i in indeed:
        if i:
            geometric_progression(nums[see_list])
        else:
            print("it is not a geometric progression!!\n")

        see_list+=1
        
        
            
    
list_numers=[2,-100,200,-300]
list_numers_2=[3,12,60,360]
list_numers_3=[5,25,625,390,625]
list_numers_4=[2,-16,128,-1024]

reals_geometrics(list_numers,
list_numers_2,
list_numers_3,
list_numers_4)
