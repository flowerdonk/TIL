def ant(W, H, T, p, q):
    x, y = q , p
    # [오른쪽 위, 왼쪽 아래, 왼쪽 위, 오른쪽 아래]
    di = [1, -1, -1, 1]
    dj = [1, -1, 1, -1]
    dij = [[1, 1], [-1, -1], [-1, 1], [1, -1]] # 방향 판독
    base = [[0 for _ in range(W + 1)] for _ in range(H + 1)]

    for h in range(H + 1): # 격자 공간, 양끝 모서리 1, 나머지 0
        for w in range(W + 1):
            if w == 0 or w == W:
                base[h][w] = 1
            else:
                base[h][w] = 0

            if h == 0 or h == H:
                base[h][w] = 1

    xx, yy = x, y  # 이전 좌표
    for i in range(T):
        if i == 0:
            x += di[0]
            y += dj[0]
            continue

        if base[x][y] != 1: # 벽과 만나지 않으면 같은 방향으로 계속 이동
            direction = dij.index([x-xx, y-yy])
            xx, yy = x, y  # 이전 좌표
            x += di[direction]
            y += dj[direction]
            continue

        else:
            direction = dij.index([x-xx, y-yy])
            xx, yy = x, y  # 이전 좌표
            # 0 -> 2, 1 -> 3, 2 -> 0, 3 -> 1
            if direction == 0 or direction == 1:
                x += di[direction + 2]
                y += dj[direction + 2]
            elif direction == 2 or direction == 3:
                x += di[direction - 2]
                y += dj[direction - 2]
            continue

    return (x, y)


W, H = map(int, input().split())
p, q = map(int, input().split())
T = int(input())

print(*ant(W, H, T, p, q))
