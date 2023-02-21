import sys
sys.stdin = open('input.txt')

T = 10
num = 100
for n in range(1, T + 1):
    N, V = map(int, input().split()) # 입력받는 데이터 길이, 시작점
    arr = list(map(int, input().split())) # (from, to, from, to, ...)
    adjl = {}
    for i in range(N // 2):
        adjl[arr[i * 2]] = adjl.get(arr[i * 2], []) + [arr[i * 2 + 1]]

    print(adjl)
    turn = [1] * num
    visited = [0] * num
    Q = [V]

    while Q:
        pass
