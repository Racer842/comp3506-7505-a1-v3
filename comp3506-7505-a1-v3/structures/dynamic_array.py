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

        abs_zero = 0 

        # Copy old data to new slab of memory
        for i in range(0, self._size):
            if self._start_pos != 0:
                if (self._start_pos + i) < self._capacity:
                    resized_data[i] = self._data[self._start_pos + i]
                else:
                    resized_data[i] = self._data[abs_zero]
                    abs_zero += 1
            else:
                resized_data[i] = self._data[i]

        self._start_pos = 0
        self._end_pos = self._size
        self._capacity = new_capacity
        self._data = resized_data

    def get_at(self, index: int) -> Any | None:
        """
        Get element at the given index.
        Return None if index is out of bounds.
        Time complexity for full marks: O(1)
        """
        if self._size == 0:
            return None
        
        if index < 0 or index >= self._size:
            return None
        
        return self.__getitem__(index)

    def __getitem__(self, index: int) -> Any | None:
        """
        Same as get_at.
        Allows to use square brackets to index elements.
        """
        if self._size == 0:
            return None
        
        if index < 0 or index >= self._size:
            return None

        if self._start_pos != 0:
            if (self._start_pos + index) < self._capacity:
                return self._data[self._start_pos + index]
            else:
                altered_index = self._capacity - (self._start_pos + index)
                if altered_index < 0:
                    altered_index = -1*altered_index
                return self._data[altered_index]

        return self._data[index]

    def set_at(self, index: int, element: Any) -> None:
        """
        Get element at the given index.
        Do not modify the list if the index is out of bounds.
        Time complexity for full marks: O(1)
        """
        if self._size == 0:
            return None
        elif index < 0 or index >= self._size:
            return None

        self.__setitem__(index, element)

    def __setitem__(self, index: int, element: Any) -> None:
        """
        Same as set_at.
        Allows to use square brackets to index elements.
        """
        pass

    def append(self, element: Any) -> None:
        """
        Add an element to the back of the array.
        Time complexity for full marks: O(1*) (* means amortized)
        """
        if self._capacity <= self._size:
            self.__resize()

        

    def prepend(self, element: Any) -> None:
        """
        Add an element to the front of the array.
        Time complexity for full marks: O(1*)
        """
        if self._capacity <= self._size:
            self.__resize()

        

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
        pass


    def remove_at(self, index: int) -> Any | None:
        """
        Remove the element at the given index from the array and return the removed element.
        If there is no such element, leave the array unchanged and return None.
        Time complexity for full marks: O(N)
        """
        # Possibly do some shift flag. Identity the poistion at which the elem is at and store,
        # If an actually value above said position exist then move down.
        pass

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
        sorted_data = [None] * self._size
        index_pos = self._start_pos
        pass

    def __merge(self, left, left_length, right, right_len) -> Any:
        pass

    def __mergesort(self, sorted_array, array_size) -> Any:
        pass


# def __init__(self) -> None:
#         self._size = 0
#         self._capacity = 4
#         self._start_pos = 0
#         self._end_pos = 0
#         self._data = [None] * 4
#         self._reverse = 0

#     def __str__(self) -> str:
#         """
#         A helper that allows you to print a DynamicArray type
#         via the str() method.
#         """
#         string_rep = "["

#         for i in range(0, self._capacity):
#             # Get string representation of data and add to output
#             string_rep += str(self._data[i])

#             # Add comma if data is not the last element
#             if i < (self._capacity - 1):
#                 string_rep += ", "

#         string_rep += "]"

#         return string_rep

#     def __resize(self) -> None:
        
#         new_capacity = self._capacity * 2
#         resized_data = [None] * new_capacity

#         abs_zero = 0 

#         # Copy old data to new slab of memory
#         for i in range(0, self._size):
#             if self._start_pos != 0:
#                 if (self._start_pos + i) < self._capacity:
#                     resized_data[i] = self._data[self._start_pos + i]
#                 else:
#                     resized_data[i] = self._data[abs_zero]
#                     abs_zero += 1
#             else:
#                 resized_data[i] = self._data[i]

#         self._start_pos = 0
#         self._end_pos = self._size
#         self._capacity = new_capacity
#         self._data = resized_data

#     def get_at(self, index: int) -> Any | None:
#         """
#         Get element at the given index.
#         Return None if index is out of bounds.
#         Time complexity for full marks: O(1)
#         """
#         if self._size == 0:
#             return None
        
#         if index < 0 or index >= self._size:
#             return None
        
#         return self.__getitem__(index)

#     def __getitem__(self, index: int) -> Any | None:
#         """
#         Same as get_at.
#         Allows to use square brackets to index elements.
#         """
#         if self._size == 0:
#             return None
        
#         if index < 0 or index >= self._size:
#             return None

#         if self._start_pos != 0:
#             if (self._start_pos + index) < self._capacity:
#                 return self._data[self._start_pos + index]
#             else:
#                 altered_index = self._capacity - (self._start_pos + index)
#                 if altered_index < 0:
#                     altered_index = -1*altered_index
#                 return self._data[altered_index]

#         return self._data[index]

#     def set_at(self, index: int, element: Any) -> None:
#         """
#         Get element at the given index.
#         Do not modify the list if the index is out of bounds.
#         Time complexity for full marks: O(1)
#         """
#         if self._size == 0:
#             return None
#         elif index < 0 or index >= self._size:
#             return None

#         self.__setitem__(index, element)

#     def __setitem__(self, index: int, element: Any) -> None:
#         """
#         Same as set_at.
#         Allows to use square brackets to index elements.
#         """
#         if self._data[index] == None:
#             self._data[index] = element
#             self._size += 1
#         elif self._start_pos != 0:
#             if (self._start_pos + index) < self._capacity:
#                 self._data[self._start_pos + index] = element
#             else:
#                 altered_index = self._capacity - (self._start_pos + index)
#                 if altered_index < 0:
#                     altered_index = -1*altered_index
#                 self._data[altered_index] = element
#         else:
#             self._data[index] = element

#     def append(self, element: Any) -> None:
#         """
#         Add an element to the back of the array.
#         Time complexity for full marks: O(1*) (* means amortized)
#         """
#         if self._capacity <= self._size:
#             self.__resize()

#         self._data[self._end_pos] = element
#         self._end_pos += 1
#         self._size += 1

#     def prepend(self, element: Any) -> None:
#         """
#         Add an element to the front of the array.
#         Time complexity for full marks: O(1*)
#         """
#         if self._capacity <= self._size:
#             self.__resize()

#         if self._start_pos - 1 < 0:
#             self._start_pos = self._capacity - 1
#             self._data[self._capacity] = element
#         else:
#             self._start_pos -= 1
#             self._data[self._start_pos] = element
#         self._size += 1

#     def reverse(self) -> None:
#         """
#         Reverse the array.
#         Time complexity for full marks: O(1)
#         """
#         if self._reverse == 0:
#             self._reverse = 1
#         else:
#             self._reverse = 0

#     def remove(self, element: Any) -> None:
#         """
#         Remove the first occurrence of the element from the array.
#         If there is no such element, leave the array unchanged.
#         Time complexity for full marks: O(N)
#         """
#         # Similar as remove_at but using an actually element
#         first_instance_found = 0
#         new_array = [None]*self._capacity
#         new_array_index = 0

#         for i in range(0, self._size):
#             if self._start_pos != 0:
#                 if (self._start_pos + i) < self._capacity:
#                     if self._data[self._start_pos + i] == element and first_instance_found == 0:
#                         first_instance_found = 1
#                     else:
#                         new_array[new_array_index] = self._data[self._start_pos + i]
#                         new_array_index += 1
#                 else:
#                     altered_index = self._capacity - (self._start_pos + i)
#                     if altered_index < 0:
#                         altered_index = -1*altered_index
#                     if self._data[altered_index] == element and first_instance_found == 0:
#                         first_instance_found = 1
#                     else:
#                         new_array[new_array_index] = self._data[altered_index]
#                         new_array_index += 1
#             else:
#                 if self._data[i] == element and first_instance_found == 0:
#                         first_instance_found = 1
#                 else:
#                     new_array[new_array_index] = self._data[i]
#                     new_array_index += 1
        
#         if first_instance_found == 1:
#             self._size -= 1
#             self._data = new_array
#             self._start_pos = 0
#             self._end_pos = self._size


#     def remove_at(self, index: int) -> Any | None:
#         """
#         Remove the element at the given index from the array and return the removed element.
#         If there is no such element, leave the array unchanged and return None.
#         Time complexity for full marks: O(N)
#         """
#         # Possibly do some shift flag. Identity the poistion at which the elem is at and store,
#         # If an actually value above said position exist then move down.
#         first_instance_found = 0
#         new_array = [None]*self._capacity
#         new_array_index = 0

#         for i in range(0, self._size):
#             if self._start_pos != 0:
#                 if (self._start_pos + i) < self._capacity:
#                     if i == index and first_instance_found == 0:
#                         first_instance_found = 1
#                     else:
#                         new_array[new_array_index] = self._data[self._start_pos + i]
#                         new_array_index += 1
#                 else:
#                     altered_index = self._capacity - (self._start_pos + i)
#                     if altered_index < 0:
#                         altered_index = -1*altered_index
#                     if self._data[altered_index] == element and first_instance_found == 0:
#                         first_instance_found = 1
#                     else:
#                         new_array[new_array_index] = self._data[altered_index]
#                         new_array_index += 1
#             else:
#                 if self._data[i] == element and first_instance_found == 0:
#                         first_instance_found = 1
#                 else:
#                     new_array[new_array_index] = self._data[i]
#                     new_array_index += 1
        
#         if first_instance_found == 1:
#             self._size -= 1
#             self._data = new_array
#             self._start_pos = 0
#             self._end_pos = self._size