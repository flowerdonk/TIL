import sys
sys.stdin = open('sample_input.txt')

def delta(arr):
    sum = 0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            for di, dj in (-1, 0), (0, 1), (1, 0), (0, -1):
                ni = i + di
                nj = j + dj
                if 0 <= ni < len(arr) and 0 <= nj < len(arr[i]):
                    sum += abs(arr[ni][nj] - arr[i][j])

    return sum

T = int(input())
for i in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    print(delta(arr))
