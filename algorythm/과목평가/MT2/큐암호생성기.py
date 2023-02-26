'''
def code(arr):
    # mn = min(arr)
    cnt = 1

    while cnt:
        for n in range(1, 6):
            fst = arr.pop(0)
            if fst - n <= 0:
                arr.append(0)
                cnt = 0
                break
            else:
                arr.append(fst - n)

T = 10
for i in range(1, T + 1):
    _ = input()
    arr = list(map(int, input().split()))
    code(arr)

    print(f'#{i}', *arr)
'''

import sys
sys.stdin = open('input.txt')

T = 10
for tc in range(1, T + 1):
    _ = input()
    data = list(map(int,input().split()))

    while data[-1] > 0:
        for n in range(1, 6):
            num = data.pop(0)
            if num - n > 0:
                data.append(num - n)
            else:
                data.append(0)
                break

    print(data)