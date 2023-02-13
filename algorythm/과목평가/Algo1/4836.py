# import sys
# sys.stdin = open('sample_input.txt')

def color(N, square):
    board = [[0 for _ in range(10)] for _ in range(10)]

    for i in range(N):
        cnt = 0
        lx, ly, rx, ry, c1 = square[i]

        for x in range(lx, rx + 1):
            for y in range(ly, ry + 1):
                if board[x][y] == 0 or board[x][y] == c1:
                    board[x][y] = c1
                else:
                    board[x][y] = 3


    for x in range(10):
        for y in range(10):
            if board[x][y] == 3:
                cnt += 1

    return cnt

T = int(input())
for i in range(1, T + 1):
    square = []
    N = int(input())
    for j in range(N):
        square.append(list(map(int, input().split())))
    print(f'#{i} {color(N, square)}')