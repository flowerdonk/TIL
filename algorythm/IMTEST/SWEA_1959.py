import sys
sys.stdin = open('input.txt')

def Max_sum(N, M, A, B):
    mx = []

    if N >= M:
        L = N
        S = M
        Larr = A
        Sarr = B
    else:
        L = M
        S = N
        Larr = B
        Sarr = A

    for l in range(L - S + 1):
        sm = 0
        for s in range(S):
            sm += Sarr[s] * Larr[l + s]
        mx.append(sm)

    return max(mx)

T = int(input())
for i in range(1, T + 1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    print(f'#{i} {Max_sum(N, M, A, B)}')