T = int(input())
for i in range(1, T + 1):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort(reverse=True)
    print(f'#{i} {sum(arr[:K])}')