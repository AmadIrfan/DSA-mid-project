

def InsertionSortdscendingOrder(array):
    for i in range(0, len(array)):
        key = array[i]
        j = i-1
        while key < array[j] and j >= 0:
            array[j+1] = array[j]
            j = j-1
        array[j+1] = key
    return array


def BubbleSort(array, start, end):
    for i in range(int(start)+1, int(end)+1):
        Sorted = False
        while i > int(start) and (not Sorted):
            Sorted = True
            for j in range(int(start), i):
                if array[j-1] > array[j]:
                    temp = array[j-1]
                    array[j-1] = array[j]
                    array[j] = temp
                    Sorted = False
    return array


def SelectionSort(array, start, end):

    for ind in range(int(start), int(end)):
        min_index = ind

        for j in range(ind + 1, int(end)):
            # select the minimum element in every iteration
            if array[j] < array[min_index]:
                min_index = j

        # swapping the elements to sort the array
        (array[ind], array[min_index]) = (array[min_index], array[ind])
    return array


def Merge(array, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    L = [0] * (n1)
    R = [0] * (n2)
    for i in range(0, n1):
        L[i] = array[p + i]
    for j in range(0, n2):
        R[j] = array[q + 1 + j]
    i = 0
    j = 0
    k = p
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            array[k] = L[i]
            i += 1
        else:
            array[k] = R[j]
            j += 1
        k += 1
    while i < n1:
        array[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        array[k] = R[j]
        j += 1
        k += 1


def MergeSort(array, start, end):
    if start < end:

        middle = start+(end-start)//2
        MergeSort(array, start, middle)
        MergeSort(array, middle+1, end)
        Merge(array, start, middle, end)

    return array


def HybridSort(array, start, end):
    if start < end:
        middle = start+(end-start)//2
        HybridSort(array, start, middle)
        HybridSort(array, middle+1, end)
        Merge(array, start, middle, end)
    else:
        print('ass')
        # InsertionSort(array, start, end)
    return array


def partition(array, low, high):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:

            i = i + 1
            (array[i], array[j]) = (array[j], array[i])
    (array[i + 1], array[high]) = (array[high], array[i + 1])
    return i + 1


def quickSort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quickSort(array, low, pi - 1)
        quickSort(array, pi + 1, high)
