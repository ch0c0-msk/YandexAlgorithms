def binarySearch(c, list):
    l, r = 0, len(list) - 1
    isFind = False
    while (l <= r) and (isFind == False):
        m = (l + r) // 2
        if  c == list[m]:
            isFind = True
        elif c > list[m]:
            l = m + 1
        else:
            r = m - 1
    if isFind:
        return "YES"
    else:
        return "NO"
def main():
    n, k = map(int, input().split())
    commonList = [int(i) for i in input().split()]
    checkList = [int(i) for i in input().split()]
    for c in checkList:
        print(binarySearch(c, commonList))
if __name__ == "__main__":
    main()