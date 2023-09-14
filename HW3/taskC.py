def main():
    n, m = map(int, input().split())
    set1, set2 = set(), set()
    for i in range(n):
        set1.add(int(input()))
    for i in range(m):
        set2.add(int(input()))
    print(len(set1.intersection(set2)))
    [print(item, end=" ") for item in sorted(set1 & set2)]
    print()
    print(len(set1 - set2))
    [print(item, end=" ") for item in sorted(set1 - set2)]
    print()
    print(len(set2 - set1))
    [print(item, end=" ") for item in sorted(set2 - set1)]
    print()

if __name__ == "__main__":
    main()