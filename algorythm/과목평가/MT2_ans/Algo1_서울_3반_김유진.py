'''
사각형 정원에 세로 줄로 나무 심기
나무는 한 줄씩 띄어서
나무 총 비용, 나무의 수,
가장 비싼 나무의 가격, 해당 나무의 열 번호 계산(여러 개 일 경우 가장 큰 열의 번호)
'''

T = int(input()) # 테스트 케이스 개수
for tc in range(1, T + 1):
    N, M = map(int, input().split()) # 정원의 크기, N : 행의 개수(가로), M : 열의 개수(세로)
    data = [list(map(int, input().split())) for _ in range(N)] # 나무 가격
    cost = n_tree = mx = mx_idx = 0 # '총 비용' '나무 수' '가장 비싼 나무 가격' '해당 나무의 열'

    for i in range(N) : # 행 순회
        for j in range(0, M, 2): # 열 순회
            cost += data[i][j] # 가격 추가
            n_tree += 1 # 개수 추가
            if data[i][j] >= mx: # 최댓값과 비교
                if data[i][j] == mx: # 같다면
                    if j >= mx_idx: # 열이 더 큰 숫자라면
                        mx = data[i][j] # 갱신
                        mx_idx = j
                    else: # 열이 더 작은 숫자라면
                        continue # 넘어감
                else: # 크다면
                    mx = data[i][j] # 갱신
                    mx_idx = j


    # 출력 : #tc '총 비용' '나무 수' '가장 비싼 나무 가격' '해당 나무의 열'
    print(f'#{tc} {cost} {n_tree} {mx} {mx_idx + 1}')