def Turn(num): # 스위치 키고 끄는 함수
    if switches[num] == 0:
        switches[num] = 1
    else:
        switches[num] = 0
    return

total = int(input())
switches = [-1] + list(map(int, input().split())) # 0 인덱스 채우기
member = int(input())

for i in range(member):
    x, y = map(int, input().split()) # 성별, 위치
    if not 1 <= y <= total: # 위치가 범위 내 인지 확인
        break

    if x == 1: # 남자일 경우
        Turn(y)
        Turn(y * 2)
    else: # 여자일 경우
        Turn(y)
        for i in range(total // 2): # 최대 전체의 절반
            if y + i > total or y - i < 1 : break # 범위 벗어나면 break
            if switches[y - 1 - i] == switches[y + 1 + i]: # 앞, 뒤 비교
                Turn(y - 1 - i) # 같으면 변경
                Turn(y + 1 + i) # 같으면 변경
            else:
                break # 같지 않을 때 break

for i in range(1, total+1): # 출력
    print(switches[i], end = ' ')
    if i % 20 == 0: # 20개 까지
        print()