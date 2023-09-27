def isAccountExist(accountsMap, name):
    if name in accountsMap:
        return True
    return False

def checkAccount(accountsMap, name):
    if name not in accountsMap:
        accountsMap[name] = 0

def deposit(accountsMap, name, sum):
    checkAccount(accountsMap, name)
    accountsMap[name] += sum

def withdraw(accountsMap, name, sum):
    checkAccount(accountsMap, name)
    accountsMap[name] -= sum

def balance(accountsMap, name):
    if isAccountExist(accountsMap, name):
        return accountsMap[name]
    else:
        return "ERROR"

def transfer(accountsMap, outName, inName, sum):    
        withdraw(accountsMap, outName, sum)
        deposit(accountsMap, inName, sum)

def income(accountsMap, percent):
    for name in accountsMap:
        if balance(accountsMap, name) > 0:
            deposit(accountsMap, name, balance(accountsMap, name) * percent // 100)
def main():
    dict = {}
    with open("input.txt", "r") as inputFile:
        accountsMap = {}
        for line in inputFile:
            wordList = line.split()
            match wordList[0]:
                case "DEPOSIT":
                    deposit(accountsMap, wordList[1], int(wordList[2]))
                case "WITHDRAW":
                    withdraw(accountsMap, wordList[1], int(wordList[2]))
                case "TRANSFER":
                    transfer(accountsMap, wordList[1], wordList[2], int(wordList[3]))
                case "INCOME":
                    income(accountsMap, int(wordList[1]))
                case "BALANCE":
                    print(balance(accountsMap, wordList[1]))

if __name__ == "__main__":
    main()