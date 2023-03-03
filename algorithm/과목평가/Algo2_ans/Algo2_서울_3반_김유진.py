def robot(N, arr):
    # 로봇 이동 방향 - 순서대로 0(우), 1(하), 2(좌), 3(상)
    direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    # 방문 여부 표시 2차원 리스트
    visited = [list(0 for _ in range(N)) for _ in range(N)]
    # 이동 방향 담을 리스트 (중복 제외)
    result = []
    i, j = 0, 0

    for n in range(N * N): # 탐색구역 수 만큼 반복
        idx = arr[i][j] # 로봇 이동 방향 인덱스 할당 -> direction 인덱스로 활용
        ni = i + direction[idx][0] # 이동할 i 인덱스
        nj = j + direction[idx][1] # 이동할 j 인덱스
        if not result or result[-1] != idx: # 비어있을 때, 혹은 마지막 원소가 중복이 아닐 때
            result.append(arr[i][j]) # 이동 방향 push

        if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0: # 새로운 좌표가 범위 내이고, 방문하지 않았을 경우
            i = ni # 인덱스 갱신
            j = nj
            visited[ni][nj] = 1 # 방문 갱신

        else: # 막힐 때
            break # 반복문 종료

    return result

T = int(input())
for i in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = robot(N, arr)

    print(f'#{i}', *ans)

