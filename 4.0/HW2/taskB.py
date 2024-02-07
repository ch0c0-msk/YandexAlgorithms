# Task condition: https://contest.yandex.ru/contest/53030/problems/B/

def findBaseStringLength(inputStr):
    x, p, h = createHashTable(inputStr)
    origStrLength = len(inputStr)
    inputStr = ' ' + inputStr
    baseStrLength = origStrLength
    for i in range(1, origStrLength):
        if isEqual(x, p, h, i, 1, (origStrLength - i + 1)):
            baseStrLength = origStrLength - i
    return baseStrLength

def createHashTable(str):
    strLen = len(str)
    p = 10**9 + 7
    _x = 256
    hashTable = [0]*(strLen + 1)
    x = [0]*(strLen + 1)
    x[0] = 1
    str = ' '+str
    for i in range(1, (strLen + 1)):
        hashTable[i] = (hashTable[i-1] * _x + ord(str[i])) % p
        x[i] = (x[i-1] * _x) % p
    return x, p, hashTable

def isEqual(x, p, h, len, from1, from2):
    return (
            (h[from1 + len - 1] + h[from2 - 1] * x[len]) % p ==
            (h[from2 + len - 1] + h[from1 - 1] * x[len]) % p
    )

def main():
    inputStr = input()
    print(findBaseStringLength(inputStr))

if __name__ == "__main__":
    main()