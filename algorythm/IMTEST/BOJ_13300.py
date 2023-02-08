def Room(N, K, arr):
    grade = [[0, 0] for _ in range(6)]
    # N = 학생 수, K = 최대 방 인원, [S = 성별, Y = 학년]
    for i in range(N): # 학년으로 구별
        S = arr[i][0]
        Y = arr[i][1]

        grade[Y - 1][S] += 1

    room = 0
    for i in range(6):
        room += grade[i][0] // K # 여자
        if grade[i][0] % K:
            room += 1

        room += grade[i][1] // K # 남자
        if grade[i][1] % K:
            room += 1

    return room

N, K = map(int, input().split())
arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))

print(Room(N, K, arr))