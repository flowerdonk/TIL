import sys
sys.stdin = open('input.txt')

## 교수님 풀이
T = 10
for i in range(1, T + 1):
    _ = int(input())
    arr = [[0] + list(map(int, input().split())) + [0] for _ in range(100)]
    mn = 100 * 100
    for sj in range(1, 101):
        # [1] 시작지점 찾기
        si = 0
        if arr[si][sj] != 1:
            continue

        cnt, dj = 0, 0
        ci, cj = si, sj

        while ci < 99:
            cnt += 1
            if dj == 0:
                if arr[ci][cj - 1] == 1: # 좌측
                    dj = -1
                elif arr[ci][cj + 1] == 1: # 우측
                    dj = 1
                else:
                    ci += 1
            else:
                if arr[ci][cj + dj] == 0: # 진행방향이 막힌경우 아래로
                    dj = 0
                    ci += 1
            cj += dj

        if mn >= cnt:
            mn, ans = cnt, sj - 1

    print(f'#{i} {ans}')

## 다시 풀이
def ladder(arr, N):
    mn = N * N

    for sj in range(1, N + 1):
        si = 0

        if arr[si][sj] != 1:
            continue

        cnt = 0
        dj = 0 # 선을 만나면 좌, 우 이동하는 방향
        ci, cj = si, sj

        while ci < N - 1:
            cnt += 1
            if dj == 0: # 방향 아래
                if arr[ci][cj - 1] == 1:
                    dj = -1
                elif arr[ci][cj + 1] == 1:
                    dj = 1
                else:
                    ci += 1
            else:
                if arr[ci][cj + dj] == 0:
                    dj = 0
                    ci += 1
            cj += dj

        if mn >= cnt:
            mn = cnt
            ans = sj - 1

    return ans


T = 10
N = 100
for i in range(1, T + 1):
    _ = int(input())
    arr = [[0] + list(map(int, input().split())) + [0] for _ in range(N)]
    print(f'#{i} {ladder(arr, N)}')



