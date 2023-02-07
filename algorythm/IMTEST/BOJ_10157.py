def Snail(C, R, K):
    di = [] # i 증감값
    dj = [] # j 증감값

    for n in range(R, 0, -1): # 한쪽 변의 길이 -> 1
        # 외각 사각형의 경우 1: (0, 1), 2: (1, 0), 3: (0, -1), 4: (-1, 0)
        for _ in range(n): # (0, 1) or (0, -1)
            di.append(0)
            dj.append(1 - 2 * ((R - n) % 2)) # n이 1번째 일 때 +1, 3번째 일 때 -1
        for _ in range(n - 1): # (1, 0) or (-1, 0)
            di.append(1 - 2 * ((R - n) % 2)) # n이 2번째 일 때 +1, 4번째 일 때 -1
            dj.append(0)
    
    arr = [[0 for _ in range(R)] for _ in range(C)]

    i = j = 0
    for m in range(1, C * R + 1):
        if m == 1: # 최종값 1
            arr[i][j] = 1
        else:
            # 인덱스를 해당 위치로 이동 -> 값 순차적 대입
            i += di[m - 1]
            j += dj[m - 1]
            arr[i][j] = m

    return arr

C, R = int(input()).split()
K = int(input())
print(Snail(C, R, K))