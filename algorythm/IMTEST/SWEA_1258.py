def storage(n, arr):


    return

T = int(input())
for i in range(1, T + 1):
    n = int(input())
    arr = [map(int, input().split()) for _ in range(n)]
    print(f'#{i} {storage(n, arr)}')