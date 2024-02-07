# Task condition: https://contest.yandex.ru/contest/53032/problems/A/

import itertools

n = int(input())
list = [str(i) for i in range(1, n + 1)]
res = set()

combination = itertools.permutations(list)

for i in combination:
    print(*i, sep='')