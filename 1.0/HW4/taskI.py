def main():
    n = int(input())
    wordMap = {}
    for i in range(n):
        word = input()
        wordLower = word.lower()
        for i, w in enumerate(word):
            if w.isupper():
                value = i
                break
        if wordLower not in wordMap:
            wordMap[wordLower] = []
        wordMap[wordLower].append(i)
    str = input()
    checkList = str.split()
    res = 0
    for word in checkList:
        countCapital = sum(1 for letter in word if letter.isupper())
        if countCapital != 1:
            res += 1
        else:
            indexCapital = next(i for i, c in enumerate(word) if c.isupper())
            wordLower = word.lower()
            if wordLower in wordMap and indexCapital not in wordMap[wordLower]:
                res += 1
    print(res)
if __name__ == "__main__":
    main()