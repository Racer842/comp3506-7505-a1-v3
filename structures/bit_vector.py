"""
Skeleton for COMP3506/7505 A1, S2, 2024
The University of Queensland
Joel Mackenzie and Vladimir Morozov
"""

from typing import Any

from structures.dynamic_array import DynamicArray


class BitVector:
    """
    A compact storage for bits that uses DynamicArray under the hood.
    Each element stores up to 64 bits, making BitVector 64 times more memory-efficient
    for storing bits than plain DynamicArray.
    """

    BITS_PER_ELEMENT = 64

    def __init__(self) -> None:
        """
        We will use the dynamic array as our data storage mechanism
        """
        self._data = DynamicArray()
        self._start_bit_pos = 0
        self._end_bit_pos = 0
        self._size = 0
        self._num_of_bits = 0
        self._reverse = 0
        self._reverse_happening = 0
        self._flip = 0

        # you may want or need more stuff here in the constructor

    def __str__(self) -> str:
        """
        A helper that allows you to print a BitVector type
        via the str() method.
        """
        bit_string = "Vector: "
        bits_to_print = self._num_of_bits
        value = 0

        for i in range(0, self._size):
            if self._start_bit_pos and i == 0:
                value += self._data[i]
            else:
                value += (self._data[i] << (self._start_bit_pos + 64 * (i - 1)))

        while bits_to_print > 0:
            bit_string += "{} ".format(bin(value & 0xFFFFFFFFFFFFFFFF))
            value = value >> 64
            bits_to_print -= 64

        return bit_string

    def __resize(self) -> None:
        pass

    def get_at(self, index: int) -> int | None:
        """
        Get bit at the given index.
        Return None if index is out of bounds.
        Time complexity for full marks: O(1)
        """
        return self.__getitem__(index)

    def __getitem__(self, index: int) -> int | None:
        """
        Same as get_at.
        Allows to use square brackets to index elements.
        """
        if index >= self._num_of_bits or index < 0:
            return None
        
        if self._reverse == 1:
            index = self._num_of_bits - index - 1

        mask = 1

        # Deals with when more than one element in the array
        if (index >= self._start_bit_pos) and (self._num_of_bits > 64):
            shifted_index = index - self._start_bit_pos
            pos = ((shifted_index) // 64) + 1
            stored_data = self._data[pos] >> (shifted_index % 64)

            if self._flip == 1:
                if (stored_data & mask) == 1:
                    return 0
                else:
                    return 1

            return stored_data & mask
        else:
            stored_data = self._data[0] >> index

            if self._flip == 1:
                if (stored_data & mask) == 1:
                    return 0
                else:
                    return 1

            return stored_data & mask

    def set_at(self, index: int) -> None:
        """
        Set bit at the given index to 1.
        Do not modify the vector if the index is out of bounds.
        Time complexity for full marks: O(1)
        """
        self.__setitem__(index, 1)

    def unset_at(self, index: int) -> None:
        """
        Set bit at the given index to 0.
        Do not modify the vector if the index is out of bounds.
        Time complexity for full marks: O(1)
        """
        self.__setitem__(index, 0)

    def __setitem__(self, index: int, state: int) -> None:
        """
        Set bit at the given index.
        Treat the integer in the same way Python does:
        if state is 0, set the bit to 0, otherwise set the bit to 1.
        Do not modify the vector if the index is out of bounds.
        Time complexity for full marks: O(1)
        """
        if index >= self._num_of_bits:
            return None
        
        if self._reverse == 1:
            index = self._num_of_bits - index - 1
        
        if self._flip == 1:
            if (state):
                state = 0
            else:
                state = 1
        
        if (state):
            # Deals with when more than one element in the array
            if (index >= self._start_bit_pos) and (self._num_of_bits > 64):
                shifted_index = index - self._start_bit_pos
                pos = (shifted_index // 64) + 1
                mask = (1 << (shifted_index % 64))
                self._data[pos] |= mask
            else:
                mask = (1 << index)
                self._data[0] |= mask
        else:
            if (index >= self._start_bit_pos) and (self._num_of_bits > 64):
                shifted_index = index - self._start_bit_pos
                pos = ((shifted_index) // 64) + 1
                mask = ~(1 << (shifted_index % 64))
                self._data[pos] &= mask
            else:
                mask = ~(1 << index)
                self._data[0] &= mask

    def append(self, state: int) -> None:
        """
        Add a bit to the back of the vector.
        Treat the integer in the same way Python does:
        if state is 0, set the bit to 0, otherwise set the bit to 1.
        Time complexity for full marks: O(1*)
        """
        if self._reverse == 0 or self._reverse_happening == 1:

            self._reverse_happening = 0

            if self._flip == 1:
                if (state):
                    state = 0
                else:
                    state = 1

            # Do any resizing if needed
            if self._size == 0 and self._num_of_bits == 0:
                self._data.append(0)
                self._size += 1
        
            if self._end_bit_pos == 64:
                self._size += 1
                self._data.append(0)
                self._end_bit_pos = 0
        
            if (state):
                # Deals when int array only has one element
                if self._num_of_bits < 64:
                    mask = self._num_of_bits % 64
                    self._data[0] |= 1 << mask
                else:
                    mask = (self._num_of_bits - self._start_bit_pos) % 64
                    self._data[((self._num_of_bits - self._start_bit_pos) // 64) + 1] |= 1 << mask
            
            self._end_bit_pos += 1

            if self._size == 1:
                self._start_bit_pos += 1

            self._num_of_bits += 1
        else:
            self._reverse_happening = 1
            self.prepend(state)

    def prepend(self, state: Any) -> None:
        """
        Add a bit to the front of the vector.
        Treat the integer in the same way Python does:
        if state is 0, set the bit to 0, otherwise set the bit to 1.
        Time complexity for full marks: O(1*)
        """
        if self._reverse == 0 or self._reverse_happening == 1:

            self._reverse_happening = 0

            if self._flip == 1:
                if (state):
                    state = 0
                else:
                    state = 1

            if self._size == 0 and self._num_of_bits == 0:
                self._data.append(0)
                self._size += 1
        
            if self._start_bit_pos == 64:
                self._size += 1
                self._data.prepend(0)
                self._start_bit_pos = 0
        
            self._data[0] <<= 1

            if (state):
                self._data[0] += 1

            self._start_bit_pos += 1
            self._num_of_bits += 1
        
            if self._size == 1:
                self._end_bit_pos += 1 
        else:
            self._reverse_happening = 1
            self.append(state)

    def reverse(self) -> None:
        """
        Reverse the bit-vector.
        Time complexity for full marks: O(1)
        """
        if self._reverse == 0:
            self._reverse = 1
        else:
            self._reverse = 0

    def flip_all_bits(self) -> None:
        """
        Flip all bits in the vector.
        Time complexity for full marks: O(1)
        """
        if self._flip == 0:
            self._flip = 1
        else:
            self._flip = 0

    def shift(self, dist: int) -> None:
        """
        Make a bit shift.
        If dist is positive, perform a left shift by `dist`.
        Otherwise perform a right shift by `dist`.
        Time complexity for full marks: O(N)
        """
        if self._num_of_bits == 0:
            return None

        if dist == 0:
            return None
        
        if self._reverse == 1:
            dist = -1*dist
        
        value = 0

        # Create a single large value
        for i in range(0, self._size):
            if self._start_bit_pos and i == 0:
                value += self._data[i]
            else:
                value += (self._data[i] << (self._start_bit_pos + 64 * (i - 1)))
        
        # Bit shift the created value
        if dist > 0:
            value = value >> dist
        else:
            value = value << abs(dist)
        
        # Rebuild _data from the shifted value
        for i in range(self._size):
            if i == 0:
                self._data[i] = value & (2**self._start_bit_pos - 1)
            else:
                self._data[i] = (value >> (self._start_bit_pos + 64 * (i - 1))) & ((1 << 64) - 1)


    def rotate(self, dist: int) -> None:
        """
        Make a bit rotation.
        If dist is positive, perform a left rotation by `dist`.
        Otherwise perform a right rotation by `dist`.
        Time complexity for full marks: O(N)
        """
        if self._num_of_bits == 0:
            return None

        if dist == 0:
            return None
        
        if self._reverse == 1:
            dist = -1*dist

        # Account for when the input dist is greater than the num of bits present
        if dist < -self._num_of_bits and dist < 0:
            dist = dist % self._num_of_bits
            dist -= self._num_of_bits
        
        if dist > self._num_of_bits and dist > 0:
            dist = dist % self._num_of_bits

        value = 0

        # Create a single large value
        for i in range(0, self._size):
            if self._start_bit_pos and i == 0:
                value += self._data[i]
            else:
                value += (self._data[i] << (self._start_bit_pos + 64 * (i - 1)))
        
        if dist > 0:  # Left rotate
            value = ((value << dist) | (value >> (self._num_of_bits - dist))) & ((1 << self._num_of_bits) - 1)
        else:  # Right rotate
            value = ((value >> abs(dist)) | (value << (self._num_of_bits - abs(dist)))) & ((1 << self._num_of_bits) - 1)
        
        # Rebuild _data from the shifted value
        for i in range(self._size):
            if i == 0:
                self._data[i] = value & (2**self._start_bit_pos - 1)
            else:
                self._data[i] = (value >> (self._start_bit_pos + 64 * (i - 1))) & ((1 << 64) - 1)


    def get_size(self) -> int:
        """
        Return the number of *bits* in the list
        Time complexity for full marks: O(1)
        """
        return self._num_of_bits
    
    def main_character_bit_vector(self) -> None:
        """
        Function purely used for main character warm up task
        """
        increased_list = [0] * (2**26)
        self._size = 2**26
        self._num_of_bits = (2**32)
        self._end_bit_pos = (2**32) - 1
        self._start_bit_pos = 0
        self._data.store_existing_array(increased_list, self._size)

