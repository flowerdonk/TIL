def storage(n, arr):
    i = 0
    while i < n:
        pos_i = 0
        pos_j = 0
        for j in range(n + 1):
            if arr[i][j] == 0:
                pos_j = j
                pos_i = i
            elif pos_j:
                w = j - pos_j - 1
        if pos_i:
            for idx in range(pos_i, n):
                if arr[idx][pos_j]:
                    h = idx - pos_i
                    i += h
                    break
        else:
            i += 1

    return

T = int(input())
for i in range(1, T + 1):
    n = int(input())
    arr = [[0] + map(int, input().split()) for _ in range(n)]
    print(f'#{i} {storage(n, arr)}')
