import unittest


# BUBBLE SORT
def bubble_sort(list):
    for a in range(len(list)):
        swap = False
        i = 0
        while i < len(list)-1:
            if list[i] > list[i+1]:
                list[i], list[i + 1] = list[i + 1], list[i]
                swap = True
            i += 1
        if swap is False:
            break
    return list

mylist = [26, 10, 11, 9, 30, 1, 9]
new2 = bubble_sort(mylist)


# MERGE SORT
def mergeSort(list):
    if len(list) > 1:
        mid = len(list) // 2
        left = list[:mid]
        right = list[mid:]
        mergeSort(left)
        mergeSort(right)

        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                list[k] = left[i]
                i += 1
            else:
                list[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            list[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            list[k] = right[j]
            j += 1
            k += 1

    return list

mylist = [26, 10, 11, 9, 30, 1, 9]
new = mergeSort(mylist)


# QUICK SORT
def partition(list, left, right):
    pivot = list[(left + right) // 2]
    i = left - 1
    j = right + 1
    while True:
        i += 1
        while list[i] < pivot:
            i += 1
        j -= 1
        while list[j] > pivot:
            j -= 1
        if i >= j:
            return j
        list[i], list[j] = list[j], list[i]


def quick_sort(list):
    def _quick_sort(list, left, right):
        if left < right:
            split_index = partition(list, left, right)
            _quick_sort(list, left, split_index)
            _quick_sort(list, split_index + 1, right)

    _quick_sort(list, 0, len(list) - 1)
    return list


mylist = [26, 10, 11, 9, 30, 1, 12]
new1 = quick_sort(mylist)


class unit_tests(unittest.TestCase):
    def test_empty_list(self):
        lst = []
        sorted_lst_1 = quick_sort(lst)
        sorted_lst_2 = mergeSort(lst)
        self.assertEqual(lst, sorted_lst_1)

    def test_single_item(self):
        lst = [1]
        sorted_lst = quick_sort(lst)
        self.assertEqual(lst, sorted_lst)

    def test_two_items_sorted(self):
        lst = [1, 2]
        sorted_lst = quick_sort(lst)
        self.assertEqual(lst, sorted_lst)

    def test_two_items_unsorted(self):
        lst = [2, 1]
        sorted_lst = quick_sort(lst)
        self.assertEqual(sorted_lst, [1, 2])

    def test_zero_in_list(self):
        lst = [10, 0]
        sorted_lst = quick_sort(lst)
        self.assertEqual(sorted_lst, [0, 10])

    def test_odd_number_of_items(self):
        lst = [13, 7, 5]
        sorted_lst = quick_sort(lst)
        self.assertEqual(sorted_lst, [5, 7, 13])

    def test_even_number_of_items(self):
        lst = [23, 7, 13, 5]
        sorted_lst = quick_sort(lst)
        self.assertEqual(sorted_lst, [5, 7, 13, 23])

    def test_duplicate_integers_in_list(self):
        lst = [1, 2, 2, 1, 0, 0, 15, 15]
        sorted_lst = quick_sort(lst)
        self.assertEqual(sorted_lst, [0, 0, 1, 1, 2, 2, 15, 15])

    def test_larger_integers(self):
        lst = [135604, 1000000, 45, 78435, 456219832, 2, 546]
        sorted_lst = quick_sort(lst)
        self.assertEqual(sorted_lst, [2, 45, 546, 78435, 135604, 1000000, 456219832])

if __name__ == '__main__':
    unittest.main()
