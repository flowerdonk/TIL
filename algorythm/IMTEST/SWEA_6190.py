def danzo(N, arr):
    mx = []

    for i in range(N - 1):
        for j in range(i + 1, N):
            cnt = 1
            num = arr[i] * arr[j]
            Snum = list(str(num))
            for n in range(len(Snum) - 1):
                if Snum[n] <= Snum[n + 1]:
                    cnt = 1
                else:
                    cnt = 0
                    break
            if cnt == 0:
                continue
            else:
                mx.append(int(num))

    if not mx:
        return -1
    else:
        return max(mx)

T = int(input())
for i in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    print(f'#{i} {danzo(N, arr)}')