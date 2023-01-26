# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
# python 내장함수 min, max 사용 금지
def min_max(scores):
    min_score = 100 # 최소 점수
    max_score = 0 # 최대 점수

    for score in scores: # 리스트 원소 각각 확인
        if min_score > score: # 최소 점수보다 작은 경우
            min_score = score # 최소 점수 갱신
        
        if max_score < score: # 최대 점수보다 큰 경우
            max_score = score # 최대 점수 갱신

    return (min_score, max_score) # 튜플 리턴



# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
########## 코드 변경 금지 ############
if __name__ == '__main__':
    scores = [80, 90, 85, 75]
    print(min_max(scores))    # (75, 90)
