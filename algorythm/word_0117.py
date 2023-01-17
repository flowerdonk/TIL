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

