# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
# 반드시 재귀함수로 구현해야 합니다.
def dec_to_bin(number):

    if number <= 1: # number가 2로 더이상 나눠지지 않을 때
        return str(number) # number를 스트링화 해서 반환

    else : 
        if number % 2 == 0: # 나머지 0
            return dec_to_bin(number//2) + '0' # 재귀 호출 후, 0 출력
        else: # 나머지 1
            return dec_to_bin(number//2) + '1' # 재귀 호출 후, 1 출력



# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
########## 코드 변경 금지 ############
if __name__ == '__main__':
    print(dec_to_bin(10))  # 1010
    print(dec_to_bin(5))   # 101
    print(dec_to_bin(50))  # 110010
