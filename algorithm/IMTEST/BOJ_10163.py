def Color(arr, N):
    result = []
    B = 1001
    base = [[0 for _ in range(B)] for _ in range(B)]
    for i in range(N):
        x = arr[i][0]
        y = arr[i][1]
        w = arr[i][2]
        h = arr[i][3]

        for hth in range(h):
            for wth in range(w):
                base[x + wth][y + hth] = i + 1
    
    for n in range(1, N + 1):
        count = 0
        for i in range(B):
            for j in range(B):
                if base[i][j] == n:
                    count += 1
        result.append(count)

    return result


N = int(input())
arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))

result = Color(arr, N)
for i in range(N):
    print(result[i])