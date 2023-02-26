# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
def caesar(word, n):
    new_word = '' # 변경된 시저 암호를 담을 스트링 변수(완성된 단어)

    for letter in word: # 전달된 단어의 각각의 문자 확인
        up_letter = False # 대문자 여부
        new_code = ord(letter) + n # 변경될 아스키 코드
        new_letter = '' # 변경될 문자

        if letter.isupper(): # 대문자 일 경우
            up_letter = True # 대문자 여부 변수 값 변경


        if up_letter: # 대문자일 경우
            if new_code > 90: # 새로운 아스키 코드가 범위에서 벗어나면
                new_code -= 26 # 다시 처음으로 돌아가 남은 범위만큼 계산

        else: # 소문자일 경우
            if new_code > 122: # 새로운 아스키 코드가 범위에서 벗어나면
                new_code -= 26 # 다시 처음으로 돌아가 남은 범위만큼 계산

        new_letter = chr(new_code) # 아스키코드 문자화
        new_word += new_letter # 변경된 문자 스트링에 추가

    return new_word




# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
########## 코드 변경 금지 ############
if __name__ == '__main__':
    print(caesar('vwxyz', 5))
