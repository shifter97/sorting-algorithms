import unittest


# BUBBLE SORT
def bubble_sort(mylist):
    for a in range(len(mylist)):
        swap = False
        i = 0
        while i < len(mylist)-1:
            if mylist[i] > mylist[i+1]:
                mylist[i], mylist[i + 1] = mylist[i + 1], mylist[i]
                swap = True
            i += 1
        if swap is False:
            break
    return mylist

# MERGE SORT
def mergeSort(mylist):
    if len(mylist) > 1:
        mid = len(mylist) // 2
        left = mylist[:mid]
        right = mylist[mid:]
        mergeSort(left)
        mergeSort(right)

        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                mylist[k] = left[i]
                i += 1
            else:
                mylist[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            mylist[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            mylist[k] = right[j]
            j += 1
            k += 1

    return mylist

mylist = [26, 10, 11, 9, 30, 1, 9]
new = mergeSort(mylist)
mergeSort(mylist)


# QUICK SORT
def partition(nums, low, high):
    pivot = nums[(low + high) // 2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while nums[i] < pivot:
            i += 1
        j -= 1
        while nums[j] > pivot:
            j -= 1
        if i >= j:
            return j
        nums[i], nums[j] = nums[j], nums[i]


def quick_sort(mylist):
    def _quick_sort(items, low, high):
        if low < high:
            split_index = partition(items, low, high)
            _quick_sort(items, low, split_index)
            _quick_sort(items, split_index + 1, high)

    _quick_sort(mylist, 0, len(mylist) - 1)
    return mylist


mylist = [26, 10, 11, 9, 30, 1, 12]
new1 = quick_sort(mylist)
print(mylist)


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
