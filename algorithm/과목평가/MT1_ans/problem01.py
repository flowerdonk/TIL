# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
def average(scores):
    avg = 0 # 평균 값을 담을 변수
    avg = sum(scores)/len(scores) # 점수 총합 / 점수 갯수
    return avg # 평균 값 리턴


# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
########## 코드 변경 금지 ############
if __name__ == '__main__':
    scores = [80, 90, 85, 75]
    print(average(scores))    # 82.5