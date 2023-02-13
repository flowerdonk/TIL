import sys
sys.stdin = open('sample_input.txt')

def subset(arr):
    ans = 0
    N = len(arr)
    for i in range(1 << N):
        sum = 0
        for j in range(N):
            if i & (1 << j):
                sum += arr[j]
        if i != 0 and sum == 0:
            return 1

    return 0

T = int(input())
for i in range(1, T + 1):
    arr = list(map(int, input().split()))
    print(f'#{i} {subset(arr)}')