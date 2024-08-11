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

from warmup.warmup import * 

def test_main_character():
    """
    A simple set of tests for the main character problem.
    This is not marked and is just here for you to test your code.
    """
    assert (main_character([1,2,3,4,5]) == -1)
 

def test_missing_odds():
    """
    A simple set of tests for the missing odds problem.
    This is not marked and is just here for you to test your code.
    """
    test = missing_odds([1, 2])
    print(test)
    test = missing_odds([1, 3])
    print(test)
    # missing_odds([1, 4]) 
    # missing_odds([4, 1])
    test = missing_odds([4, 1, 8, 5])
    print(test) 

def test_k_cool():
    """
    A simple set of tests for the k cool problem.
    This is not marked and is just here for you to test your code.
    """
    test = k_cool(2, 1)  
    print(test)                   # The first 2-cool number is 2^0 = 1
    test = k_cool(2, 3)
    print(test)                     # The third 2-cool number is 2^1 + 2^0 = 3
    test = k_cool(3, 5)
    print(test)                   # The fifth 3-cool number is 3^2 + 3^0 = 10
    test = k_cool(10, 42)
    print(test)
    test = k_cool(128, 5000)
    print(test)
    test = k_cool(7, 8)
    print(test)
    test = k_cool(10**42, 10**100000)
    print("heelp")
    print(test)


def test_number_game():
    """
    A simple set of tests for the number game problem.
    This is not marked and is just here for you to test your code.
    """

def test_road_illumination():
    """
    A simple set of tests for the road illumination problem.
    This is not marked and is just here for you to test your code.
    """

# The actual program we're running here
if __name__ == "__main__":
    # Get and parse the command line arguments
    parser = argparse.ArgumentParser(description="COMP3506/7505 Assignment One: Testing Warmup Problems")

    parser.add_argument("--character", action="store_true", help="Test your main character sol.")
    parser.add_argument("--odds", action="store_true", help="Test your missing odds sol.")
    parser.add_argument("--kcool", action="store_true", help="Test your k-cool sol.")
    parser.add_argument("--numbergame", action="store_true", help="Test your number game sol.")
    parser.add_argument("--road", action="store_true", help="Test your road illumination sol.")
    parser.add_argument("--seed", type=int, default='42', help="Seed the PRNG.")
    args = parser.parse_args()

    # No arguments passed
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(-1)

    # Seed the PRNG in case you are using randomness
    random.seed(args.seed)

    # Now check/run the selected algorithm
    if args.character:
        test_main_character()

    if args.odds:
        test_missing_odds()

    if args.kcool:
        test_k_cool()

    if args.numbergame:
        test_number_game()

    if args.road:
        test_road_illumination()

