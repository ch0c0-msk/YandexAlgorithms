def main():
    n, k = map(int, input().split())
    treeList = [int(i) for i in input().split()]
    left = 0
    treeCounter = [0] * (k + 1)
    distinctTreeCount = 0
    bestInterval = (0, (n-1))
    for right, tree in enumerate(treeList):
        if not treeCounter[tree]:
            distinctTreeCount += 1
        treeCounter[tree] += 1
        if distinctTreeCount == k:
            while(treeCounter[treeList[left]] > 1):
                treeCounter[treeList[left]] -= 1
                left += 1
            if (right - left) < (bestInterval[1] - bestInterval[0]):
                bestInterval = (left, right)

    print(bestInterval[0] + 1, end=" ")
    print(bestInterval[1] + 1)

if __name__ == "__main__":
    main()