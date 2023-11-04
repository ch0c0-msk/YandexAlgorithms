def main():
    [print(i, end=" ") for i in sorted(set([int(i) for i in input().split()]) & set([int(i) for i in input().split()]))]
    
if __name__ == "__main__":
    main()