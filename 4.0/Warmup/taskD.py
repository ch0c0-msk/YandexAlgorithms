def main():
    firstWord = input()
    secondWord = input()
    firstWordLetterMap = {}

    for w in firstWord:
        if w not in firstWordLetterMap:
            firstWordLetterMap[w] = 0
        firstWordLetterMap[w] += 1

    isAnagramm = True
    for w in secondWord:
        if w not in firstWordLetterMap:
            isAnagramm = False
            break
        else:
            firstWordLetterMap[w] -= 1
    
    for w in firstWordLetterMap:
        if firstWordLetterMap[w] != 0:
            isAnagramm = False
            break
    
    if isAnagramm:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()