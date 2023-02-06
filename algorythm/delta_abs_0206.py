from random import randrange

T = int(input())
sum = []
for i in range(T):
    # arr = [[randrange(1, 100) for i in range(0, 5)] for r in range(0, 5)]
    xy = int(input())
    arr = [list(map(int, input().split())) for _ in range(0, xy)]
    total = 0

    for x in range(5):
        for y in range(5):
            for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                ni, nj = x + di, y + dj # 인덱스 좌표
                if 0 <= ni < 5 and 0 <= nj < 5: # 0~4 내
                    total += abs(arr[ni][nj] - arr[x][y])
    sum.append(total)

for i in range(T):
    print(f'#{i + 1} {sum[i]}')