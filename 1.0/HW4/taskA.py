def main():
    n = int(input())
    dict = {}
    for i in range(n):
        key, val = input().split()
        dict[key] = val
    word = input()
    if word in dict.keys():
        print(dict[word])
    else:
        for key in dict.keys():
            if dict[key] == word:
                print(key)
                break
    
if __name__ == "__main__":
    main()