def findTempareture(tRoom, tCond, mode):
    if mode == "fan":
        print(tRoom)
    elif mode == "auto":
        print(tCond)
    elif mode == "heat":
        if tRoom < tCond:
            print(tCond)
        else:
            print(tRoom)
    elif mode == "freeze":
        if tRoom < tCond:
            print(tRoom)
        else:
            print(tCond)

tRoom, tCond = map(int, input().split())
mode = input()
findTempareture(tRoom, tCond, mode)