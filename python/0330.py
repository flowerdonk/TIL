'''
def promising(i, j):
    for di, dj in [[-1, -1], [-1, 0], [-1, 1]]: # 좌상, 상, 우상
        ni, nj = i + di, j + dj
        while 0 <= ni < N and 0 <= nj < N:
            if board[ni][nj]:                   # 다른 퀸이 있으면
                return 0                        # 실패
            ni, nj = ni + di, nj + dj           # 해당 방향은 성공, 다음 방향
    return 1                                    # i, j에 퀸을 놓을 수 있음

def f(i, N):
    global cnt
    if i == N: # N개의 퀸을 놓은 경우
        cnt += 1
    else:
        for j in range(N):
            if promising(i, j):
                board[i][j] = 1
                f(i + 1, N)
                board[i][j] = 0

T = int(input())
for tc in range(1, T + 1):
    N = int(input())

    board = [[0] * N for _ in range(N)]
    cnt = 0
    f(0, N)
    print(cnt)
'''

def f(i, k, s, key, rs):
    global cnt, c
    c += 1
    if s == key:
        cnt += 1
        return
    elif i == k or s > key or s + rs < key:
        return
    else:
        bit[i] = 0
        f(i + 1, k, s, key, rs - A[i])
        bit[i] = 1
        f(i + 1, k, s + A[i], key, rs - A[i])
        return

A = [i for i in range(1, 11)]
N = 10
bit = [0] * N
key = 55
cnt = 0
c = 0 # 재귀 호출 횟수
f(0, N, 0, key, sum(A))
print(cnt, c)