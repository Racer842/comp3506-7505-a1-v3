"""
Skeleton for COMP3506/7505 A1, S2, 2024
The University of Queensland
Joel Mackenzie and Vladimir Morozov

MallocLabs K-mer Querying Structure
"""

from typing import Any

"""
You may wish to import your data structures to help you with some of the
problems. Or maybe not.
"""
from structures.bit_vector import BitVector
from structures.dynamic_array import DynamicArray
from structures.linked_list import DoublyLinkedList, Node


class KmerStore:
    """
    A data structure for maintaining and querying k-mers.
    You may add any additional functions or member variables
    as you see fit.
    At any moment, the structure is maintaining n distinct k-mers.
    """

    def __init__(self, k: int) -> None:
        
        # self._sequence_data = DynamicArray()
        self._sequence_data = []
        self._size = 0
        self._kmer = k
        
        self._AA_compabile = 0
        self._AC_compabile = 0
        self._AG_compabile = 0
        self._AT_compabile = 0
        self._CA_compabile = 0
        self._CC_compabile = 0
        self._CG_compabile = 0
        self._CT_compabile = 0
        self._GA_compabile = 0
        self._GC_compabile = 0
        self._GG_compabile = 0
        self._GT_compabile = 0
        self._TA_compabile = 0
        self._TC_compabile = 0
        self._TG_compabile = 0
        self._TT_compabile = 0

    def read(self, infile: str) -> None:
        """
        Given a path to an input file, break the sequences into
        k-mers and load them into your data structure.
        """
        with open(infile, 'r') as file:
            data_info = file.readline()

    def batch_insert(self, kmers: list[str]) -> None:
        """
        Given a list of m k-mers, add the matching ones
        (including all duplicates).
        [V2: Correction]
        If the data structure contains n elements, and the input kmer list
        contains m elements, the targeted time complexity is:
        O(m log m) + O(n + m) amortized time (or better, of course!)

        Merge the data togther and store within the exisiting data array
        Code based on Week 2 Lecture code 2-mergesort.py
        
        """
        converted_kmers = DynamicArray()
        converted_kmers.store_existing_array(kmers, len(kmers))

        converted_kmers.sort()

        if self._size > 0:
            new_sequence_list = []
            inserted_index = 0
            existing_list_index = 0

            # Use the two finger algorithm from 2-mergesort.py
            # Recreate the sequence list in a sorted manner using the existing data and newly inputted data
            while existing_list_index < self._size and inserted_index < converted_kmers.get_size():
                if converted_kmers[inserted_index] <= self._sequence_data[existing_list_index]:
                    new_sequence_list.append(converted_kmers[inserted_index])
                    self.__compatible_update(converted_kmers[inserted_index][0], converted_kmers[inserted_index][1], 1)
                    inserted_index += 1
                else:
                    new_sequence_list.append(self._sequence_data[existing_list_index])
                    existing_list_index += 1
            
            # Ensure all the data still in the pre exisiting sequence list is stored into the new list
            while existing_list_index < self._size:
                new_sequence_list.append(self._sequence_data[existing_list_index])
                existing_list_index += 1
            
            # Ensure all data from the inserted list is stored into the new list
            while inserted_index < converted_kmers.get_size():
                new_sequence_list.append(converted_kmers[inserted_index])
                self.__compatible_update(converted_kmers[inserted_index][0], converted_kmers[inserted_index][1], 1)
                inserted_index += 1
            
            self._sequence_data = new_sequence_list
            self._size += converted_kmers.get_size()
        
        else:
            new_sequence_list = []
            inserted_index = 0

            while inserted_index < converted_kmers.get_size():
                new_sequence_list.append(converted_kmers[inserted_index])
                self.__compatible_update(converted_kmers[inserted_index][0], converted_kmers[inserted_index][1], 1)
                inserted_index += 1
            
            self._sequence_data = new_sequence_list
            self._size += converted_kmers.get_size()


    def batch_delete(self, kmers: list[str]) -> None:
        """
        Given a list of m k-mers, delete the matching ones
        (including all duplicates).
        [V2: Correction]
        If the data structure contains n elements, and the input kmer list
        contains m elements, the targeted time complexity is:
        O(m log m) + O(n + m) amortized time (or better, of course!)

        Code based on the lecture week 2 example of megre sort. More specifically the merge function
        """

        if self._size < 0:
            return None

        converted_kmers = DynamicArray()
        converted_kmers.store_existing_array(kmers, len(kmers))

        converted_kmers.sort()

        updated_sequence = []
        dele_index = 0
        existing_list_index = 0

        # Use the two finger algorithm from 2-mergesort.py
        while existing_list_index < self._size and dele_index < converted_kmers.get_size():
            if self._sequence_data[existing_list_index] < converted_kmers[dele_index]:
                updated_sequence.append(self._sequence_data[existing_list_index])
                existing_list_index += 1
            elif self._sequence_data[existing_list_index] > converted_kmers[dele_index]:
                dele_index += 1
            else:
                self.__compatible_update(self._sequence_data[existing_list_index][0], self._sequence_data[existing_list_index][1], 0)
                existing_list_index += 1

        while existing_list_index < self._size:
            updated_sequence.append(self._sequence_data[existing_list_index])
            existing_list_index += 1
        
        self._sequence_data = updated_sequence
        self._size = len(updated_sequence)

    def freq_geq(self, m: int) -> list[str]:
        """
        Given an integer m, return a list of k-mers that occur
        >= m times in your data structure.
        Time complexity for full marks: O(n)
        """
        "Return the kmer that has more than m duplicates"
        
        count = 1

        result = []
        previous = self._sequence_data[0]

        for i in range(1, self._size):
            current = self._sequence_data[i]
            if current == previous:
                count += 1
            else:
                if count >= m:
                    result.append(previous)
                previous = current
                count = 1

        if count >= m:
            result.append(previous)

        return result



    def count(self, kmer: str) -> int:
        """
        Given a k-mer, return the number of times it appears in
        your data structure.
        Time complexity for full marks: O(log n)

        Reference: Refer to statement.txt for references
        """
        
        first_occurence = self.__first_occurence(kmer)
        last_occurence = self.__last_occurence(kmer)

        if first_occurence == -1:
            return 0
        
        return last_occurence - first_occurence + 1

    def count_geq(self, kmer: str) -> int:
        """
        Given a k-mer, return the total number of k-mers that
        are lexicographically greater or equal.
        Time complexity for full marks: O(log n)
        """
        "Possibly use binary search"
        start, end = 0, self._size - 1
        first_geq = self._size

        while start <= end:
            midpoint = start + (end - start) // 2

            if self._sequence_data[midpoint] >= kmer:
                first_geq = midpoint
                end = midpoint - 1
            else:
                start = midpoint + 1

        # The number of k-mers greater that are lexicographically greater or equal
        return self._size - first_geq
    

    def compatible(self, kmer: str) -> int:
        """
        Given a k-mer, return the total number of compatible
        k-mers. You will be using the two suffix characters
        of the input k-mer to compare against the first two
        characters of all other k-mers.
        Time complexity for full marks: O(1) :-)
        """
        if kmer[self._kmer - 2] == 'A' and kmer[self._kmer - 1] == 'A':
            return self._TT_compabile
        if kmer[self._kmer - 2] == 'A' and kmer[self._kmer - 1] == 'C':
            return self._TG_compabile
        if kmer[self._kmer - 2] == 'A' and kmer[self._kmer - 1] == 'G':
            return self._TC_compabile
        if kmer[self._kmer - 2] == 'A' and kmer[self._kmer - 1] == 'T':
            return self._TA_compabile
        
        if kmer[self._kmer - 2] == 'C' and kmer[self._kmer - 1] == 'A':
            return self._GT_compabile
        if kmer[self._kmer - 2] == 'C' and kmer[self._kmer - 1] == 'C':
            return self._GG_compabile
        if kmer[self._kmer - 2] == 'C' and kmer[self._kmer - 1] == 'G':
            return self._GC_compabile
        if kmer[self._kmer - 2] == 'C' and kmer[self._kmer - 1] == 'T':
            return self._GA_compabile
        
        if kmer[self._kmer - 2] == 'G' and kmer[self._kmer - 1] == 'A':
            return self._CT_compabile
        if kmer[self._kmer - 2] == 'G' and kmer[self._kmer - 1] == 'C':
            return self._CG_compabile
        if kmer[self._kmer - 2] == 'G' and kmer[self._kmer - 1] == 'G':
            return self._CC_compabile
        if kmer[self._kmer - 2] == 'G' and kmer[self._kmer - 1] == 'T':
            return self._CA_compabile
        
        if kmer[self._kmer - 2] == 'T' and kmer[self._kmer - 1] == 'A':
            return self._AT_compabile
        if kmer[self._kmer - 2] == 'T' and kmer[self._kmer - 1] == 'C':
            return self._AG_compabile
        if kmer[self._kmer - 2] == 'T' and kmer[self._kmer - 1] == 'G':
            return self._AC_compabile
        if kmer[self._kmer - 2] == 'T' and kmer[self._kmer - 1] == 'T':
            return self._AA_compabile
        
        
    def __first_occurence(self, element):
        """
        Find the first occurence of a kmer
        Reference: See statement.txt
        """
        start, end, first_instance = 0, self._size - 1, -1

        while start <= end:
            midpoint = start + (end - start) // 2

            if self._sequence_data[midpoint] == element:
                first_instance = midpoint
                end = midpoint - 1
            elif self._sequence_data[midpoint] < element:
                start = midpoint + 1
            else:
                end = midpoint - 1
        
        return first_instance

    def __last_occurence(self, element):
        """
        Find the last occurence of a kmer
        Reference: See statement.txt
        """
        start, end, last_instance = 0, self._size - 1, -1

        while start <= end:
            midpoint = start + (end - start) // 2

            if self._sequence_data[midpoint] == element:
                last_instance = midpoint
                start = midpoint + 1
            elif self._sequence_data[midpoint] < element:
                start = midpoint + 1
            else:
                end = midpoint - 1
        
        return last_instance

    # Any other functionality you may need
    def __compatible_update(self, first_elem, second_elem, flag) ->None:
        """
        Updates how many compatiable kmers of each type exist
        """
        if flag == 1:
            if first_elem == 'A' and second_elem == 'A':
                self._AA_compabile += 1
            if first_elem == 'A' and second_elem == 'C':
                self._AC_compabile += 1
            if first_elem == 'A' and second_elem == 'G':
                self._AG_compabile += 1
            if first_elem == 'A' and second_elem == 'T':
                self._AT_compabile += 1

            if first_elem == 'C' and second_elem == 'A':
                self._CA_compabile += 1
            if first_elem == 'C' and second_elem == 'C':
                self._CC_compabile += 1
            if first_elem == 'C' and second_elem == 'G':
                self._CG_compabile += 1
            if first_elem == 'C' and second_elem == 'T':
                self._CT_compabile += 1
            
            if first_elem == 'G' and second_elem == 'A':
                self._GA_compabile += 1
            if first_elem == 'G' and second_elem == 'C':
                self._GC_compabile += 1
            if first_elem == 'G' and second_elem == 'G':
                self._GG_compabile += 1
            if first_elem == 'G' and second_elem == 'T':
                self._GT_compabile += 1
            
            if first_elem == 'T' and second_elem == 'A':
                self._TA_compabile += 1
            if first_elem == 'T' and second_elem == 'C':
                self._TC_compabile += 1
            if first_elem == 'T' and second_elem == 'G':
                self._TG_compabile += 1
            if first_elem == 'T' and second_elem == 'T':
                self._TT_compabile += 1
        else:
            if first_elem == 'A' and second_elem == 'A':
                self._AA_compabile -= 1
            if first_elem == 'A' and second_elem == 'C':
                self._AC_compabile -= 1
            if first_elem == 'A' and second_elem == 'G':
                self._AG_compabile -= 1
            if first_elem == 'A' and second_elem == 'T':
                self._AT_compabile -= 1

            if first_elem == 'C' and second_elem == 'A':
                self._CA_compabile -= 1
            if first_elem == 'C' and second_elem == 'C':
                self._CC_compabile -= 1
            if first_elem == 'C' and second_elem == 'G':
                self._CG_compabile -= 1
            if first_elem == 'C' and second_elem == 'T':
                self._CT_compabile -= 1
            
            if first_elem == 'G' and second_elem == 'A':
                self._GA_compabile -= 1
            if first_elem == 'G' and second_elem == 'C':
                self._GC_compabile -= 1
            if first_elem == 'G' and second_elem == 'G':
                self._GG_compabile -= 1
            if first_elem == 'G' and second_elem == 'T':
                self._GT_compabile -= 1
            
            if first_elem == 'T' and second_elem == 'A':
                self._TA_compabile -= 1
            if first_elem == 'T' and second_elem == 'C':
                self._TC_compabile -= 1
            if first_elem == 'T' and second_elem == 'G':
                self._TG_compabile -= 1
            if first_elem == 'T' and second_elem == 'T':
                self._TT_compabile -= 1
            
