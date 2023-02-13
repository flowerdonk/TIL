def game(N, r, c, arr):
    score = 0 # 획득 점수

    for n in range(N): # 두더지가 머리는 내미는 횟수만큼 반복

        A, B, K = arr[n][0], arr[n][1], arr[n][2] # 두더지 좌표 A, B, 머무는 시간 K

        if abs(r - A) + abs(c - B) <= K: # 두더지 위치까지 걸리는 시간이 K 범위 내 일 때
            c = B # 망치 좌표를 두더지 좌표로 이동
            r = A
            score += 1 # 점수 + 1

        else: # 두더지 위치까지 걸리는 시간이 K보다 적어 도달하지 못할 때

            if abs(c - B) >= K: # 가로 이동 거리가 K 보다 크면 -> 가로이동까지만

                if B < c: # 두더지 위치가 망치 위치보다 왼쪽에 있으면
                    c = c - K # c 위치 갱신

                else: # 두더지 위치가 망치 위치보다 오른쪽에 있으면
                    c = c + K # c 위치 갱신

            else: # 가로 이동 거리보다 K가 크면 -> 세로이동까지

                if A < r: #  두더지 위치가 망치 위치보다 위에 있으면
                    r = abs(c - B) - K + r # r 위치 갱신
                    c = B # c 위치 갱신

                else: #  두더지 위치가 망치 위치보다 아래에 있으면
                    r = K - abs(c - B) + r # r 위치 갱신
                    c = B # c 위치 갱신

    return score

T = int(input()) # 테스트 케이스 수
for i in range(1, T + 1): # 테스트 케이스 수 만큼 반복
    N = int(input()) # 두더지가 머리를 내미는 횟수
    r, c = map(int, input().split()) # 망치의 시작 위치
    arr = [list(map(int, input().split())) for _ in range(N)] # [[A, B, K], [...]]
    print(f'#{i} {game(N, r, c, arr)}')