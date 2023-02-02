def Baby_gin(Number):
    judge = 0
    run = 0
    triplet = 0
    idx = 0
    count = [0] * 10

    for letter in Number:
        count[letter] += 1

    while idx < 10: # continue로 빠져나오면 idx가 증가하지 X
        if count[idx] >= 3:
            count[idx] -= 3
            triplet += 1
            continue
        if count[idx] >= 1 and count[idx + 1] >= 1 and count[idx + 2] >= 1:
            count[idx] -= 1
            count[idx + 1] -= 1
            count[idx + 2] -= 1
            run += 1
            continue
        idx += 1

    if run + triplet == 2:
        judge = 1

    return judge

T = int(input()) # 테스트 케이스 수

Numbers = [] # 숫자 리스트-리스트

for i in range(T):
    Numbers.append(list(map(int, list(input()))))

for i in range(T):
    judge_ = Baby_gin(Numbers[i]) # 인풋 그룹 하나씩 전달
    print(f'#{i + 1} {judge_}')