def collatz(num):
    turn = 0

    while num != 1:
        if num % 2: # 홀수
            num = num * 3 + 1

        else: # 짝수
            num /= 2
        turn += 1

        if turn >= 500:
            return -1

    return turn


print(collatz(6)) #=> 8
print(collatz(16)) #=> 4
print(collatz(27)) #=> 111
print(collatz(626331)) #=> -1