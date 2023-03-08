import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input()) # 지도 한 변의 크기
    data = [list(map(int, input().split())) for _ in range(N)]
    # 오른쪽 -> 아래 -> 왼쪽 -> 위 -> 오른쪽
    direction = [[0, 1], [1, 0], [0, -1], [-1, 0]] # 해당 순서대로 움직일 수 있음
    d_idx = 0
    cnt = 0
    apple = [] # (사과 번호, i, j)
    for i in range(N):
        for j in range(N):
            if data[i][j] != 0:
                apple.append((data[i][j], i, j))
    apple.sort(key = lambda x : x[0])

    i, j = 0, 0
    while apple:
        if i <= apple[0][1]:
            mn_i = i
            mx_i = apple[0][1]
        else:
            mn_i = apple[0][1]
            mx_i = i

        if j <= apple[0][2]:
            mn_j = j
            mx_j = apple[0][2]
        else:
            mn_j = apple[0][2]
            mx_j = j

        if i == apple[0][1] and j == apple[0][2]:
            apple.pop(0)
        else:
            ni = i + direction[d_idx][0]
            nj = j + direction[d_idx][1]
            if mn_i <= ni <= mx_i and mn_j <= nj <= mx_j:
                i = ni
                j = nj
            else:
                d_idx = (d_idx + 1) % 4
                cnt += 1


    print(f'#{tc} {cnt}')