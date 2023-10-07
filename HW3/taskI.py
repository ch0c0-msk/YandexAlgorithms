def main():
    n = int(input())
    allLangSet = set()
    currLangSet = set()
    commonLangSet = set()
    for i in range(n):
        m = int(input())
        for j in range(m):
            lang = input()
            currLangSet.add(lang)
        allLangSet = allLangSet.union(currLangSet)
        if i == 0:
            commonLangSet = currLangSet
        commonLangSet = commonLangSet.intersection(currLangSet)
        currLangSet.clear()

    print(len(commonLangSet))
    if len(commonLangSet) > 0:
        [print(i) for i in commonLangSet]

    print(len(allLangSet))
    if len(allLangSet) > 0:
        [print(i) for i in allLangSet]

if __name__ == "__main__":
    main()