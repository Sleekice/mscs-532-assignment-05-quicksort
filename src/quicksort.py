
"""
University of the Cumberlands
Course: MSCS 532 - Algorithms and Data Structures
Assignment 5: Quicksort Algorithm Implementation, Analysis, and Randomization

Student: Peter Nwochie Tiewah
Date: November 15, 2026
File: src/quicksort.py

Description:
    Deterministic Quicksort using the first element as the pivot.
    Demonstrates partitioning and recursive sorting.

Time Complexity:
    Best/Average: O(n log n)
    Worst:        O(n^2)

Space Complexity:
    Balanced partitions: O(n log n)
    Worst case:          O(n^2)

Note:
    Educational implementation using additional lists.
    Debugging output is disabled during benchmarking.
"""


def quicksort(numbers):
    """Return the values in ascending order without changing the input."""
    if len(numbers) <= 1:
        return numbers[:]

    pivot = numbers[0]
    smaller = []
    larger = []

    for number in numbers[1:]:
        if number <= pivot:
            smaller.append(number)
        else:
            larger.append(number)

    return quicksort(smaller) + [pivot] + quicksort(larger)


if __name__ == "__main__":
    numbers = [7, 2, 9, 4, 1]
    print("Original list:", numbers)
    print("Final result:", quicksort(numbers))