# Task condition: https://contest.yandex.ru/contest/53029/problems/C/

def merge(seq1, seq2):
    res = [0] * (len(seq1) + len(seq2))
    index1, index2, i = 0, 0, 0
    while index1 < len(seq1) and index2 < len(seq2):
        if seq1[index1] < seq2[index2]:
            res[i] = seq1[index1]
            index1 += 1
            i += 1
        else:
            res[i] = seq2[index2]
            index2 += 1
            i += 1
    while index1 < len(seq1):
        res[i] = seq1[index1]
        index1 += 1
        i += 1
    while index2 < len(seq2):
        res[i] = seq2[index2]
        index2 += 1
        i += 1
    return res

def main():
    n = int(input())
    seq1 = [int(i) for i in input().split()]
    m = int(input())
    seq2 = [int(i) for i in input().split()]
    print(*merge(seq1, seq2))

if __name__ == "__main__":
    main()