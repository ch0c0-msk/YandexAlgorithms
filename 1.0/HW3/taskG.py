def main():
    n = int(input())
    turtleSet = set()
    count = 0
    for i in range(n):
        i, j = map(int, input().split())
        if (n - i - 1) == j and (j not in turtleSet) and (i >= 0 and j >= 0):
            turtleSet.add(j)
            count += 1
    print(count)
    
if __name__ == "__main__":
    main()