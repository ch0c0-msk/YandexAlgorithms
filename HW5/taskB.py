def main():
    n, k = map(int, input().split())
    nums = [int(i) for i in input().split()]
    left = 0
    res = 0
    currentSum = 0
    for right, num in enumerate(nums): 
        currentSum += num
        while currentSum > k:
            currentSum -= nums[left]
            left += 1
        if currentSum == k:
            res += 1
    print(res)

if __name__ == "__main__":
    main()
