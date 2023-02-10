import sys
sys.stdin = open('input.txt')

def view(N, arr):
    total = 0
    n = 2
    while n < N - 2:
        if max(arr[n - 2:n + 3]) != arr[n]:
            n += 1
            continue
        else:
            total += arr[n] - max(arr[n - 2], arr[n - 1], arr[n + 1], arr[n + 2])
            n += 3
    return total

T = 10
for i in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    print(f'#{i} {view(N, arr)}')