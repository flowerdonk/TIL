def stamp(N, M, arr):
    board = [[0 for _ in range(N)] for _ in range(N)] # N x N 도화지 이차원 리스트
    ans = 0 # 도장이 칠해진 갯수, 리턴값
    # 문제에서 도장의 색상, 겹친 정도는 중요하지 않음 - 전체 넓이만 구하면 됨

    for n in range(M): # 도장 찍은 횟수 만큼 반복, 도장 하나씩 확인
        x, y, w, h = arr[n][0], arr[n][1], arr[n][2], arr[n][3] # 도장 한 번의 행, 열, 높이, 좌표
        for x_ in range(x, x + h): # 행 시작, 행 + 높이까지
            for y_ in range(y, y + w): # 열 시작, 열 + 너비까지
                board[x_][y_] = 1 # 0 -> 1로 바꿈

    for i in range(N): # board 원소 검사, 행
        for j in range(N): # board 원소 검사, 열
            if board[i][j] == 1: # 1로 바뀌었다면 -> 도장이 찍혔다면
                ans += 1 # +1

    return ans

T = int(input()) # 테스트 케이스 수
for i in range(1, T + 1): # 테스트 케이스 수 만큼 반복
    N, M = map(int, input().split()) # N = 도화지의 크기, M = 도장을 찍은 횟수
    arr = [list(map(int, input().split())) for _ in range(M)] # [[왼쪽 모서리 좌표 행, 열, 너비, 높이], [...]]
    print(f'#{i} {stamp(N, M, arr)}')
