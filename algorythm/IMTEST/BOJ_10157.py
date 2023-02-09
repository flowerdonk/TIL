def Seat(C, R, K):

    if K > C * R:
        return 0
    # 이동 오른쪽, 아래, 왼쪽, 위
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    arr = [[0 for _ in range(C)] for _ in range(R)]
    i, j = 0, 0 # 현재 좌표
    arr[i][j] = 1 # 첫 번째 대기 순서
    idx = 0 # 이동방향 인덱스

    for n in range(2, K + 1):
        while True: # 이동 가능하면 이동, 불가능하면 방향 전환
            ni = i + di[idx] # 가고자 하는 위치
            nj = j + dj[idx]

            if 0 <= ni < R and 0 <= nj < C and arr[ni][nj] == 0:
                arr[ni][nj] = n
                i = ni
                j = nj
                break
            else:
                idx = (idx + 1) % 4

    return (i + 1, j + 1)

R, C = map(int, input().split())
K = int(input())
print(Seat(C, R, K))