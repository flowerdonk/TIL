# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
# python 내장함수 len 사용 금지
def title_length(movie):
    count = 0 # 글자수 확인 변수
    for letter in movie["title"]: # 딕셔너리 내부 제목의 값(스트링)의 글자 각각 확인
        count += 1 # 글자 수 만큼 더해지는 수

    return count



# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
########## 코드 변경 금지 ############
if __name__ == '__main__':
    movie = {
            "id": 1,
            "user_rating": 8.1,
            "title": "그리고 내일",
            "overview": "과거보다 더 성장한 당신은 드디어 꿈을 이루게 된다.",
        }

    print(title_length(movie))  # 6 (공백 포함 길이)