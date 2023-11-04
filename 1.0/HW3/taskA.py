def findDiffDigitsCount(seq):
    digitsSet = set()
    for item in seq:
        digitsSet.add(item)
    return len(digitsSet)

def main():
    seq = [int(i) for i in input().split()]
    print(findDiffDigitsCount(seq))

if __name__ == "__main__":
    main()