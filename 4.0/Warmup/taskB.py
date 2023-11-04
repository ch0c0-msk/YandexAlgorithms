def main():
    a, b, c, d = map(int, input().split())
    denumerator = findLCM(b, d)
    numerator = a * (denumerator // b) + c * (denumerator // d)
    print(*shorten(numerator, denumerator))

def shorten(numerator, denumerator):
    nod = findNOD(numerator, denumerator)
    return numerator // nod, denumerator // nod

def findNOD(a, b):
    if (a == 0 or b == 0):
        return (a + b)
    else:
        if a > b:
            return findNOD(a-b, b)
        else:
            return findNOD(a, b-a)

def findLCM(a, b):
    nod = findNOD(a, b)
    return (a * b) // nod

if __name__ == "__main__":
    main()