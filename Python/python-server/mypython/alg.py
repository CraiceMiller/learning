#------------------------------->
#Stack data structure 
from typing import (Any,Callable, Iterator,Optional,Iterable,Generic,TypeVar)
from .Typing.interfaces import (QueueInterface) #type:ignore
from collections import deque
import heapq 
from .utils import quickSort #type: ignore

Item = TypeVar('Item')
"""This type is the to use generic Type <Item> like in TypeScript"""


#this ocan only be added for the end, end removing for the end 
class Stack(Generic[Item]): 
    """
    LIFO  data structure. Last-in First-out, store objects into a sort of "vertical Tower"
    push() too add to the top
    pop() to remove from the top 
    """


    def __init__(self) -> None:
        self._array:deque[Item] = deque()
        
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self._array}) "

    
    def push(self,item:Item)->Item: 
        """
        Parameters: 
            :item: the item to be pushed onto the stack
        
        Return: 
            the item arguemnt
        """
        self._array.append(item)
        return item 
    

    def pop(self)->Item: 
        """
        remove the top object of this stack
        Return: 
            the object at the top of this stack(The last item of the object)

        Raise:  
            ValueError if this stack is empty
        """
        self.peek()
        return self._array.pop()

   
    def peek(self)->Item: 
        """
        Return: 
            the object at the top of this stack(The last item of the object)

        Raise:  
            ValueError if this stack is empty
        """
        size:int = len(self._array)
        if (size == 0): 
            raise ValueError("the stack list is empty")
        
        return self._array[size - 1 ]
    
    
    def empty(self)->bool: 
        return len(self._array) == 0
    
    
    def search(self,obj:Item)->int: 
        """
        Return the 1-based position where an object is on this stack. 
        if the param 'obj' occurs as an item in this stack, this method return 
        the distance from the top of the stack of the occurence nearest the top of the stack; 
        the topmost item on the stack is considered to be at distance. 
        Parameters: 
            :obj: the desired object

        Return: 
            the 1-based position from the top of the stack where the object is located. 
        
        """
        try: 
            index: int = self._array.index(obj)
            return len(self._array) - index 
        except ValueError : 
            return -1 


    

    @property
    def stack(self): 
        return self._array



# TypeVar is used for generic type hinting, similar to <E> in Java.

class _Node( Generic[Item]): 
    def __init__(self,
                 data:Item,
                 prev_node:Optional['_Node']=None, 
                 next_node: Optional['_Node']=None
                 ) -> None:
        self.data = data
        self.prev = prev_node
        self.next = next_node 
        
class LinkedList( QueueInterface[Item] ): 
    """_summary_
        A linked list is a linear data structure that stores a collection of data elements
        in a sequence. Unlike an array, a linked list does not store its elements in contiguous
        memory locations. Instead, it consists of individual objects called nodes, where each node
        contains the data itself and a reference (or link) to the next node in the sequence
    
    Core components
        Node: The fundamental building block of a linked list. It contains two parts: the data and a pointer to the next node.
        Head: A reference to the first node in the list. This is the starting point for all operations.
        Tail: A reference to the last node in the list. In a standard linked list, this node's next pointer is None (or null).
        
        
    Types of linked lists
        Singly-linked list: Each node points only to the next node in the sequence. Traversal is possible in only one direction.
        Doubly-linked list: Each node has two references: one to the next node and one to the previous node.
        This allows for traversal in both forward and backward directions.
        Circular linked list: The last node points back to the first node, forming a loop. 


    How it works
        The LinkedList class manages the overall structure by keeping track of the head and tail nodes.
        Operations like adding or removing elements involve changing the pointers of the nodes, which
        can be done without reallocating or shifting the entire structure. 
        
    Advantages and disadvantages
        Advantages
           - Dynamic size: Can easily grow or shrink at runtime without the need for fixed-size memory allocation;
           - Efficient modifications: Inserting or deleting elements is fast and easy, especially at the beginning of the list.
            
        Disadvantages
                - Slower access: Retrieving an element by its position is inefficient, requiring a linear scan; 
                -  Higher memory usage: The extra space needed for pointers results in a higher memory footprint compared to arrays. 

    Args:
        QueueInterface (_type_): _description_
            This is the same to do this in typeScript:
                myList = LinkList<number>([1,2,3,4])
                
    Example: 
        >>> my_list:LinkList[int] = LinkList([1,2,3,4])
        >>> a:bool= my_list.offer(5)
        >>> b:int = my_list.remove()
                
    """
    def __init__(self,data:Iterable[Item]=()) -> None:
        self._size:int = 0 
        self._head:Optional[_Node[Item]] = None
        self._tail:Optional[_Node[Item]] = None
        
        if data: 
            self.extend(data)
            
        
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}([{', '.join([repr(item) for item in self ])} "
        
    def __len__(self) -> int:
        return self._size
    
    def __iter__(self) -> Iterator:
        node = self._head
        while node: 
            yield node.data
            node = node.next 
        
    def __contains__(self, __x: object) -> bool:
        for item in self:
            if item == __x:
                return True
            
        return False
        
    #private function to be used withtin this class. helpers
    #function to work wiht the last element (tail)
    def _link_last(self,element:Item)->None: 
        last_Data:Optional[_Node] = self._tail
         
        new_data:_Node  = _Node(element,last_Data,None)
        self._tail = new_data
        
        if last_Data is None: 
            self._head = new_data

        else:
            last_Data.next = new_data

        
        self._size += 1 
    
    def _add_last(self,element:Item)->None: 
        self._link_last(element)
        
        
    def _unlink_first(self)->Item : 
        if self._head is None: 
            raise IndexError("The linkList is empty")
        
        head = self._head
        data= self._head.data
        
        self._head = head.next
        
        if self._head is None: 
            self._tail =  None 
        else: 
            self._head.prev = None 
        
        self._size -= 1 
        return data
        
    def _remove_first(self): 
        return self._unlink_first()
        
        
    #The main function to the programer can use 
    def add(self,element:Item)->None: 
        self._add_last(element)
        
    def offer(self,element:Item)->bool:
        try: 
            self._add_last(element)
            return True
        except: 
            return False
    
    def extend(self,iterable:Iterable[Item])->None: 
        for item in iterable: 
            self._add_last(item)
            
    def remove(self)->Item : 
        return self._remove_first()
    
    def poll(self)->None | Item : 
        try: 
            return self._remove_first()
        except: 
            return None 
            
            
            
            
            
    def size(self)->int: 
        return self._size
    
    
    
    def peek(self)->Item|None: 
        if self._head is None: 
            return None 
        return self._head.data
        
        
    
    def peek_last(self)->Item | None : 
        if self._tail is None:
            return None 
        return self._tail.data     
    
    
    def element(self)->Item: 
        if self._head is None: 
            raise IndexError("The LinkList is empty")
        return   self._head.data
    
    def empty(self)->bool:
        return self._head ==  None    
        

Priority = TypeVar("Priority",bound=Callable[...,Any])

class PriorityQueue(QueueInterface[Item]): 
    def __init__(self,data:Iterable[Item]=(),key:Optional[Callable[[Item],Any]]=None) -> None:
        self._data =list(data)
        heapq.heapify(self._data)
            
        
        
    def __iter__(self) -> Iterator[Item]:
        return iter(self._data)
        
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}([{', '.join([str(x) for x in self])}])"
       
    def __len__(self) -> int:
        return len(self._data) 
    
    def __contains__(self, __x: object) -> bool:
        return __x in self._data
        
    def _assert(self)->None:
        if self.empty(): 
            raise IndexError("The Object is empty")    
        
    def _add_item(self,element:Item)->None: 
        heapq.heappush(self._data,element)
        
        
        
    def _remove_first(self)->Item:
     
        
        return heapq.heappop(self._data)
    
    
    
        

    def add(self,element:Item)->None:
        self._add_item(element)
        
        
    def offer(self,element)->bool: 
        self._add_item(element)
        return True 
    
    def extend(self,iterables:Iterable[Item])->None: 
        for item in iterables:
            self.offer(item)
    
    def poll(self) -> Item | None:
        if self.empty(): 
            return None 
        
        return self._remove_first()
    
    def remove(self) -> Item:
        self._assert()
        return self._remove_first()
    
    def peek(self) -> Item | None:
        if self.empty(): 
            return None 
        
        return heapq.nsmallest(1,self._data)[0]
    
    def element(self) -> Item:
        self._assert()
        return self._data[0]
        
    
    def empty(self)->bool:
        return not bool(self._data)
    
    def size(self): 
        return len(self._data)
    
        
        
        

