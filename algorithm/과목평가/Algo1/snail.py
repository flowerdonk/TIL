import sys
sys.stdin = open('sample_input.txt')

def seat(X, Y, N):
    board = [[0 for _ in range(X)] for _ in range(Y)]

    if N > X * Y:
        return 0

    x, y = 0, 0
    idx = 0

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    board[0][0] = 1

    for n in range(2, N + 1):

        while True:
            nx = x + dx[idx]
            ny = y + dy[idx]
            if 0 <= nx < X and 0 <= ny <Y and board[ny][nx] == 0:
                board[ny][nx] = n
                x = nx
                y = ny
                break
            else:
                idx = (idx + 1) % 4

    return (x + 1, y + 1)

T= int(input())
for i in range(1, T + 1):
    X, Y = map(int, input().split())
    N = int(input())
    print(f'#{i} {seat(X, Y, N)}')