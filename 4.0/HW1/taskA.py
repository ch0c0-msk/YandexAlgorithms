# Task condition: https://contest.yandex.ru/contest/53029/problems/

# Метод трех указателей
def partition(a, list, l, r):
    n, e, g = l, l, l
    while n < len(list):
        if list[n] < a:
            temp = list[n]
            list[n] = list[g]
            list[g] = list[e]
            list[e] = temp
            e += 1
            g += 1
            n += 1
        elif list[n] == a:
            temp = list[n]
            list[n] = list[g]
            list[g] = temp
            g += 1
            n += 1
        else:
            n += 1
    return e

def main():
    n = int(input())
    sourceList = [int(i) for i in input().split()]
    a = int(input())
    if len(sourceList) > 0:
        pivot = partition(a, sourceList, 0, len(sourceList) - 1)
        print(pivot)
        print(n - pivot)
    else:
        print(0)
        print(0)

if __name__ == "__main__":
    main()