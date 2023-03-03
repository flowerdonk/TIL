'''
def maze(arr):
    # 시작점, 끝점 찾기
    arr_i = ''.join(arr)
    start_x, start_y = divmod(arr_i.index('2'), N)
    end_x, end_y = divmod(arr_i.index('3'), N)

    # visited = [[0] * N] * N
    visited = [[0] * N for _ in range(N)]
    Q = [(start_x, start_y)]
    visited[start_x][start_y] = 1

    # 인접 지점 찾기
    # adjL = [[] * N] * N
    direction = [[-1, 0], [0, 1], [1, 0], [0, -1]]

    while Q:
        x, y = Q.pop(0)
        sx, sy = x, y

        for d in direction:
            nx, ny = sx + d[0], sy + d[1]
            if arr[nx][ny] != '1' and visited[nx][ny] == 0:
                Q.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1


    if visited[end_x][end_y] != 0:
        return 1
    else:
        return 0
'''

import sys
sys.stdin = open('input.txt')

T = 10
for tc in range(1, T + 1):
    _ = input()
    arr = [input() for _ in range(16)]
    arr_i = ''.join(arr)
    start_x, start_y = divmod(arr_i.index('2'), 16)
    visited = [[0] * 16 for _ in range(16)]
    Q = [(start_x, start_y)]
    visited[start_x][start_y] = 1
    ans = 0

    while Q:
        x, y = Q.pop()

        for d in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
            nx, ny = x + d[0], y + d[1]
            if arr[nx][ny] != '1' and visited[nx][ny] == 0:
                if arr[nx][ny] == '3':
                    Q.clear()
                    ans = 1
                    break
                Q.append((nx, ny))
                visited[nx][ny] = 1

    print(ans)