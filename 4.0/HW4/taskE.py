# Task condition: https://contest.yandex.ru/contest/53032/problems/B/

def generation(l, r=0, s='', p=''):
    if l == 0 and r == 0:
        print(s)
    if l:
        generation(l - 1, r + 1, s + '(', p + ')')
        generation(l - 1, r + 1, s + '[', p + ']')
    if r:
        generation(l, r - 1, s + p[-1], p[:-1])

def main():
    n = int(input())
    if n %2 == 0:
        generation(n / 2)

if __name__ == "__main__":
    main()