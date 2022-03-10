def bubble_sort(numbers_list):
    """ 
        Sort the list by using bubble sort algorithm, 
        iterating throw list and repeatedly swapping 
        the adjacent elements if they are in wrong order
    """
    for a in range(len(numbers_list)):
        swap = False
        i = 0
        while i < len(numbers_list)-1:
            if numbers_list[i] > numbers_list[i+1]:
                numbers_list[i], numbers_list[i + 1] = numbers_list[i + 1], numbers_list[i]
                swap = True
            i += 1
        if swap is False:
            break
    return numbers_list


def merge_sort(numbers_list):
    """ 
        Sort the list by using merge sort algorithm,
        Divide the unsorted list into n sublists, 
        each containing one element (a list of one element is considered sorted).
        Repeatedly merges sublists to produce new sorted sublists
        until there is only one sublist remaining. This will be the sorted list.
    """
    
    if len(numbers_list) > 1:
        mid = len(numbers_list) // 2
        left = numbers_list[:mid]
        right = numbers_list[mid:]
        
        merge_sort(left)
        merge_sort(right)

        i, j, k = 0, 0, 0 

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                numbers_list[k] = left[i]
                i += 1
            else:
                numbers_list[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            numbers_list[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            numbers_list[k] = right[j]
            j += 1
            k += 1

    return numbers_list


def quick_sort(numbers_list):
    """ 
        Sort the list by using quicksort algorithm,
        in the current implementation pivot is in the middle,
        comparing elements before pivot and after pivot and swapping places,
        used recursion for left and right side of list sorting.
    """
    
    def _partition(numbers_list, left, right):
        # Choosing pivot in the middle
        pivot = numbers_list[(left + right) // 2]
        i = left - 1
        j = right + 1
        while True:
            i += 1

            while numbers_list[i] < pivot:
                i += 1

            j -= 1
            while numbers_list[j] > pivot:
                j -= 1
            if i >= j:
                return j
            
            numbers_list[i], numbers_list[j] = numbers_list[j], numbers_list[i]

    def _quick_sort(numbers_list, left, right):
        if left < right:
            split_index = _partition(numbers_list, left, right)
            _quick_sort(numbers_list, left, split_index)
            _quick_sort(numbers_list, split_index + 1, right)

    _quick_sort(numbers_list, 0, len(numbers_list) - 1)

    return numbers_list