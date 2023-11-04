def main():
    dict = {}
    with open("input.txt", "r") as inputFile:
        for line in inputFile:
            for word in line.split():
                if word not in dict:
                    dict[word] = 0
                print(dict[word], end=" ")
                dict[word] += 1

if __name__ == "__main__":
    main()