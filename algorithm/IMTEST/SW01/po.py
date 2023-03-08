import sys
sys.stdin = open('input1.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    po_i, po_j = 0, 0
    direction = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    for i in range(N):
        for j in range(N):
            if data[i][j] == 2:
                po_i, po_j = i, j

    stack = [(po_i, po_j)]
    cnt = 0

    while stack:
        si, sj = stack.pop(0)
        data[si][sj] = 0
        for d in direction:
            for n in range(1, N):
                temp = cnt
                ni = si + d[0] * n
                nj = sj + d[1] * n
                if 0 <= ni < N and 0 <= nj < N and data[ni][nj] == 1: # 알을 만나면
                    for m in range(1, N):
                        nni = ni + d[0] * m
                        nnj = nj + d[1] * m
                        if 0 <= nni < N and 0 <= nnj < N:
                            if not (nni, nnj) in stack:
                                stack.append((nni, nnj))
                                visited[nni][nnj] = visited[si][sj] + 1
                                if visited[nni][nni] > 3:
                                    stack.clear()
                            if data[nni][nnj] == 1:
                                cnt += 1
                                break
                if cnt != temp:
                    break
    print(f'#{tc} {cnt}')