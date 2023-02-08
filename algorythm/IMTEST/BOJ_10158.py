def ant(W, H, T, p, q):
    x, y = p, q
    # [오른쪽 위, 왼쪽 아래, 왼쪽 위, 오른쪽 아래]
    di = [1, -1, -1, 1]
    dj = [1, -1, 1, -1]

    for i in range(T):
        pass

    return (x, y)


W, H = map(int, input().split())
p, q = map(int, input().split())
T = int(input())

print(*ant(W, H, T, p, q))
