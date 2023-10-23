def main():
    n, r = tuple(map(int, input().split()))
    monumentList = [int(i) for i in input().split()]
    last = 0
    result = 0
    for first in range(n):
        while last < len(monumentList) and (monumentList[last] - monumentList[first]) <= r:
            last += 1
        result += len(monumentList) - last
    print(result)
if __name__ == "__main__":
    main()