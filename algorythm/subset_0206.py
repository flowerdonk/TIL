def subset():
    nums = list(map(int, input().split()))
    N = len(nums)
    zero = 0

    for i in range(1 << N):
        sum = 0
        for j in range(N):
            if i & (1 << j):
                sum += nums[j]

        if not i == 0 and sum == 0:
            zero = 1

    return zero


T = int(input())

for i in range(T):
    print(f'#{i + 1} {subset()}')


