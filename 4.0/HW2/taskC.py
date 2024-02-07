# Task condition: https://contest.yandex.ru/contest/53030/problems/C/

def createZfuncList(inputStr):
    z = [0]*len(inputStr)
    strLen = len(inputStr)
    l = r = 0
    for i in range(1, strLen):
        if i <= r:
            z[i] = min(r - i + 1, z[i-l])
        while (i + z[i] < strLen and inputStr[z[i]] == inputStr[z[i] + i]):
            z[i] += 1
        if (i + z[i] - 1 > r):
            l = i
            r = i + z[i] - 1
    return z

def main():
    inputStr = input()
    print(*createZfuncList(inputStr))

if __name__ == "__main__":
    main()