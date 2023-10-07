def main():
    n = int(input())
    birdSet = set()
    for i in range(n):
        x, y = map(int, input().split())
        birdSet.add(x)

    print(len(birdSet))
if __name__ == "__main__":
    main()