from typing import (TypeVar)
from abc import (ABC, abstractmethod)
from collections.abc import (Collection)


Item = TypeVar('Item')
"""This type is the to use generic Type <Item> like in TypeScript"""

class QueueInterface( ABC,Collection[Item]):
    """
    An abstract base class representing a collection designed for holding
    elements prior to processing. Besides the methods inherited from
    Collection, this interface provides methods for adding, removing,
    and inspecting elements.

    The methods come in two forms: one throws an exception if the operation
    fails, the other returns a special value (None or False).
    """


    @abstractmethod
    def add(self, element: Item) -> None:
        """
        Inserts the specified element into this queue.
        
        Args:
            e: The element to add.
        
        Raises:
            Exception: If the element cannot be added due to capacity
                       restrictions or other implementation-specific issues.
        """
        pass

    @abstractmethod
    def offer(self, element: Item) -> bool:
        """
        Inserts the specified element into this queue if possible.
        
        Args:
            e: The element to add.
            
        Returns:
            True if the element was added, False otherwise.
        """
        pass

    @abstractmethod
    def remove(self) -> Item :
        """
        Retrieves and removes the head of this queue.
        
        Returns:
            The head of this queue.
            
        Raises:
            IndexError: If this queue is empty.
        """
        pass

    @abstractmethod
    def poll(self) -> Item | None:
        """
        Retrieves and removes the head of this queue, or returns None
        if this queue is empty.
        
        Returns:
            The head of this queue, or None if the queue is empty.
        """
        pass

    @abstractmethod
    def element(self) -> Item:
        """
        Retrieves, but does not remove, the head of this queue.
        
        Returns:
            The head of this queue.
            
        Raises:
            IndexError: If this queue is empty.
        """
        pass

    @abstractmethod
    def peek(self) -> Item | None:
        """
        Retrieves, but does not remove, the head of this queue, or
        returns None if this queue is empty.
        
        Returns:
            The head of this queue, or None if the queue is empty.
        """
        pass
