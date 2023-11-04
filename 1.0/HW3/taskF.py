def main():
    gen1 = input()
    gen2 = input()
    genList1 = []
    for i in range(len(gen1) - 1):
        genList1.append(gen1[i] + gen1[i+1])
    genSet2 = set()
    for i in range(len(gen2) - 1):
        genSet2.add(gen2[i] + gen2[i+1])
    count = 0
    for i in genList1:
        if i in genSet2:
            count += 1
    print(count)
    
if __name__ == "__main__":
    main()