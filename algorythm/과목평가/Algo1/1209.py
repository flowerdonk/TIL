import sys
sys.stdin = open('sample_input.txt')

def maxsum(N, nums):
    total = []
    nums_T = list(map(list, zip(*nums)))
    dia1 = 0
    dia2 = 0
    for line in range(N):
        total.append(sum(nums[line]))
        total.append(sum(nums_T[line]))
        dia1 += nums[line][line]
        dia2 += nums_T[line][line]

    total.append(dia1)
    total.append(dia2)

    return max(total)

T = 10
N = 100
for i in range(1, T + 1):
    _ = input()
    nums = [list(map(int, input().split())) for _ in range(N)]
    print(f'#{i} {maxsum(N, nums)}')