import unittest
from parameterized import parameterized
import src.sorting as sorting


class SortingUnitTest(unittest.TestCase):
    sorting_function_map = {
        "quick_sort": sorting.quick_sort,
        "merge_sort": sorting.merge_sort,
        "bubble_sort": sorting.bubble_sort
    }

    @parameterized.expand(list(sorting_function_map.keys()))
    def test_empty_list(self, algorithm_name):
        input_list = []
        output_list = self.sorting_function_map[algorithm_name](input_list)
        self.assertEqual(input_list, output_list)

    @parameterized.expand(list(sorting_function_map.keys()))
    def test_single_item(self, algorithm_name):
        input_list = [1]
        output_list = self.sorting_function_map[algorithm_name](input_list)
        self.assertEqual(input_list, output_list)

    @parameterized.expand(list(sorting_function_map.keys()))
    def test_two_items_sorted(self, algorithm_name):
        input_list = [1, 2]
        output_list = self.sorting_function_map[algorithm_name](input_list)
        self.assertEqual(input_list, output_list)

    @parameterized.expand(list(sorting_function_map.keys()))
    def test_two_items_unsorted(self, algorithm_name):
        input_list = [2, 1]
        output_list = self.sorting_function_map[algorithm_name](input_list)
        self.assertEqual(output_list, [1, 2])

    @parameterized.expand(list(sorting_function_map.keys()))
    def test_zero_in_list(self, algorithm_name):
        input_list = [10, 0]
        output_list = self.sorting_function_map[algorithm_name](input_list)
        self.assertEqual(output_list, [0, 10])

    @parameterized.expand(list(sorting_function_map.keys()))
    def test_odd_number_of_items(self, algorithm_name):
        input_list = [13, 7, 5]
        output_list = self.sorting_function_map[algorithm_name](input_list)
        self.assertEqual(output_list, [5, 7, 13])

    @parameterized.expand(list(sorting_function_map.keys()))
    def test_even_number_of_items(self, algorithm_name):
        input_list = [23, 7, 13, 5]
        output_list = self.sorting_function_map[algorithm_name](input_list)
        self.assertEqual(output_list, [5, 7, 13, 23])

    @parameterized.expand(list(sorting_function_map.keys()))
    def test_duplicate_integers_in_list(self, algorithm_name):
        input_list = [1, 2, 2, 1, 0, 0, 15, 15]
        output_list = self.sorting_function_map[algorithm_name](input_list)
        self.assertEqual(output_list, [0, 0, 1, 1, 2, 2, 15, 15])

    @parameterized.expand(list(sorting_function_map.keys()))
    def test_larger_integers(self, algorithm_name):
        input_list = [135604, 1000000, 45, 78435, 456219832, 2, 546]
        output_list = self.sorting_function_map[algorithm_name](input_list)
        self.assertEqual(output_list, [2, 45, 546, 78435, 135604, 1000000, 456219832])