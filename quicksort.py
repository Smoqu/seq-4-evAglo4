def partition(array, low, high):
    pivot = array[high]
    i = low
    for j in range(low, high):
        if array[j] < pivot:
            array[i], array[j] = array[j], array[i]
            i += 1
    array[i], array[high] = array[high], array[i]

    return i

def quicksort(array, low, high):
    if low < high:
        p = partition(array, low, high)
        quicksort(array, low, p - 1)
        quicksort(array, p + 1, high)

    return array