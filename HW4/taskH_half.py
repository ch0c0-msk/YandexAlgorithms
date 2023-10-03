def isAllItemsIsNull(map):
    allNullFlag = True
    for i in map:
        if map[i] != 0:
            allNullFlag = False
            break
    return allNullFlag

def countOfOccurences(signMap, str):
    signCounterMap = signMap.copy()
    res = 0
    windowSize = 0
    for i in range(len(str)):
        currChar = str[i]
        if currChar in signCounterMap:
            if signCounterMap[currChar] != 0:
                signCounterMap[currChar] -= 1
                windowSize += 1
            else:
                if isAllItemsIsNull(signCounterMap):
                    res += 1
                for j in range(windowSize):
                    signCounterMap[str[i-windowSize+j]] += 1
                    if str[i-windowSize+j] == str[i]:
                        signCounterMap[str[i-windowSize+j]] -= 1
                        windowSize = windowSize - j - 1
                        break
        else:
            if isAllItemsIsNull(signCounterMap):
                res += 1
            signCounterMap = signMap.copy()
            windowSize = 0
    return res

def main():
    g, s = map(int, input().split())
    word = input()
    str = input()
    signMap = {}
    for w in word:
        if w not in signMap:
            signMap[w] = 0
        signMap[w] += 1
    print(countOfOccurences(signMap, str))


if __name__ == "__main__":
    main()