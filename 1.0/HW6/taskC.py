def binarySearch(w, h, n):
    l = max(w, h)
    r = l * n
    while l < r:
        m = (l + r) // 2
        if (m // w) * (m // h) < n:
            l = m + 1
        else:
            r = m
    return l

def main():
    w, h, n = map(int, input().split())
    print(binarySearch(w,h,n))

if __name__ == "__main__":
    main()