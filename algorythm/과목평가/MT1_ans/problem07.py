# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
def calculator(*numbers):
    pi = 3.14 # 파이 변수화
    number_list = list(numbers) # 입력값 리스트화 

    if len(number_list) == 0: # 0일 때,
        return 0 # 0 반환

    if len(number_list) == 1: # 원
        return number_list[0] ** 2 * pi # 넓이 반환

    if len(number_list) == 2:
        if not (number_list[0] + number_list[1]) % 2: # 사각형 
            return number_list[0] * number_list[1] # 넓이 반환
        else : # 삼각형
            return number_list[0] * number_list[1] / 2 # 넓이 반환

    else: # 입력 값 3개 이상
        return (sum(number_list), sum(number_list)/len(number_list)) # 합, 평균 반환



# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
########## 코드 변경 금지 ############
if __name__ == '__main__':
    print(calculator(5))                # 78.5
    print(calculator(10, 20))           # 200
    print(calculator(10, 20, 30, 40))   # (100, 25.0)
    print(calculator())                 # 0