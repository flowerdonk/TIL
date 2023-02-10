import sys
sys.stdin = open('input.txt')

def electric(K, N, M, station):
    charge = 0
    position = 0

    while position + K < N:
        if position + K in station:
            position += K
            charge += 1
        else:
            for i in range(1, K):
                if position + K - i in station:
                    position += K - i
                    charge += 1
                    break
                if i == K - 1:
                    return 0

    return charge

T = int(input())
for i in range(1, T + 1):
    K, N, M = map(int, input().split())
    station = list(map(int, input().split()))
    print(f'#{i} {electric(K, N, M, station)}')