def createPrefixSum(nums):
    res = [0] * (len(nums) + 1)
    for i in range(1, len(nums)+1):
        res[i] = res[i-1] + nums[i-1]
    return res

def findCountSets(prefixSum, k):
    res = 0
    for i in range(len(prefixSum) - 1):
        for j in range(i+1, len(prefixSum)):
            if (prefixSum[j] - prefixSum[i] == k):
                res += 1
            elif (prefixSum[j] - prefixSum[i] > k):
                break
    return res

def main():
    n, k = map(int, input().split())
    nums = [int(i) for i in input().split()]
    print(findCountSets(createPrefixSum(nums), k))

if __name__ == "__main__":
    main()