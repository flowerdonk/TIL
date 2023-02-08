def Snail(C, R, K):
    di = [] # i 증감값
    dj = [] # j 증감값
    result = (0)
    if C > R:
        for n in range(R, 0, -1): # 한쪽 변의 길이 -> 1
            # 외각 사각형의 경우 1: (1, 0), 2: (0, -1), 3: (-1, 0), 4: (0, 1)
            for _ in range(n): # (1, 0) or (-1, 0)
                di.append(1 - 2 * ((R - n) % 2))
                dj.append(0) # n이 1번째 일 때 +1, 3번째 일 때 -1
            for _ in range(n): # (0, -1) or (0, 1)
                di.append(0) # n이 2번째 일 때 +1, 4번째 일 때 -1
                dj.append(1 - 2 * ((R - n) % 2))

    elif R > C:
        for n in range(R, 0, -1): # 한쪽 변의 길이 -> 1
            # 외각 사각형의 경우 1: (1, 0), 2: (0, -1), 3: (-1, 0), 4: (0, 1)
            for _ in range(n): # (1, 0) or (-1, 0)
                di.append(1 - 2 * ((R - n) % 2))
                dj.append(0) # n이 1번째 일 때 +1, 3번째 일 때 -1
            for _ in range(n - 2): # (0, -1) or (0, 1)
                di.append(0) # n이 2번째 일 때 +1, 4번째 일 때 -1
                dj.append(1 - 2 * ((R - n) % 2))

    else:
        for n in range(R, 0, -1): # 한쪽 변의 길이 -> 1
            # 외각 사각형의 경우 1: (1, 0), 2: (0, -1), 3: (-1, 0), 4: (0, 1)
            for _ in range(n): # (1, 0) or (-1, 0)
                di.append(1 - 2 * ((R - n) % 2))
                dj.append(0) # n이 1번째 일 때 +1, 3번째 일 때 -1
            for _ in range(n - 1): # (0, -1) or (0, 1)
                di.append(0) # n이 2번째 일 때 +1, 4번째 일 때 -1
                dj.append(1 - 2 * ((R - n) % 2))

    arr = [[0 for _ in range(C)] for _ in range(R)]

    i = j = 0
    for m in range(1, C * R + 1):
        if m == 1: # 최종값 1
            arr[R - 1 - i][j] = 1
        else:
            # 인덱스를 해당 위치로 이동 -> 값 순차적 대입
            i += di[m - 1]
            j += dj[m - 1]
            arr[R - 1 - i][j] = m
            if m == K:
                result = (j + 1, i + 1)

    return result

C, R = map(int, input().split())
K = int(input())
print(*Snail(C, R, K))