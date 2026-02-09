from mypython.alg import LinkedList,PriorityQueue,QueueInterface #type: ignore
from typing import TypeVar, Callable, Any, TypeAlias





This = TypeVar("This")
def Key(map:This,key:None | Callable[[This],Any])->This:
    items:list=[]
    for value in map:
        if key is not None: 
            element = key()
            items.append(element)
            
    if items:
        items.sort()
        new_list = [x for x in map if x in items]
        
            
    
    return map 
    
    


if __name__ == "__main__": 
    que:QueueInterface[str] = LinkedList(("hersy","craice","miseru"))
    notes:QueueInterface[float] = PriorityQueue()

        
        
    INFO:list[dict] = [
        {
        "name":"Stephany",
        "age":19
    },{
        "name":"mariam",
        "age":21
    },{
        "name":"Jhon",
        "age":17
    }
        
        
    ]
    
    n:list[dict]=sorted(INFO,key=lambda x:x["name"])
    print(n)
    z:list[dict]=Key(INFO,key=lambda x:x["name"])
        
        

    
class Node:
    def __init__(self,data,previous,_next) -> None:
        self.data  = data 
        self.prev = previous
        self.next = _next 
        
class Link:
    def __init__(self) -> None:
        self.size = 0 
        self.head = None 
        self.tail = None 
        
    def empty(self): 
        return self.head == None
        
    def offer(self,e): 
        Last = self.tail
        new_data = Node(e,Last,None)
        self.tail = new_data
        if self.head is None: 
            self.head = new_data
        else: 
            Last.prev = new_data
        self.size =+ 1 
        return e 
    
    def poll(self): 
        First = self.head 
        self.head = First.next 
        if self.head is None: 
            self.tail = None
        else:
            self.head.prev = None 
        return First.data


    