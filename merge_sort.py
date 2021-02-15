def merge(left, right):
    result = []

    while len(left) != 0 and len(right) != 0:
        if left[0] <= right[0]:
            result.append(left[0])
            left = left[1:]
        else:
            result.append(right[0])
            right = right[1:]

    while len(left) != 0:
        result.append(left[0])
        left = left[1:]
    
    while len(right) != 0:
        result.append(right[0])
        right = right[1:]

    return result


def merge_sort(array):
    if len(array) <= 1:
        return array

    left = []
    right = []

    for x in range(len(array)):
        if x < len(array) / 2:
            left.append(array[x])
        else:
            right.append(array[x])

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


