# Task problem: https://contest.yandex.ru/contest/53033/problems/A/?success=99491164#30404/2018_11_06/lm7dcCtB2h

def findCx(x):
    i, j = 1, 1
    iSq, jCub = 1, 1
    k = 1
    while k <= x:
        if iSq== jCub:
            i += 1
            iSq = i*i
            k -= 1
        elif iSq < jCub:
            res = iSq
            i += 1
            iSq = i*i
        else:
            res = jCub
            j += 1
            jCub = j*j*j
        k += 1

    return res

def main():
    x = int(input())
    print(findCx(x))

if __name__ == "__main__":
    main()