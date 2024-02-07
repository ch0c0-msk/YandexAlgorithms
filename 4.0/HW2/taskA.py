# Task condition: https://contest.yandex.ru/contest/53030/problems/A/

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
            (h[from1 + len] + h[from2] * x[len]) % p ==
            (h[from2 + len] + h[from1] * x[len]) % p
    )

def main():
    inputString = input()
    requestCount = int(input())
    x, p, hashTable = createHashTable(inputString)
    outputList = list()
    for i in range(requestCount):
        l, from1, from2 = map(int, input().split())
        if isEqual(x, p, hashTable, l, from1, from2):
            outputList.append("yes")
        else:
            outputList.append("no")
    for elem in outputList:
        print(elem)

if __name__ == "__main__":
    main()