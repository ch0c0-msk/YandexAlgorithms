# Task condition: https://contest.yandex.ru/contest/53032/problems/B/

def isSafe(board, row, col, n):
    for i in range(row):
        if board[i][col] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, n), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve(board, row, n, count):
    if row == n:
        count[0] += 1
        return

    for col in range(n):
        if isSafe(board, row, col, n):
            board[row][col] = 1
            solve(board, row + 1, n, count)
            board[row][col] = 0

def main():
    n = int(input())

    board = [[0] * n for _ in range(n)]
    count = [0]

    solve(board, 0, n, count)
    print(count[0])

if __name__ == "__main__":
    main()