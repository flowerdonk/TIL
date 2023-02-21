T = int(input())
for n in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    for i in range(N - 1, 0, -1):
        for j in range(0, i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    Narr = []
    for _ in range(5):
        Narr.append(arr.pop())
        Narr.append(arr.pop(0))

    print(f'#{n}', *Narr)