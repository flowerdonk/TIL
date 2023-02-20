import sys
sys.stdin = open('input.txt')

def fly(N, M, arr):
    result = []
    direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    for i in range(N - M + 1):
        for j in range(N - M + 1):
            mx = arr[i][j] # 파리 수 총합
            idx = cnt = 0 # 방향 인덱스, 이동 카운트
            si, sj = i, j # 현재 인덱스 저장
            visited = [[0] * N for _ in range(N)] # 매번 방문한 인덱스 확인
            visited[i][j] = 1 # 시작점 인덱스 방문 표시
            while cnt != M * M - 1: # 이동 카운트가 파리채 크기까지
                ni = si + direction[idx][0] # 이동할 방향
                nj = sj + direction[idx][1]
                if i <= ni < i + M and j <= nj < j + M and visited[ni][nj] == 0: # 파리채 크기 내, 방문하지 않았다면
                    mx += arr[ni][nj] # 총합 추가
                    si = ni # 위치 저장
                    sj = nj
                    cnt += 1 # 이동한 수
                    visited[ni][nj] = 1 # 방문
                else:
                    idx = (idx + 1) % 4 # 방향 변경

            result.append(mx) # 총합 리스트에 삽입

    return max(result)

T = int(input())
for i in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    print(f'#{i} {fly(N, M, arr)}')