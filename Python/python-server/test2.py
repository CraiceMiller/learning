#a heap is an algorithom. its main purpose is to get la lowest or largest value in an _array... 
import heapq
from mypython.alg import LinkedList, Stack #type: ignore
from mypython.utils import quickSort,binarySearch,doTask #type: ignore

#formula 
#       index
#     2*index +1 
#     2* index + 2 

"""
  
            1
        2       3
    4  7      9   9
    
        

"""

def he()->None: 
    _array:list = [4,7,9,10,1,3,9,1,29,100,2,10,45,12,]
    print("normal list: ", _array)
    heapq.heapify(_array)
    heapq.heappush(_array,-2)
    heapq.heappop(_array)
    a = heapq.heappushpop(_array,10)
    m = heapq.merge(['dog', 'horse'], ['cat', 'fish', 'kangaroo'],key=len)
    r = heapq.heapreplace(_array,0)




    print("heap list: ", _array)
    print("Replace heap list: ",r)
    print("The smallest: ", heapq.nsmallest(1,_array))
    print("The Largest: ", heapq.nlargest(1,_array))
    print(a)
    #print(next(m))

    print(heapq.__name__)


def test1()->None: 

    stack: Stack[str] = Stack()
    num:Stack[int] = Stack()
    print()
    print(stack.empty())
    #stack.peek()

    stack.push("Minecraft")
    stack.push("Doom")
    stack.push("Hollow Knight")
    stack.push("Fire emblem")
    stack.push("Fire emblem")
    stack.push("Fire emblem")
    stack.push("Cup-Head")
    stack.push("Pokemon Black editon")

    print(stack.empty())
    stack.pop()
    stack.pop()
    stack.pop()
    
    print(stack.stack)
    print(stack.peek())
    stack.pop()
    stack.pop()
    for _ in range(10): 
        stack.push("Banjo and Kazooi")
    
    print(stack.stack)
    


    #print(stack.stack)
    print(stack.peek())
    print(stack.search("Hollow Knight"))
    
    




#print(heapq.__about__)




if __name__ =="__main__": 
    my_list:LinkedList[str]= LinkedList() 
    my_list.offer("Hersy")
    my_list.add("Craice")
    my_list.offer("Sthephany")
    my_list.offer("Ashley")
    my_list.offer("Miseru")
    
    my_list.poll()
    my_list.remove()
    
    
    print(my_list.peek()) 
    print(my_list.size())
    print(my_list.element())
    
    nums:LinkedList[int] = LinkedList((1,3,5))
    #nums.offer("hello") #this will give me an error due it a str instead of int 
    nums.add(10)
    nums.remove()
    
    print(nums.peek())
    print("----->")
    test1()
    
    print("--------------------------z")
    a:list[str] = quickSort([0,2,3,1,2,6,4,9,10])
    b:list[str] = quickSort(["Miseru","Hersy","Craise","Ashely"])
    c:int= binarySearch(iterable=a,target=2.5)
    print(a,b,b[1].capitalize(),c)
    print("--------------------------z")
    z:LinkedList[dict] = LinkedList()
    z.offer({"a":1,"b":2})
    z.offer({"c":10,"d":20})
    z.offer({"e":100,"f":200})
    print(z.peek())
    z.remove()
    print(z.peek())
    print(z.peek().get("c"))
    
    

        

  
  
  


