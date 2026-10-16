def quick_sort(array):
    if len(array) <= 1:
        return array[:]
   
    pivot = array[0]
    left = []
    mid = []
    right = []
    for n in array:
        if n < pivot:
            left.append(n)
        elif n > pivot:
            right.append(n)
        else:
            mid.append(n)

    return quick_sort(left) + mid + quick_sort(right)

quick_sort([87, 11, 23, 18, 18, 23, 11, 56, 87, 56])