# Task condition: https://contest.yandex.ru/contest/53029/problems/E/

def main():

    n = int(input())
    list = [input() for _ in range(n)]

    print('Initial array:')
    print(*list, sep=', ')
    print('**********')

    maximum = len(list[0])

    for i in range(1, maximum + 1):
        print(f'Phase {i}')

        list_old = list
        list = []
        for tabl in range(10):
            res = []
            for slovo in list_old:
                if int(slovo[maximum - i]) == tabl:
                    res.append(slovo)
                    list.append(slovo)

            if len(res) == 0:
                print(f'Bucket {tabl}: empty')
            else:
                print(f"Bucket {tabl}:", end=' ')
                print(*res, sep=', ')
        print('**********')


    print('Sorted array:')
    print(*list, sep=', ')

if __name__ == "__main__":
    main()

