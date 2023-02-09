import sys
sys.stdin = open('input.txt')

def Ladder(arr, L):
    firstLine = []
    for x in range(len(arr[0])):
        if arr[0][x] == 1:
            firstLine.append(x)  # 시작점 좌표 담기

    keep_x = 0
    keep_y = 0
    minN = L * L
    minX = 0

    for start in firstLine:  # 시작점 하나씩 반복
        keep_x = start  # 시작점 저장
        y = 0
        x = firstLine.index(start)  # 시작점 x 인덱스
        cnt = 0  # 꺾은 수

        while x <= len(firstLine) - 1:
            if y == L - 1:  # 마지막 줄
                if L + cnt < minN:
                    minX = start
                    minN = L + cnt
                    print(minN)
                    print(minX)
                    # y = 0
                break


            else:
                if x != len(firstLine) - 1 and arr[y][firstLine[x] + 1] == 1:  # 오른쪽 길
                    keep_y = y  # y좌표 저장
                    x += 1  # x 전 값으로
                    y += 1
                    cnt += firstLine[x] - firstLine[x - 1]
                    continue  # 다음 x좌표로
                elif x != 0 and arr[y][firstLine[x] - 1] == 1:  # 왼쪽 길
                    keep_y = y  # y좌표 저장
                    x -= 1
                    y += 1
                    cnt += firstLine[x + 1] - firstLine[x]
                    continue
                else:
                    y += 1

    return minX


L = 100
T = 10
for _ in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(L)]
    print(f'#{N} {Ladder(arr, L)}')
