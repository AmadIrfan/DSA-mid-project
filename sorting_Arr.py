
import pandas as pd
# from DL import dataList
from BL import *


def insertionSort(array, method):
    if method == "Ascending":
        for i in range(len(array)):
            key = array[i]
            j = i-1
            while j >= 0 and key < array[j]:
                array[j+1] = array[j]
                j = j-1
            array[j+1] = key
        # return array
    if method == "Descending":
        for i in range(0, (len(array))):
            key = array[i]
            j = i-1
            while j >= 0 and key > array[j]:
                array[j+1] = array[j]
                j = j-1
            array[j+1] = key
        # return array
    print(array)


def SelectionSort(array, method):
    if method == "Ascending":
        for i in range(0, len(array)):
            for j in range(0, len(array)-i-1):
                if (array[j] > array[j+1]):
                    temp = array[j]
                    array[j] = array[j+1]
                    array[j+1] = temp
        return array
    if method == "Descending":
        for i in range(0, len(array)):
            for j in range(0, len(array)-i-1):
                if (array[j] < array[j+1]):
                    temp = array[j]
                    array[j] = array[j+1]
                    array[j+1] = temp
        return array


def partition(array, low, high, method):
    if method == "Ascending":
        pivot = array[high]
        i = low - 1
        for j in range(low, high):
            if array[j] <= pivot:
                i = i + 1
                (array[i], array[j]) = (array[j], array[i])
        (array[i + 1], array[high]) = (array[high], array[i + 1])
        return i + 1
    if method == "Descending":
        pivot = array[high]
        i = low - 1
        for j in range(low, high):
            if array[j] >= pivot:
                i = i + 1
                (array[i], array[j]) = (array[j], array[i])
        (array[i + 1], array[high]) = (array[high], array[i + 1])
        return i + 1


def quickSort(array, low, high, method):
    if low < high:
        pivot = partition(array, low, high, method)
        quickSort(array, low, pivot - 1, method)
        quickSort(array, pivot + 1, high, method)
    return array


def BubbleSort(array, method):
    j = len(array)
    if method == "Ascending":
        sorted1 = False
        while ((j > 1) and (not (sorted1))):
            sorted1 = True
            for i in range(0, len(array)):
                if (array[i-1] > array[i]):
                    temp = array[i-1]
                    array[i-1] = array[i]
                    array[i] = temp
                    sorted1 = False
        return array
    if method == "Descending":
        sorted1 = False
        while ((j > 1) and (not (sorted1))):
            sorted1 = True
            for i in range(0, len(array)):
                if (array[i-1] > array[i]):
                    temp = array[i-1]
                    array[i-1] = array[i]
                    array[i] = temp
                    sorted1 = False
        return array

# def BubbleSort(Arr, method):
#     if method == "Ascending":
#         for i in range(0, len(Arr)):
#             j = i+1
#             for j in range(0, len(Arr)):
#                 if (Arr[i] < Arr[j]):
#                     Temp_Val = Arr[i]
#                     Arr[i] = Arr[j]
#                     Arr[j] = Temp_Val
#                     temp = dataList[i]
#                     dataList[i] = dataList[j]
#                     dataList[j] = temp
#         return Arr
#     if method == "Descending":
#         for i in range(0, len(Arr)):
#             j = i+1
#             for j in range(0, len(Arr)):
#                 if (Arr[i] > Arr[j]):
#                     Temp_Val = Arr[i]
#                     Arr[i] = Arr[j]
#                     Arr[j] = Temp_Val
#                     temp = dataList[i]
#                     dataList[i] = dataList[j]
#                     dataList[j] = temp
#         return Arr


# def Merge(Array, p, q, r):
#     n1 = q-p+1
#     n2 = r-q
#     Left = []
#     Right = []

#     for i in range(n1+1):
#         Left.append(Array[p+i-1])

#     for j in range(n2+1):
#         Right.append(Array[q+j])

#     Left.append(100000000)
#     Right.append(100000000)

#     i = 1
#     j = 1

#     for k in range(p, r+1):
#         if (Left[i] < Right[j]):
#             Array[k] = Left[i]
#             i = i+1
#         else:
#             Array[k] = Right[j]
#             j = j+1
#     return Array


# def MergeSort(array, method):
#     start = 0
#     end = len(array)
#     if (start < end):
#         q = int((start+end)/2)
#         MergeSort(array, method)
#         MergeSort(array, method)
#         Merge(array, start, q, end)


# def HybridMergeSort(array, start, end):
#     if (start < end):
#         q = int((start+end)/2)
#         MergeSort(array, start, q)
#         MergeSort(array, q+1, end)
#         Merge(array, start, q, end)
    # else:
    # InsertionSort(array,method)


# pf = pd.read_csv("scrap.csv")
# id = pf["id"].values.tolist()
# id=[89,23,5,1,53,2,43,23,64,87,23,12,1,5,8,]
# id = ['as', 'ab', 'ac', 'az', 'aa', 'ar']
# print(quickSort(id, 0, len(id)-1,'Ascending'))
# print(BubbleSort(id, 'Descending'))
# insertionSort(id, 'Ascending')
# print(SelectionSort(id, 'Ascending'))
# print(MergeSort(id, 'Ascending'))
