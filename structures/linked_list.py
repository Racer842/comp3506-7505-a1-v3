"""
Skeleton for COMP3506/7505 A1, S2, 2024
The University of Queensland
Joel Mackenzie and Vladimir Morozov
"""

# so we can hint Node get_next
from __future__ import annotations

from typing import Any


class Node:
    """
    A simple type to hold data and a next pointer
    """

    def __init__(self, data: Any) -> None:
        self._data = data  # This is the payload data of the node
        self._next = None  # This is the "next" pointer to the next Node
        self._prev = None  # This is the "previous" pointer to the previous Node

    def set_data(self, data: Any) -> None:
        self._data = data

    def get_data(self) -> Any:
        return self._data

    def set_next(self, node: Node) -> None:
        self._next = node

    def get_next(self) -> Node | None:
        return self._next

    def set_prev(self, node: Node) -> None:
        self._prev = node

    def get_prev(self) -> Node | None:
        return self._prev


class DoublyLinkedList:
    """
    Your doubly linked list code goes here.
    Note that any time you see `Any` in the type annotations,
    this refers to the "data" stored inside a Node.

    [V3: Note that this API was changed in the V3 spec] 
    """

    def __init__(self) -> None:
        # You probably need to track some data here...
        self._head = None
        self._tail = None
        self._size = 0
        self._reversed = 0
        self._reversed_input_occuring = 0


    def __str__(self) -> str:
        """
        A helper that allows you to print a DoublyLinkedList type
        via the str() method.
        """
        string_rep = ""
        cur = self._head
        while cur is not None:
            # Assumes the data stored in cur has __str__ implemented
            string_rep += str(cur.get_data()) + " <-> "
            cur = cur.get_next()
        string_rep += "[EOL]"  # end of list == None
        
        return string_rep

    """
    Simple Getters and Setters below
    """

    def get_size(self) -> int:
        """
        Return the size of the list.
        Time complexity for full marks: O(1)
        """
        return self._size

    def get_head(self) -> Any | None:
        """
        Return the data of the leftmost node in the list, if it exists.
        Time complexity for full marks: O(1)
        """
        if self._reversed == 1:
            return self._tail.get_data()
        return self._head.get_data()
        

    def set_head(self, data: Any) -> None:
        """
        Replace the leftmost node's data with the given data.
        If the list is empty, do nothing.
        Time complexity for full marks: O(1)
        """
        self._head = data

    def get_tail(self) -> Any | None:
        """
        Return the data of the rightmost node in the list, if it exists.
        Time complexity for full marks: O(1)
        """
        if self._reversed == 1:
            return self._head.get_data()
        return self._tail.get_data()

    def set_tail(self, data: Any) -> None:
        """
        Replace the rightmost node's data with the given data.
        If the list is empty, do nothing.
        Time complexity for full marks: O(1)
        """
        self._tail = data

    """
    More interesting functionality now.
    """

    def insert_to_front(self, data: Any) -> None:
        """
        Insert the given data to the front of the list.
        Hint: You will need to create a Node type containing
        the given data.
        Time complexity for full marks: O(1)
        """

        if self._reversed == 0 or self._reversed_input_occuring == 1:

            new_node = Node(data)
            #If list is empty
            if self._head is None:
                new_node.set_prev(None)
                self.set_head(new_node)
                self.set_tail(new_node)
            else:
                if self._size == 1:
                    self.set_head(new_node)
                    self._head.set_next(self._tail) 
                    self._tail.set_prev(self._head)
                    
                else:
                    self._head.set_prev(new_node)
                    new_node.set_next(self._head)
                    self.set_head(new_node)
            
            self._size += 1
            self._reversed_input_occuring = 0
        else:
            self._reversed_input_occuring = 1
            self.insert_to_back(data)

    def insert_to_back(self, data: Any) -> None:
        """
        Insert the given data (in a node) to the back of the list
        Time complexity for full marks: O(1)
        """

        if self._reversed == 0 or self._reversed_input_occuring == 1:
            
            new_node = Node(data)
            
            # If list is empty
            if self._head is None:
                new_node.set_prev(None)
                self.set_head(new_node)
                self.set_tail(new_node)

            else:
                if self._size == 1:
                    self.set_tail(new_node)
                    self._head.set_next(self._tail) 
                    self._tail.set_prev(self._head)
                else:
                    self._tail.set_next(new_node)
                    new_node.set_prev(self._tail)
                    self.set_tail(new_node)
        
            self._size += 1
            self._reversed_input_occuring = 0
        else:
            self._reversed_input_occuring = 1
            self.insert_to_front(data)

    def remove_from_front(self) -> Any | None:
        """
        Remove the front node, and return the data it holds.
        Time complexity for full marks: O(1)
        """
        if self._size == 0:
            return None
        
        #dele_node = self._head
        if self._reversed == 0:
            del_node = self._head
            self._head = self._head.get_next()
            self._head.set_prev(None)
        else:
            del_node = self._tail
            self._tail = self._tail.get_prev()
            self._tail.set_next(None)
        
        self._size -= 1
        
        return del_node.get_data()
        

    def remove_from_back(self) -> Any | None:
        """
        Remove the back node, and return the data it holds.
        Time complexity for full marks: O(1)
        """
        if self._size == 0:
            return None

        if self._reversed == 0:
            del_node = self._tail
            self._tail = self._tail.get_prev()
            self._tail.set_next(None)
        else:
            del_node = self._head
            self._head = self._head.get_next()
            self._head.set_prev(None)
        
        self._size -= 1

        return del_node.get_data()

    def find_element(self, elem: Any) -> bool:
        """
        Looks at the data inside each node of the list and returns True
        if a match is found; False otherwise.
        Time complexity for full marks: O(N)
        """
        cur_pos = self._head
        while cur_pos is not None:
            if cur_pos.get_data() == elem:
                return True
            cur_pos = cur_pos.get_next()
        return False

    def find_and_remove_element(self, elem: Any) -> bool:
        """
        Looks at the data inside each node of the list; if a match is
        found, this node is removed from the linked list, and True is returned.
        False is returned if no match is found.
        Time complexity for full marks: O(N)
        """
        curr_pos = self._head
        while curr_pos is not None:
            # If the head is the elem
            if curr_pos.get_data() == elem and curr_pos == self._head:
                if not curr_pos.get_next():
                    curr_pos = None
                    self.set_head(None)
                    self._size -= 1
                    return True
                else: # If an element after head exist
                   nxt_elem = curr_pos.get_next()
                   curr_pos.set_next(None)
                   nxt_elem.set_prev(None)
                   curr_pos.set_data(None)
                   self.set_head(nxt_elem)
                   self._size -= 1
                   return True
            elif curr_pos.get_data() == elem:
                if curr_pos.get_next():
                    nxt_elem = curr_pos.get_next()
                    prev_elem = curr_pos.get_prev()
                    prev_elem.set_next(nxt_elem)
                    nxt_elem.set_prev(prev_elem)
                    curr_pos.set_next(None)
                    curr_pos.set_prev(None)
                    curr_pos.set_data(None)
                    self._size -= 1
                    return True
                else: # IF element is at the end of the list
                    last_elem_before_curr = curr_pos.get_prev()
                    self.set_tail(last_elem_before_curr)
                    self._tail.set_next(None)
                    curr_pos.set_prev(None)
                    curr_pos.set_data(None)
                    self._size -= 1
                    return True
            curr_pos = curr_pos.get_next()
        return False


    def reverse(self) -> None:
        """
        Reverses the linked list
        Time complexity for full marks: O(1)
        """
        # Set flag to dicide which way the list is to br read. e.g. if flag = 1 then read backwards 0 read normal direction
        if self._reversed == 0:
            self._reversed = 1
        else:
            self._reversed = 0

