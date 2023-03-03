import sys
sys.stdin = open('input.txt')

def babygin(nums):
    check = 0
    cnt = [0] * 10
    for num in nums:
        cnt[num] += 1

    for idx in range(10):
        while cnt[idx] >= 3:
            cnt[idx] -= 3
            check += 1
        while cnt[idx] >= 1 and cnt[idx + 1] >= 1 and cnt[idx + 2]:
            cnt[idx] -= 1
            cnt[idx + 1] -= 1
            cnt[idx + 2] -= 1
            check += 1
        if cnt.count(0) == 10:
            break
    if check == 2:
        return 1
    else:
        return 0

T = int(input())
for i in range(1, T + 1):
    nums = list(map(int, input()))
    print(f'#{i} {babygin(nums)}')
