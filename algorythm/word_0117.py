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