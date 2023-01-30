pillarN = int(input()) # 기둥 갯수
store = [] * 1000 # 창고
input_pillar = [] # 기둥 L, H 리스트 저장 - 2차원 리스트
for i in range(pillarN):
    input_pillar.append(list(map(int, input().split())))

max_L = 0 # 최대 위치
max_H = 0 # 최대 높이 
max_H_idx = 0 # 최대 높이 인덱스
for i in range(pillarN): # 최대 위치 찾기
    max_L = max(max_L, input_pillar[i][0])

for i in range(pillarN): # 최대 높이, 인덱스 찾기
    if max_H <= input_pillar[i][1]:
        max_H = input_pillar[i][1]
        max_H_idx = input_pillar[i][0]

for i in range(1, max_L + 1): # 창고 리스트에 기둥 정보 담기
    count = 0
    for r in range(pillarN):
        if input_pillar[r][0] == i:
            store.insert(i, input_pillar[r][1])
            count += 1
            break
    
    if count == 0:
        store.insert(i, 0)

area = 0
big = 0
for i in range(max_H_idx): # 최대 높이까지
    if i < max_H_idx:
        if big < store[i]:
            big = store[i]
        area += big
    elif i == max_H_idx:
        area += max_H
    
big = 0
for i in range(max_L - max_H_idx): # 최대 높이 이후, 역순 계산
    if big < store[max_L - 1 - i]:
        big = store[max_L - 1 - i]
    area += big
    

print(area)
