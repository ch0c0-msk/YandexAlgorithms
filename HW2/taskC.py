def findNearestNumber(seq, x):
    res = seq[0]
    for i in range(1, len(seq)):
        if abs(seq[i] - x) < abs(res - x):
            res = seq[i]
    return res
k = int(input())
seq = [int(i) for i in input().split()]
x = int(input())
print(findNearestNumber(seq, x))
        