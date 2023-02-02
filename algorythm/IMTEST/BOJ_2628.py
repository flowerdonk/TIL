def Cut(x, y, cutN, cut_list):
    cut_x = [] # [4]
    cut_y = [] # [3, 2]

    for i in range(cutN): # 자르는 값들 x, y 끼리 리스트에 넣기
        if cut_list[i][0] == 0: # 가로로 자를 때
            cut_y.append(cut_list[i][1]) # y에 추가
        elif cut_list[i][0] == 1: # 세로로 자를 때
            cut_x.append(cut_list[i][1]) # x에 추가

    cut_x.sort(reverse=True) # 내림차순 정렬
    cut_y.sort(reverse=True)

    # 가장 긴 길이 초기값 = 양 끝에 자르기 직전까지 거리 중 긴 것
    big_x = x - cut_x[0] if x - cut_x[0] >= cut_x[-1] else cut_x[-1]
    big_y = y - cut_y[0] if y - cut_y[0] >= cut_y[-1] else cut_y[-1]

    # 자르는 선 사이의 거리 중 긴 것 찾기
    for i in range(len(cut_x) - 1):
        if big_x <= cut_x[i] - cut_x[i + 1]:
            big_x = cut_x[i] - cut_x[i + 1]

    for i in range(len(cut_y) - 1):
        if big_y <= cut_y[i] - cut_y[i + 1]:
            big_y = cut_y[i] - cut_y[i + 1]

    return big_x * big_y

x, y = map(int, input().split()) # 전체 종이 가로, 세로
cutN = int(input()) # 자를 점선의 개수
cut_list = []
for i in range(cutN):
    cut_list.append(list(map(int, input().split()))) # 가로 0, 세로 1 / 점선 번호

print(Cut(x, y, cutN, cut_list))