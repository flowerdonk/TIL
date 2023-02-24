infix = '(6 + 5 * (2 - 8) / 2)'
stack = []
result = ''

# 변환할 식을 순회
for token in infix:
    # 토큰이 피연산자일 경우
    if token.isdecimal():
        result += token

    # 토큰이 연산자일 경우
    else:
        # stack이 비어있는 경우, stack에 push
        if not stack: # if len(stack) == 0
            stack.append(token)

        else:
            # (는 incoming 우선순위가 가장 높음
            if token == '(':
                stack.append(token)
            # )는 (가 나올때까지 stack에서 pop, result에 append
            elif token == ')':
                while stack[-1] != '(':
                    result += stack.pop()
                stack.pop()
            
            # incoming 우선순위가 2인 경우
            elif token == '*' or token == '/':
                # stack의 top의 토큰이 우선순위가 낮을 때까지 stack pop, result append
                while stack and stack[-1] == '*' or stack[-1] == '/':
                    result += stack.pop()
                stack.append(token)

            # incoming 우선순위가 1인 경우
            elif token == '+' or token == '-':
                # stack의 top의 토큰이 우선순위가 낮을 때까지 stack pop, result append
                # (가 아닌 경우, 모두 동치
                while stack and stack[-1] != '(':
                    result += stack.pop()
                stack.append(token)

while stack:
    result += stack.pop()

print(result) # 6528-*2/+

'''
계산하기

1. 피연산자
    stack에 push

2. 연산자
    stack에 담겨있는 2개의 토큰을 pop 후 연산 후 stack에 push
'''