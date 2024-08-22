"""
Skeleton for COMP3506/7505 A1, S2, 2024
The University of Queensland
Joel Mackenzie and Vladimir Morozov
"""

from typing import Any


class DynamicArray:
    def __init__(self) -> None:
        self._size = 0
        self._capacity = 4
        self._start_pos = 0
        self._end_pos = 0
        self._data = [None] * 4
        self._reverse = 0
        self._reverse_happening = 0

    def __str__(self) -> str:
        """
        A helper that allows you to print a DynamicArray type
        via the str() method.
        """
        string_rep = "["

        for i in range(0, self._capacity):
            # Get string representation of data and add to output
            string_rep += str(self._data[i])

            # Add comma if data is not the last element
            if i < (self._capacity - 1):
                string_rep += ", "

        string_rep += "]"

        return string_rep

    def __resize(self) -> None:
        
        new_capacity = self._capacity * 2
        resized_data = [None] * new_capacity

        for i in range(0, self._size):
            resized_data[i] = self._data[self._start_pos + i]

        self._start_pos = 0
        self._end_pos = self._size - 1
        self._capacity = new_capacity
        self._data = resized_data

    def get_at(self, index: int) -> Any | None:
        """
        Get element at the given index.
        Return None if index is out of bounds.
        Time complexity for full marks: O(1)
        """
    
        return self.__getitem__(index)

    def __getitem__(self, index: int) -> Any | None:
        """
        Same as get_at.
        Allows to use square brackets to index elements.
        """
        if index < self._size and self._size != 0:
            if self._reverse == 0:
                shifted_index = self._start_pos + index
                return self._data[shifted_index]
            else:
                shifted_index = self._end_pos - index
                if shifted_index < 0:
                    shifted_index += self._capacity
                return self._data[shifted_index]

    def set_at(self, index: int, element: Any) -> None:
        """
        Get element at the given index.
        Do not modify the list if the index is out of bounds.
        Time complexity for full marks: O(1)
        """

        self.__setitem__(index, element)

    def __setitem__(self, index: int, element: Any) -> None:
        """
        Same as set_at.
        Allows to use square brackets to index elements.
        """
        if index < self._size and self._size != 0:
            if self._reverse == 0:
                shifted_index = self._start_pos + index
                self._data[shifted_index] = element
            else:
                shifted_index = self._end_pos - index
                if shifted_index < 0:
                    shifted_index += self._capacity
                self._data[shifted_index] = element

    def append(self, element: Any) -> None:
        """
        Add an element to the back of the array.
        Time complexity for full marks: O(1*) (* means amortized)
        """
        if self._capacity == self._size:
            self.__resize()

        if self._reverse == 0 or self._reverse_happening == 1:
            self._reverse_happening = 0
            if self.get_size() == 0:
                self._end_pos = 0
                self._start_pos = 0
            else:
                self._end_pos += 1

            self._data[self._end_pos] = element

            self._size += 1
        else:
            self._reverse_happening = 1
            self.prepend(element)

        

    def prepend(self, element: Any) -> None:
        """
        Add an element to the front of the array.
        Time complexity for full marks: O(1*)
        """
        if self._capacity == self._size:
            self.__resize()

        if self._reverse == 0 or self._reverse_happening == 1:
            self._reverse_happening = 0
            if self.get_size() == 0:
                self._end_pos = 0
                self._start_pos = 0
            else:
                self._start_pos -= 1

            self._data[self._start_pos] = element
            self._size += 1
        
        else:
            self._reverse_happening = 1
            self.append(element)
        

    def reverse(self) -> None:
        """
        Reverse the array.
        Time complexity for full marks: O(1)
        """
        if self._reverse == 0:
            self._reverse = 1
        else:
            self._reverse = 0

    def remove(self, element: Any) -> None:
        """
        Remove the first occurrence of the element from the array.
        If there is no such element, leave the array unchanged.
        Time complexity for full marks: O(N)
        """
        # Similar as remove_at but using an actually element
        found_elem = 0
        
        for i in range(0, self._size):
            if self.get_at(i) == element and found_elem == 0:
                found_elem = 1
                found_at = i
            else:
                if found_elem == 1 and i > found_at:
                    self.set_at(i - 1, self.get_at(i))
                    if i == self._size - 1:   
                        self.set_at(i, None)
        
        # Handles case when element is located at the end of the array
        if self._reverse == 0:
            if self._data[self._end_pos] == element:
                found_elem = 1
                self._data[self._end_pos] = None
        else:
            if self._data[self._start_pos] == element:
                found_elem = 1
                self._data[self._start_pos] = None

        # Ensures data is updated only if the element is found
        if found_elem:
            self._size -= 1
            if self._reverse == 0:
                self._end_pos -= 1
            else:
                self._start_pos += 1


    def remove_at(self, index: int) -> Any | None:
        """
        Remove the element at the given index from the array and return the removed element.
        If there is no such element, leave the array unchanged and return None.
        Time complexity for full marks: O(N)
        """
        # Possibly do some shift flag. Identity the poistion at which the elem is at and store,
        # If an actually value above said position exist then move down.
        found_index = 0
        data = None
        for i in range(0, self._size):
            if i == index:
                data = self.get_at(i)
                found_at = i
                found_index = 1
            if found_index == 1 and i > found_at:
                self.set_at(i - 1, self.get_at(i))
                if i == self._size - 1:   
                    self.set_at(i, None)

        if data is not None:
            self._size -= 1
            if self._reverse == 0:
                self._end_pos -= 1
            else:
                self._start_pos += 1
            return data
        else:
            return None

    def is_empty(self) -> bool:
        """
        Boolean helper to tell us if the structure is empty or not
        Time complexity for full marks: O(1)
        """
        if self._size == 0:
            return True
        return False

    def is_full(self) -> bool:
        """
        Boolean helper to tell us if the structure is full or not
        Time complexity for full marks: O(1)
        """
        if self.get_size() == self.get_capacity():
            return True
        return False

    def get_size(self) -> int:
        """
        Return the number of elements in the list
        Time complexity for full marks: O(1)
        """
        return self._size

    def get_capacity(self) -> int:
        """
        Return the total capacity (the number of slots) of the list
        Time complexity for full marks: O(1)
        """
        return self._capacity

    def sort(self) -> None:
        """
        Sort elements inside _data based on < comparisons.
        Time complexity for full marks: O(NlogN)
        """

        if self._size == 0:
            return None

        self.__mergesort(0, self._size) 
    
    def __merge(self, left_start, left_end, right_start, right_end) -> None:
        """
        Merge the data togther and store within the exisiting data array
        Code based on Week 2 Lecture code 2-mergesort.py
        """

        l_size = left_end - left_start
        r_size = right_end - right_start

        l_array = [None] * l_size
        r_array = [None] * r_size

        # Fill the left and right array
        for i in range(left_end - left_start):
            l_array[i] = self._data[(self._start_pos + left_start + i)]
    
        for i in range(right_end - right_start):
            r_array[i] = self._data[(self._start_pos + right_start + i)] 

        
        # Set input_index to left_start because that’s the index in self._data where the merging process begins.
        l, r, input_index = 0, 0, left_start

        # Two finger algorithm
        while l < l_size and r < r_size:
            if l_array[l] < r_array[r]:
                self._data[self._start_pos + input_index] = l_array[l]
                l += 1
            else:
                self._data[self._start_pos + input_index] = r_array[r]
                r += 1
            input_index += 1

        #Clean up list
        while l < l_size:
            self._data[self._start_pos + input_index] = l_array[l]
            l += 1
            input_index += 1

        while r < r_size:
            self._data[self._start_pos + input_index] = r_array[r]
            r += 1
            input_index += 1
    
    def __mergesort(self, start, end) -> None:
        """
        Find the lower and upped bounds needed for each resursion
        Code based on Week 2 Lecture code 2-mergesort.py
        """

        if end - start < 2:
            return None

        midpoint = (start + end) // 2

        self.__mergesort(start, midpoint)
        self.__mergesort(midpoint, end)

        self.__merge(start, midpoint, midpoint, end)

    
    def store_existing_array(self, array, size) -> None:
        self._data = array
        self._size = size
        self._capacity = size
        self._start_pos = 0
        self._end_pos = size - 1

