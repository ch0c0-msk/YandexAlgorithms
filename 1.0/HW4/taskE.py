def main():
    n = int(input())
    dict = {}
    w, h = map(int, input().split())
    dict[w] = h

    for i in range(n-1):
        w, h = map(int, input().split())
        if w not in dict or dict[w] < h:
            dict[w] = h

    res = 0
    for i in dict:
        res += dict[i]
    print(res)

if __name__ == "__main__":
    main()