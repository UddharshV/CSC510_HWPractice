"""
Module contains the unit test case for the merge_sort function.
"""
import unittest
from post_traces.hw2_debugging import merge_sort


class TestMergeSort(unittest.TestCase):
    """
    Test cases for merge_sort function for avg case.
    """

    def test_avg_case(self):
        """
        This module for merge sort use unsorted array as input.
        """
        self.assertEqual(merge_sort([4,5,2,3,1]), [1, 2, 3, 4, 5])
    def test_best_case(self):
        """
        This module for merge sort use unsorted array as input.
        """
        self.assertEqual(merge_sort([1,2,3,4,5]), [1, 2, 3, 4, 5])
    def test_worst_case(self):
        """
        This module for merge sort use unsorted array as input.
        """
        self.assertEqual(merge_sort([5,4,3,2,1]), [1, 2, 3, 4, 5])
if __name__ == '__main__':
    unittest.main()