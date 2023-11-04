def main():
    n, m = map(int, input().split())
    inputList = [int(i) for i in input().split()]
    for i in range(m):
        l, r = map(int, input().split())
        isFind, res = getAnyValueNotMin(inputList, l, r)
        if isFind:
            print(res)
        else:
            print("NOT FOUND")

def getAnyValueNotMin(inputList, l, r):
    min = inputList[l]
    for i in range(l, (r+1)):
        if inputList[i] < inputList[l]:
            min = inputList[i]
    
    res = None
    for i in range(l, (r+1)):
        if inputList[i] != min:
            res = inputList[i]
            break
    
    if res is None:
        return False, 0
    else:
        return True, res
    
if __name__ == "__main__":
    main()