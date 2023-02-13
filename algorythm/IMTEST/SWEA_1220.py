import sys
sys.stdin = open('input.txt')

def table(arr):
    # 전치
    arr_t = list(zip(*arr))
    # 왼쪽 : N극, 오른쪽 : S극
    # 1 : N극, 2 : S극
    cnt = 0

    for x in range(N):
        flag = 0
        for y in range(N):
            if arr_t[x][y] == 1:
                flag = 1
            elif arr_t[x][y] == 2:
                if flag == 1:
                    cnt += 1
                    flag = 0

    return cnt

T = 10
for i in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    print(f'#{i} {table(arr)}')