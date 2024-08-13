"""
Skeleton for COMP3506/7505 A1, S2, 2024
The University of Queensland
Joel Mackenzie and Vladimir Morozov

NOTE: This file is not used for assessment. It is just a driver program for
you to write your own test cases and execute them against your data structures.
"""

# Import helper libraries
import random
import sys
import time
import argparse

# Import our data structures
from structures.linked_list import Node, DoublyLinkedList
from structures.dynamic_array import DynamicArray 
from structures.bit_vector import BitVector

def test_linked_list():
    """
    A simple set of tests for the linked list implementation.
    This is not marked and is just here for you to test your code.
    """
    print ("==== Executing Linked List Tests ====")

    # Consider expanding these tests into your own methods instead of
    # just doing a bunch of stuff here - this is just to get you started
    
    # OK, let's add some strings to a list
    # my_list = DoublyLinkedList()
    # assert(my_list.get_size() == 0)
    # my_list.insert_to_back("hello")
    # my_list.insert_to_front(432)
    # print(my_list.get_size())
    # print(my_list.get_head())
    # print(str(my_list))
    # my_list.find_and_remove_element(432)
    # print(str(my_list))

    test_list = [random.randint(0, 1234) for i in range(50000)]
    my_list = DoublyLinkedList()
    print(my_list.get_head())
    #print(my_list.set_head(12))
    #print(my_list.get_head())
    for item in test_list:
        my_list.insert_to_back(item)
    
    print(my_list.get_size())
    print(my_list.get_head())
    print(my_list.get_tail())
    my_list.set_head(12)
    print(my_list.get_head())
    if my_list.find_element(2):
        print("Yes")
    if my_list.find_and_remove_element(55):
        print("Craxy")
    
    if my_list.find_and_remove_element(22):
        print("Craxy")
    
    print(my_list.get_size())
    my_list.reverse()
    print(my_list.get_size())
    print(my_list.get_head())
    print(my_list.get_tail())

    # my_list.reverse()

    # flag = my_list.find_element("Dog")
    # if flag is True:
    #     print("Found Element")
    # else:
    #     print("Did Not find it")
    
    # flag = my_list.find_element("9090")
    # if flag is True:
    #     print("Found Element")
    # else:
    #     print("Did Not find it")
    
    # print(my_list.get_head())
    # print(my_list.get_tail())

    # my_list.remove_from_front()
    # print(str(my_list))

    # my_list.remove_from_back()
    # print(str(my_list))

    # print(my_list.get_head())
    # print(my_list.get_tail())

    # flag = my_list.find_and_remove_element("3100")
    # if flag is True:
    #     print("Found Element")
    # else:
    #     print("Did Not find it")
    # print(str(my_list))
    # print(my_list.get_tail())
    # print(my_list.get_size())

def test_dynamic_array():
    """
    A simple set of tests for the dynamic array implementation.
    This is not marked and is just here for you to test your code.
    """
    print ("==== Executing Dynamic Array Tests ====")
    my_list = DynamicArray()
    my_list.append(1)
    my_list.append(3)
    my_list.append(4)
    my_list.append(6)
    my_list.append(8)
    print(str(my_list))
    print(my_list.get_at(5))
    print(str(my_list))
    # my_list.prepend(7)
    # print(my_list.get_at(0))
    # my_list.prepend(6)
    # print(str(my_list))
    # my_list.set_at(7, 9)
    # print(str(my_list))
    # print(my_list.get_at(7))
    # my_list.prepend(99)
    # print(str(my_list))
    # if my_list.is_full():
    #     print("Monkey")
    # my_list.remove(3)
    # print(str(my_list))
    my_list.append(3)
    my_list.append(12)
    my_list.prepend(59)
    my_list.prepend(68283)
    my_list.prepend(9122344)
    my_list.append(103)
    my_list.append(397)
    my_list.append(4037)
    my_list.append(90000010101)

    print(str(my_list))
    # my_list.set_at(1, 7)
    # print(str(my_list))
    # my_list.set_at(17, 1)
    # print(str(my_list))


def test_bitvector():
    """
    A simple set of tests for the bit vector implementation.
    This is not marked and is just here for you to test your code.
    """
    print ("==== Executing Bit Vector Tests ====")



# The actual program we're running here
if __name__ == "__main__":
    # Get and parse the command line arguments
    parser = argparse.ArgumentParser(description="COMP3506/7505 Assignment One: Testing Data Structures")

    parser.add_argument("--linkedlist", action="store_true", help="Test your linked list.")
    parser.add_argument("--dynamicarray", action="store_true", help="Test your dynamic array.")
    parser.add_argument("--bitvector", action="store_true", help="Test your bit vector.")
    parser.add_argument("--seed", type=int, default='42', help="Seed the PRNG.")
    
    args = parser.parse_args()

    # No arguments passed
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(-1)

    # Seed the PRNG in case you are using randomness
    random.seed(args.seed)

    # Now check/run the selected algorithm
    if args.linkedlist:
        test_linked_list()

    if args.dynamicarray:
        test_dynamic_array()

    if args.bitvector:
        test_bitvector()

