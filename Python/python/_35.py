def binary_(ls:list,target)->int:
    start:int=0
    end:int=len(ls) -1

    while start <= end:
        mid:int= (start + end ) //2

        if ls[mid] == target: return mid

        if ls[mid] < target: start=mid + 1

        else: end=mid -1

    return -1


my_list=list(range(10))
print(binary_(my_list,2))


