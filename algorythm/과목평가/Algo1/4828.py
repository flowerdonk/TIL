import sys
sys.stdin = open('input.txt')

def sumOfPart(N, M, arr):
    total = []

    for idx in range(N - M + 1):
        total.append(sum(arr[idx:idx+M]))

    ans = max(total) - min(total)

    return ans

T = int(input())
for i in range(1, T + 1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    print(f'#{i} {sumOfPart(N, M, arr)}')
