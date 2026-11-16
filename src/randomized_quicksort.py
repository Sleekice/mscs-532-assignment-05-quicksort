
"""
University of the Cumberlands
Course: MSCS 532 - Algorithms and Data Structures
Assignment 5: Quicksort Algorithm Implementation, Analysis, and Randomization

Student: Peter Nwochie Tiewah
Date: November 15, 2026
File: src/randomized_quicksort.py

Description:
    Randomized Quicksort using a randomly selected pivot.
    Demonstrates partitioning and recursive sorting.

Time Complexity:
    Expected: O(n log n)
    Worst:    O(n^2)

Space Complexity:
    Expected:   O(n log n)
    Worst case: O(n^2)

Note:
    Educational implementation using additional lists.
    Debugging output is disabled during benchmarking.
"""

import random


def randomized_quicksort(numbers):
    """Return the values in ascending order using random pivot selection."""
    if len(numbers) <= 1:
        return numbers[:]

    pivot_index = random.randrange(len(numbers))
    pivot = numbers[pivot_index]
    smaller = []
    larger = []

    for index, number in enumerate(numbers):
        if index == pivot_index:
            continue

        if number <= pivot:
            smaller.append(number)
        else:
            larger.append(number)

    return randomized_quicksort(smaller) + [pivot] + randomized_quicksort(larger)


if __name__ == "__main__":
    numbers = [7, 2, 9, 4, 1]
    print("Original list:", numbers)
    print("Final result:", randomized_quicksort(numbers))
