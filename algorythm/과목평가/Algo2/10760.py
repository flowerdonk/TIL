def spaceship(N, M, arr):
    result = 0
    delta = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)] # 시계 방향

    for i in range(1, N + 1):
        for j in range(1, M + 1):
            cnt = 0
            for d in delta:
                if arr[i + d[0]][j + d[1]] < arr[i][j]:
                    cnt += 1
                if cnt >= 4:
                    result += 1
                    break

    return result

T = int(input())
for i in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [[9] + list(map(int, input().split())) + [9] for _ in range(N)] # 양 옆 패딩
    arr = [[9] * (M + 2)] + arr + [[9] * (M + 2)] # 위 아래 패딩
    print(f'#{i} {spaceship(N, M, arr)}')