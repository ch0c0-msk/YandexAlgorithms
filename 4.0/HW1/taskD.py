# Task condition: https://contest.yandex.ru/contest/53029/problems/D/

def merge(list):
    if len(list) == 1:
        return list
    leftList = merge(list[:(len(list) // 2)])
    rightList = merge(list[(len(list)//2):])
    res = [0] * (len(leftList) + len(rightList))
    index1, index2, i = 0, 0, 0
    while index1 < len(leftList) and index2 < len(rightList):
        if leftList[index1] < rightList[index2]:
            res[i] = leftList[index1]
            index1 += 1
            i += 1
        else:
            res[i] = rightList[index2]
            index2 += 1
            i += 1
    while index1 < len(leftList):
        res[i] = leftList[index1]
        index1 += 1
        i += 1
    while index2 < len(rightList):
        res[i] = rightList[index2]
        index2 += 1
        i += 1
    return res

def main():
    n = int(input())
    if n > 0:
        list = [int(i) for i in input().split()]
        print(*merge(list))

if __name__ == "__main__":
    main()