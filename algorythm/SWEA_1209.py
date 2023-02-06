import sys
sys.stdin = open('input.txt')

def Max(arr):
    findMax = []

    for i in range(len(arr)):
        sum = 0
        for r in range(len(arr[i])):
            sum += arr[i][r]
        findMax.append(sum)

    for i in range(len(arr)):
        sum = 0
        for r in range(len(arr[i])):
            sum += arr[r][i]
        findMax.append(sum)

    for i in range(len(arr)):
        sum = 0
        for r in range(len(arr[i])):
            if i == r:
                sum += arr[i][r]
        findMax.append(sum)

    for i in range(len(arr)):
        sum = 0
        for r in range(len(arr[i]), 0, -1):
            if i == r:
                sum += arr[i][r]
        findMax.append(sum)

    return max(findMax)


for i in range(10):
    N = int(input())
    Tcase = list(map(int, input().split()))
    arr = [Tcase for r in range(0, 100)]
    print(Max(arr))
