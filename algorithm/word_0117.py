# 끝말 잇기 (중복 X, 'done' 입력 시 중단)

words = ["round" , "dream", "magnet" , "tweet" , "tweet", "trick", "kiwi"]
history = []

for i in range(1, len(words)):
    if i == 1:
        history.append(words[0])

    if words[i] == 'done':
        print('끝말잇기 끝!')
        break

    if words[i][0] == words[i-1][-1]:
        if words[i] in history:
            print(f'same word! No.{i+1}')
            break
        else:
            history.append(words[i])
    
    else:
        print(f'incorrect! No.{i+1}')
        break


# 다른 방법

words = ["round" , "dream", "magnet" , "tweet" , "tweet", "trick", "kiwi"]
idx = 0
word_idx = len(words) - 1 # index는 0부터 시작하기 때문에

while idx < word_idx:
    idx += 1
    if words[idx - 1][-1] != words[idx][0] or words[idx] in words[:idx]:
        print(f'{idx + 1}번째 참가자가 탈락')
        break
    elif idx == word_idx: # 만약 아무도 탈락하지 않고 끝까지 진행
        print('아무도 탈락하지 않았다.')


# 함수로 작성

def word_relay():
    """
    끝말잇기 게임 함수
    함수 호출 시 게임이 시작된다
    사용자가 'done'을 입력하거나, 중복될 때 함수 종료
    """
    word_list = []
    idx = 1
    is_playing = True
    
    while is_playing:
        word = input('단어를 입력해주세요: ')

        # 입력받은 단어가 'done'이면 게임 종료
        if word == 'done':
            print('사용자에 의해 게임이 임의로 종료되었습니다.')
            is_playing = False

        # 첫 번째 단어가 입력됐을 때 그냥 단어 추가
        if not len(word_list):
            word_list.append(word)
            continue

        word_list.append(word)

        # 탈락자를 가려내는 조건
        if words[idx - 1][-1] != words[idx][0] or words[idx] in words[:idx]:
            print(f'{idx + 1}번째 참가자가 탈락')
            is_playing = False

        else: 
            idx += 1
            continue

word_relay()


        