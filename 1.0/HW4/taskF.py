def main():
    dict = {}
    with open("input.txt", "r") as inputFile:
        for line in inputFile:
            name = line.split()[0]
            product = line.split()[1]
            count = int(line.split()[2])
            if name not in dict:
                dict[name] = {}
            if product not in dict[name]:
                dict[name][product] = 0
            dict[name][product] += count

    nameList = sorted(dict.keys())
    for name in nameList:
        productList = sorted(dict[name].keys())
        print(f"{name}:")
        for product in productList:
            print(f"{product} {dict[name][product]}")

if __name__ == "__main__":
    main()