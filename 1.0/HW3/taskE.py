def main():
    buttons = set(int(i) for i in input().split())
    digits = set(int(d) for d in input())
    print(len(digits - buttons))

if __name__ == "__main__":
    main()