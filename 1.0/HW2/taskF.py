def findMinSeq(n, seq):
    res = []
    for i in range(len(seq)):
        isSimmetric = True
        for j in range((len(seq) - i) // 2):
            if seq[i + j] != seq[-1 - j]:
                res.insert(0, seq[i])
                isSimmetric = False
                break
        if isSimmetric:
            break
    return res

def main():
    n = int(input())
    seq = [int(i) for i in input().split()]
    res = findMinSeq(n, seq)
    if len(res) == 0:
         print(0)
    else:
        print(len(res))
        for item in res:
            print(item, end=" ")


if __name__ == "__main__":
    main()