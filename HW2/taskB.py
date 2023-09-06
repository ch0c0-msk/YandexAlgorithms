def getArrayType():
    inputNumber = int(input())
    if inputNumber != -2000000000:
        typesDict = {"CONSTANT": True, "ASCENDING": True, "DESCENDING": True, "WEAKLY ASCENDING": True, "WEAKLY DESCENDING": True, "RANDOM": True}
        prev = inputNumber
        inputNumber = int(input())
        while inputNumber != -2000000000:
            if inputNumber != prev:
                typesDict["CONSTANT"] = False
            if inputNumber <= prev:
                typesDict["ASCENDING"] = False
            if inputNumber < prev:
                typesDict["WEAKLY ASCENDING"] = False
            if inputNumber >= prev:
                typesDict["DESCENDING"] = False
            if inputNumber > prev:
                typesDict["WEAKLY DESCENDING"] = False
            prev = inputNumber
            inputNumber = int(input())
        for i in typesDict.keys():
            if typesDict[i] == True:
                return i
    else:
        return "UNKNOWN"
print(getArrayType())