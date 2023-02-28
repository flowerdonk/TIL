'''
별자리가 나오는 범위 안에서 최대로 확대
한 번 확대 시 K - 2, K >= 1
'''

T = int(input())
for tc in range(1, T + 1):
    # N : 전체 하늘의 한 쪽 길이, K : 최대 영역 한 쪽 길이, (A, B) : 초점
    N, K, A, B = map(int, input().split())
    data = [list(input().split()) for _ in range(N)]
    zoom = 0
    stars = [] # 별 위치 담기
    stars_r = [] # 별 위치 i, j 위치 바꿔서 담기 -> 정렬 후 최소, 최대값 찾기 위함

    for i in range(N): # 별 위치 찾기
        for j in range(N):
            if 0 <= i < N and 0 <= j < N and data[i][j] == '*':
                stars.append([i, j]) # [i, j] 담기
                stars_r.append([j, i]) # [j, i] 담기

    stars.sort()
    stars_r.sort()
    mx_i, mn_i = stars[-1][0], stars[0][0] # 최대, 최소 i값
    mx_j, mn_j = stars_r[-1][0], stars_r[0][0] # 최대, 최소 j값

    final_i = final_j = 0 # 기준점부터 별이 있는 최대 길이
    if abs(A - mn_i) >= abs(A - mx_i): # 기준점 - 최대 최소 i 비교
        final_i = abs(A - mn_i)
    else:
        final_i = abs(A - mx_i)

    if abs(B - mn_j) >= abs(B - mx_j): # 기준점 - 최대 최소 j 비교
        final_j = abs(B - mn_j)
    else:
        final_j = abs(B - mx_j)

    num_i = K // 2 - final_i # 최대 영역 - 기준점에서의 거리
    num_j = K // 2 - final_j

    if mx_i > A + K // 2 or mn_i < A - K // 2 or mx_j > B + K // 2 or mn_j < B - K // 2: # 망원경 시야 내 인지 확인
        result = -1
    elif num_i == 0 and num_j == 0: # 둘 다 0이면 확대 X
        result = 0
    else:
        if num_i >= num_j: # 기준점에서 거리가 더 큰 것을 전체 영역에서 빼기
            result = K // 2 - num_i
        else:
            result = K // 2 - num_j

    print(f'#{tc} {result}')