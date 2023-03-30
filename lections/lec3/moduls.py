def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)



def merge_sort(list1):
    if len(list1) > 1:
        mid = len(list1) // 2
        left = list1[mid:]
        right = list1[:mid]
