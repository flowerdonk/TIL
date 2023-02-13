import sys
sys.stdin = open('sample_input.txt')

def sumsub(N, K):
    A = [i for i in range(1, 13)]
    total = len(A)
    subs = []
    count = 0

    for i in range(1 << total):
        for j in range(total):
            if i & (1 << j):
                subs.append(A[j])
        if len(subs) == N and sum(subs) == K:
            count += 1
        subs.clear()

    return count

T = int(input())
for i in range(1, T + 1):
    N, K = map(int, input().split())
    print(f'#{i} {sumsub(N, K)}')
