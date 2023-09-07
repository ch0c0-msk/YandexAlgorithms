def findBigNumbersCount(seq):
    res = 0
    for i in range(1,len(seq) - 1):
        if seq[i] > seq[i-1] and seq[i] > seq[i+1]:
            res += 1
    return res

seq = [int(i) for i in input().split()]
print(findBigNumbersCount(seq))