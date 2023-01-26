# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
def is_position_safe(N, M, position):
    game_end = True # 2차원 평면 범위를 벗어나는지 여부
    position = list(position) # 포지션 튜플 리스트화
    
    if M == 1: # 칸 이동이 아래일 경우
        position[0] += 1 # 포지션 x 좌표 +1
        if position[0] >= N: # 범위에서 벗어날 경우
            game_end = False

    elif M == 2: # 칸 이동이 왼쪽일 경우
        position[1] += -1 # 포지션 y 좌표 -1
        if position[1] < 0: # 범위에서 벗어날 경우
            game_end = False

    elif M == 3: # 칸 이동이 오른쪽일 경우
        position[1] += 1 # 포지션 y 좌표 +1
        if position[1] >= N: # 범위에서 벗어날 경우
            game_end = False

    else: # 칸 이동이 위일 경우
        position[0] += -1 # 포지션 x 좌표 -1
        if position[0] < 0: # 범위에서 벗어날 경우
            game_end = False

    return game_end


# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
########## 코드 변경 금지 ############
if __name__ == '__main__':
    print(is_position_safe(3, 0, (0, 1)))  # True
    print(is_position_safe(3, 1, (2, 1)))  # False
