import sys
sys.stdin = open('input.txt')

def money(N):
    cnt = {50000 : 0, 10000 : 0, 5000 : 0, 1000 : 0, 500 : 0, 100 : 0, 50 : 0, 10 : 0}
    left = N
    for k in cnt.keys():
        cnt[k] = left // k
        left = left % k
    return cnt.values()

T = int(input())
for i in range(1, T + 1):
    N = int(input())
    print(f'#{i}')
    print(*money(N))