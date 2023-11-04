def checkPhoneNumber(numberList):

    for i in range(len(numberList)):
        numberList[i] = numberList[i].replace("-", "")
        numberList[i] = numberList[i].replace("(", "")
        numberList[i] = numberList[i].replace(")", "")
    
    for i in range(len(numberList)):
        if len(numberList[i]) > 7:
            numberList[i] = numberList[i].replace("+7", "8")
        else:
            numberList[i] = "8495" + numberList[i]

    res = []

    for i in range(1, len(numberList)):
        if numberList[0] == numberList[i]:
            res.append("YES")
        else:
            res.append("NO")
    
    return res

num = input()
num1 = input()
num2 = input()
num3 = input()

res = checkPhoneNumber([num, num1, num2, num3])
for i in range(len(res)):
    print(res[i])