import sys
sys.stdin = open('sample_input.txt')

def flatten(N, arr):

    for dump in range(N):
        mx_idx = arr.index((max(arr)))
        mn_idx = arr.index((min(arr)))
        arr[mx_idx] -= 1
        arr[mn_idx] += 1

        if max(arr) - min(arr) <= 1:
            break

    return max(arr) - min(arr)

T = 10
for i in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    print(f'#{i} {flatten(N, arr)}')