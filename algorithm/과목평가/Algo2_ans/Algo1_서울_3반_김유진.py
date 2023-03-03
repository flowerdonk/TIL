def mountain(N, hi):
    top = []

    # 시계방향
    direction = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]

    for i in range(1, N - 1): # hi 세로 판별, 가장자리 제외
        for j in range(1, N - 1): # 가로
            mx = hi[i][j] # 최댓값 초기화 = 기준점, 즉 가운데
            samecnt = 0 # 기준점과 동일할 경우 판별

            for d in direction: # 방향 내 순회, 8개의 방향 확인
                if hi[i + d[0]][j + d[1]] >= mx: # 최댓값 갱신 기준
                    mx = hi[i + d[0]][j + d[1]] # 최댓값 갱신
                    if mx == hi[i][j]: # 만약 기준점과 최댓값이 같다면
                        samecnt += 1

            if mx != hi[i][j] or samecnt > 0: # 최댓값이 기준점이 아니거나, 기준점과 동일한 경우가 있었을 때
                continue
            else: # 최댓값이 기준점일 때
                top.append(mx)

    if not len(top) >= 2: # 봉우리를 모아둔 리스트가 1 이하일 때
        return -1

    return (max(top) - min(top))

T = int(input())
for i in range(1, T + 1):
    N = int(input())
    hi = [list(map(int, input().split())) for _ in range(N)]

    print(f'#{i} {mountain(N, hi)}')