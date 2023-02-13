# stack = [0] * 3
# top = -1
#
# top += 1
# stack[top] = 10
#
# top += 1
# stack[top] = 20
#
# top += 1
# stack[top] = 30
#
# top -= 1
# print(stack[top + 1])
#
# top -= 1
# print(stack[top + 1])
#
# top -= 1
# print(stack[top + 1])
#
# top -= 1
# print(stack[top + 1])

# 1️⃣ 문자열에 있는 괄호 차례대로 조사
# 왼쪽 괄호 → 스택에 삽입
# 오른쪽 괄호 → 스택에서 top 괄호 삭제 후 오른쪽 괄호와 짝이 맞는지 검사
#
# 2️⃣ 이 때, 스택이 비어있으면 조건 1 또는 조건 2에 위배
# 괄호의 짝이 맞지 않으면 조건 3에 위배
#
# 3️⃣ 마지막 괄호까지 조사
# 스택에 괄호가 남아있으면 조건 1에 위배

def bracket(bracs):
    stack = []
    for i in range(len(bracs)):
        if bracs[i] == '(':
            stack.append(bracs[i])
        elif bracs[i] == ')':
            if len(stack) == 0:
                print('빈 스택')
                return -1

            if stack.pop() == '(':
                continue
            elif stack.pop() != '(':
                print('선행관계 오류')
                return -1
        else:
            print('잘못된 입력!')
            return

    if len(stack) != 0:
        return -1
    return 1

T = int(input())
for i in range(1, T + 1):
    bracs = input()
    print(f'#{i} {bracket(bracs)}')