def farm(N, arr):
    result = 0

    return result

T = int(input())
for i in range(1, T + 1):
    N = int(input())
    arr = [map(int, input()) for _ in range(N)]
    print(f'#{i} {farm(N, arr)}')
