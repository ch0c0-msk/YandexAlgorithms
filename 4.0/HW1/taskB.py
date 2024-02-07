# Task condition: https://contest.yandex.ru/contest/53029/problems/

import sys, random

def quickSort(list, low, high):

    if (high - low + 1 <= 10):
        insertionSort(list, low, high)
        return
    
    elif (low < high):
        pivot_low, pivot_high = partition(list, low, high)
        quickSort(list, low, pivot_low - 1)
        quickSort(list, pivot_high, high)

def insertionSort(list, low, high):
    for i in range(low + 1, high + 1):
        temp = list[i]
        j = i - 1
        while (j >= 0 and temp < list[j]):
            list[j+1] = list[j]
            j = j - 1
        list[j+1] = temp

def partition(list, l, r):

    pivotValue = list[random.randint(l, r)]
    
    n, e, g = l, l, l
    while n < len(list):
        if list[n] < pivotValue:
            temp = list[n]
            list[n] = list[g]
            list[g] = list[e]
            list[e] = temp
            e += 1
            g += 1
            n += 1
        elif list[n] == pivotValue:
            temp = list[n]
            list[n] = list[g]
            list[g] = temp
            g += 1
            n += 1
        else:
            n += 1
    return e, g

def main():
    n = int(input())
    sourceList = [int(i) for i in sys.stdin.readline().rstrip().split()]
    sourceList.sort()
    for elem in sourceList:
        print(elem, end=" ")

if __name__ == "__main__":
    main() 