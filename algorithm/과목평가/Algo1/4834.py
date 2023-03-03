import sys
sys.stdin = open('sample_input.txt')

def card(N, arr):
    mx = num = 0
    count = [0] * 10

    for num in arr:
        count[num] += 1

    for i in range(10):
        if count[i] >= mx:
            mx = count[i]
            num = i

    return (num, mx)

T = int(input())
for i in range(1, T + 1):
    N = int(input())
    arr = list(map(int, list(input())))
    result = card(N, arr)
    print(f'#{i}', end = ' ')
    print(*result)