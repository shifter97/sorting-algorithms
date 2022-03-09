def bubble_sort(list):
    """ 
        Sort the list by using bubble sort algorithm, 
        iterating throw list and repeatedly swapping 
        the adjacent elements if they are in wrong order
    """
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


def merge_sort(list):
    """ 
        Sort the list by using merge sort algorithm,
        Divide the unsorted list into n sublists, 
        each containing one element (a list of one element is considered sorted).
        Repeatedly merges sublists to produce new sorted sublists
        until there is only one sublist remaining. This will be the sorted list.
    """

    if len(list) > 1:
        mid = len(list) // 2
        left = list[:mid]
        right = list[mid:]
        
        merge_sort(left)
        merge_sort(right)

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


def quick_sort(list):
    """ 
        Sort the list by using quicksort algorithm,
        in the current implementation pivot is in the middle,
        comparing elements before pivot and after pivot and swapping places,
        used recursion for left and right side of list sorting.
    """
    def _partition(list, left, right):   
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

    def _quick_sort(list, left, right):
        if left < right:
            split_index = _partition(list, left, right)
            _quick_sort(list, left, split_index)
            _quick_sort(list, split_index + 1, right)

    _quick_sort(list, 0, len(list) - 1)

    return list