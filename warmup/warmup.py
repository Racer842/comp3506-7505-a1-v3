"""
Skeleton for COMP3506/7505 A1, S2, 2024
The University of Queensland
Joel Mackenzie and Vladimir Morozov

WARMUP PROBLEMS

 Each problem will be assessed on three sets of tests:

1. "It works":
       Basic inputs and outputs, including the ones peovided as examples, with generous time and memory restrictions.
       Large inputs will not be tested here.
       The most straightforward approach will likely fit into these restrictions.

2. "Exhaustive":
       Extensive testing on a wide range of inputs and outputs with tight time and memory restrictions.
       These tests won't accept brute force solutions, you'll have to apply some algorithms and optimisations.

 3. "Welcome to COMP3506":
       Extensive testing with the tightest possible time and memory restrictions
       leaving no room for redundant operations.
       Every possible corner case will be assessed here as well.

There will be hidden tests in each category that will be published only after the assignment deadline.
"""

"""
You may wish to import your data structures to help you with some of the
problems. Or maybe not. We did it for you just in case.
"""
import math
import time
from structures.bit_vector import BitVector
from structures.dynamic_array import DynamicArray
from structures.linked_list import DoublyLinkedList, Node


def main_character(instring: list[int]) -> int:
    """
    @instring@ is an array of integers in the range [0, 2^{32}-1].
    Return the first position a repeat integer is encountered, or -1 if
    there are no repeated ints.

    Limitations:
        "It works":
            @instring@ may contain up to 10'000 elements.

        "Exhaustive":
            @instring@ may contain up to 300'000 elements.

        "Welcome to COMP3506":
            @instring@ may contain up to 5'000'000 elements.

    Examples:
    main_character([1, 2, 3, 4, 5]) == -1
    main_character([1, 2, 1, 4, 4, 4]) == 2
    main_character([7, 1, 2, 7]) == 3
    main_character([60000, 120000, 654321, 999, 1337, 133731337]) == -1
    """
    #Create Bit Vector
    # set it to the size using custom function
    storage_vector = BitVector()
    storage_vector.main_character_bit_vector()

    index = 0
    for elem in instring:
        if storage_vector.get_at(elem) == 0:
            storage_vector.set_at(elem)
        else:
            return index
        index += 1

    return -1

def missing_odds(inputs: list[int]) -> int:
    """
    @inputs@ is an unordered array of distinct integers.
    If @a@ is the smallest number in the array and @b@ is the biggest,
    return the sum of odd numbers in the interval [a, b] that are not present in @inputs@.
    If there are no such numbers, return 0.

    Limitations:
        "It works":
            @inputs@ may contain up to 10'000 elements.
            Each element is in range 0 <= inputs[i] <= 10^4
        "Exhaustive":
            @inputs@ may contain up to 300'000 elements.
            Each element is in range 0 <= inputs[i] <= 10^6
        "Welcome to COMP3506":
            @inputs@ may contain up to 5'000'000 elements.
            Each element is in range 0 <= inputs[i] <= 10^16

    Examples:
    missing_odds([1, 2]) == 0
    missing_odds([1, 3]) == 0
    missing_odds([1, 4]) == 3
    missing_odds([4, 1]) == 3
    missing_odds([4, 1, 8, 5]) == 10    # 3 and 7 are missing
    """

    # YOUR CODE GOES HERE
    total_sum = 0
    upper_odd = 0
    lower_odd = 0
    upper_bound = 0
    lower_bound = 0
    odd_present_sum = 0
    first_element_flag = 0

    # Find upper and lower bound
    for elem in inputs:
        if first_element_flag == 0:
            lower_bound = elem
            upper_bound = elem
            first_element_flag = 1
        if elem < lower_bound:
            lower_bound = elem
        if elem > upper_bound:
            upper_bound = elem
        if elem % 2 == 1:
            odd_present_sum += elem
    
    # Find the lower and upper bound odd number
    if lower_bound % 2 == 0:
        lower_odd = lower_bound + 1
    else:
        lower_odd = lower_bound
    
    if upper_bound % 2 == 0:
        upper_odd = upper_bound - 1
    else:
        upper_odd = upper_bound
    
    total_sum = ((upper_odd - lower_odd + 2)*(lower_odd + upper_odd)) // 4

    total_sum = total_sum - odd_present_sum

    return total_sum

def k_cool(k: int, n: int) -> int:
    """
    Return the n-th largest k-cool number for the given @n@ and @k@.
    The result can be large, so return the remainder of division of the result
    by 10^16 + 61 (this constant is provided).

    Limitations:
        "It works":
            2 <= k <= 128
            1 <= n <= 10000
        "Exhaustive":
            2 <= k <= 10^16
            1 <= n <= 10^100     (yes, that's ten to the power of one hundred)
        "Welcome to COMP3506":
            2 <= k <= 10^42
            1 <= n <= 10^100000  (yes, that's ten to the power of one hundred thousand)

    Examples:
    k_cool(2, 1) == 1                     # The first 2-cool number is 2^0 = 1
    k_cool(2, 3) == 2                     # The third 2-cool number is 2^1 + 2^0 = 3
    k_cool(3, 5) == 10                    # The fifth 3-cool number is 3^2 + 3^0 = 10
    k_cool(10, 42) == 101010
    k_cool(128, 5000) == 9826529652304384 # The actual result is larger than 10^16 + 61,
                                          # so k_cool returns the remainder of division by 10^16 + 61
    """

    MODULUS = 10**16 + 61

    answer = 0

    # This starts it at k^0
    k_to_the_power = 0

    while n > 0:
        if n & 1:
            answer = (answer + pow(k, k_to_the_power, MODULUS)) % MODULUS
        k_to_the_power = (k_to_the_power + 1) % MODULUS
        n >>= 1

    return answer 


def number_game(numbers: list[int]) -> tuple[str, int]:
    """
    @numbers@ is an unordered array of integers. The array is guaranteed to be of even length.
    Return a tuple consisting of the winner's name and the winner's score assuming that both play optimally.
    "Optimally" means that each player makes moves that maximise their chance of winning
    and minimise opponent's chance of winning.
    You are ALLOWED to use a tuple in your return here, like: return (x, y)
    Possible string values are "Alice", "Bob", and "Tie"

    Limitations:
        "It works":
            @numbers@ may contain up to 10'000 elements.
            Each element is in range 0 <= numbers[i] <= 10^6
        "Exhaustive":
            @numbers@ may contain up to 100'000 elements.
            Each element is in range 0 <= numbers[i] <= 10^16
        "Welcome to COMP3506":
            @numbers@ may contain up to 300'000 elements.
            Each element is in range 0 <= numbers[i] <= 10^16

    Examples:
    number_game([5, 2, 7, 3]) == ("Bob", 5)
    number_game([3, 2, 1, 0]) == ("Tie", 0)
    number_game([2, 2, 2, 2]) == ("Alice", 4)

    For the second example, if Alice picks 2 to increase her score, Bob will pick 3 and win. Alice does not want that.
    The same happens if she picks 1 or 0, but this time she won't even increase her score.
    The only scenario when Bob does not win immediately is if Alice picks 3.
    Then, Bob faces the same choice:
    pick 1 to increase his score knowing that Alice will pick 2 and win, or pick 2 himself.
    The same happens on the next move.
    So, nobody picks any numbers to increase their score, which results in a Tie with both players having scores of 0.
    """
    # YOUR CODE GOES HERE
    Alice_score = 0
    Bob_score = 0
    turn_tracker = 0
    size = 0

    game_array = DynamicArray()

    size = len(numbers)

    # start_time_1 = time.time()
    game_array.store_existing_array(numbers, size)

    game_array.sort()

    game_array.reverse()

    for elem in game_array:
        
        if elem is None:
            break
        
        if turn_tracker == 0:
            if elem & 1 == 0:
                Alice_score += elem
            turn_tracker = 1
        else:
            if elem & 1 == 1:
                Bob_score += elem
            turn_tracker = 0

    if Bob_score > Alice_score:
      winner = "Bob"
      winning_score = Bob_score
    elif Alice_score > Bob_score:
      winner = "Alice"
      winning_score = Alice_score
    else:
      winner = "Tie"
      winning_score = Bob_score
    
    return winner, winning_score


def road_illumination(road_length: int, poles: list[int]) -> float:
    """
    @poles@ is an unordered array of integers.
    Return a single floating point number representing the smallest possible radius of illumination
    required to illuminate the whole road.
    Floating point numbers have limited precision. Your answer will be accepted
    if the relative or absolute error does not exceed 10^(-6),
    i.e. |your_ans - true_ans| <= 0.000001 OR |your_ans - true_ans|/true_ans <= 0.000001

    Limitations:
        "It works":
            @poles@ may contain up to 10'000 elements.
            0 <= @road_length@ <= 10^6
            Each element is in range 0 <= poles[i] <= 10^6
        "Exhaustive":
            @poles@ may contain up to 100'000 elements.
            0 <= @road_length@ <= 10^16
            Each element is in range 0 <= poles[i] <= 10^16
        "Welcome to COMP3506":
            @poles@ may contain up to 300'000 elements.
            0 <= @road_length@ <= 10^16
            Each element is in range 0 <= poles[i] <= 10^16

    Examples:
    road_illumination(15, [15, 5, 3, 7, 9, 14, 0]) == 2.5
    road_illumination(5, [2, 5]) == 2.0
    """

    # YOUR CODE GOES HERE
    road_array = DynamicArray()
    difference = 0
    size = 0
    
    # for elem in poles:
    #   size += 1

    size = len(poles)
    
    road_array.store_existing_array(poles, size)

    road_array.sort()
    
    for i in range(0, size - 1):
      temp_diff = road_array[i + 1] - road_array[i]
      if temp_diff > difference:
          difference = temp_diff

    # for i in range(1, size):
    #     max_gap = max(max_gap, poles[i] - poles[i - 1])
    
    radius = difference / 2
    if road_array[0] > radius:
      radius = road_array[0]
    if (road_length - road_array[size - 1]) > radius:
      radius = road_length - road_array[size - 1]
    
    return radius
