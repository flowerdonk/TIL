sum_h = []
bad = []

for i in range(9): # 입력 수 리스트에 담기
    sum_h.append(int(input()))
bad_hs = sum(sum_h) - 100 # 총합 - 100
sum_h.sort() # 정렬

for i in range(5): # 절반까지만 확인
    another = bad_hs - sum_h[i] # 100과의 차이 - 원소값
    if sum_h.count(another) == 1: # 두 원소의 합 = 100과의 차이
        sum_h.remove(sum_h[i]) # 해당 인덱스 값 삭제
        sum_h.remove(another)
        break

for i in range(7): # 출력
    print(sum_h[i])