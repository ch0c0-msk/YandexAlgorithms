def main():
    n = int(input())
    dict = {}
    inputList = [int(i) for i in input().split()]
    for i in range(n):
        dict[i+1] = inputList[i]
    
    k = int(input())
    for i in map(int, input().split()):
        dict[i] -= 1
    
    for i in dict:
        if dict[i] >= 0:
            print("NO")
        else:
            print("YES")

if __name__ == "__main__":
    main()