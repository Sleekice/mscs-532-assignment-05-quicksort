
"""
University of the Cumberlands
MSCS 532 - Algorithms and Data Structures
Assignment 5: Quicksort Testing

Student: Peter Nwochie Tiewah
Date: November 15, 2026
"""

import unittest

from src.quicksort import quicksort
from src.randomized_quicksort import randomized_quicksort


class TestQuicksort(unittest.TestCase):

    def test_both_algorithms(self):
        test_cases = [
            [],
            [5],
            [7, 2, 9, 4, 1],
            [1, 2, 3, 4, 5],
            [5, 4, 3, 2, 1],
            [5, 3, 5, 2, 3],
            [-3, 0, 7, -1, 4],
        ]

        for algorithm in (quicksort, randomized_quicksort):
            for numbers in test_cases:
                with self.subTest(
                    algorithm=algorithm.__name__,
                    numbers=numbers
                ):
                    original = numbers.copy()
                    result = algorithm(numbers)

                    self.assertEqual(result, sorted(numbers))
                    self.assertEqual(numbers, original)


if __name__ == "__main__":
    unittest.main()
