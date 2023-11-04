def binarySearch(c, list):
    l, r = 0, len(list) - 1
    isFind = False
    while (l <= r):
        m = (l + r) // 2
        if  c == list[m]:
            return list[m]
        elif c > list[m]:
            l = m + 1
        else:
            r = m - 1
    if l != len(list) and abs(list[l] - c) < abs(list[r] - c):
        return list[l]
    else:
        return list[r]



def main():
    n, k = map(int, input().split())
    commonList = [int(i) for i in input().split()]
    checkList = [int(i) for i in input().split()]
    for c in checkList:
        print(binarySearch(c, commonList))
if __name__ == "__main__":
    main()