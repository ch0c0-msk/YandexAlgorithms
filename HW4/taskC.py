def main():
    dict = {}
    with open("input.txt", "r") as inputFile:
        for line in inputFile:
            for word in line.split():
                if word not in dict:
                    dict[word] = 0
                dict[word] += 1
    
    max = -1
    for word in dict:
        if dict[word] > max:
            max = dict[word]
            maxWord = word
        elif dict[word] == max and word < maxWord:
            maxWord = word
    print(maxWord)

if __name__ == "__main__":
    main()