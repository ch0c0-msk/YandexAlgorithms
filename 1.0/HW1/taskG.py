def findDetailsCount(n, k, m):
    count_d = 0

    while n >= k:
        count_z = n // k
        count_d += count_z * (k // m)
        n -= count_z * (k // m) * m

    print(count_d)

n, k, m = map(int, input().split())
findDetailsCount(n, k, m)
