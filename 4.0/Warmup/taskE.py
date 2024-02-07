def createPrefixSumArray(list):
    res = [0]*(len(list)+1)
    for i in range(0, len(list)):
        res[i+1] = list[i] + res[i]
    return res

def findDiscontentLevel(studentRatings, prefixSumArray, i):
    res = 0
    res += studentRatings[i] * i - prefixSumArray[i]
    res += prefixSumArray[-1] - prefixSumArray[i+1] - (len(studentRatings) - i - 1) * studentRatings[i]
    return res

def main():
    n = int(input())
    studentRatings = [int(i) for i in input().split()]
    ans = [0]*n
    prefixSumArray = createPrefixSumArray(studentRatings)
    for i in range(len(ans)):
        ans[i] = findDiscontentLevel(studentRatings, prefixSumArray, i)
    print(*ans)
if __name__ == "__main__":
    main()