def Turn(num):
    if switches[num-1] == 0:
        switches[num-1] = 1
    else:
        switches[num-1] = 0
    return

total = int(input())
switches = list(map(int, input().split()))
member = int(input())

for i in range(member):
    x, y = map(int, input().split())
    
    if x == 1:
        Turn(y)
        Turn(y * 2)
    else:
        Turn(y)
        for i in range(total // 2):
            if y + i > total or y - i < 1 : break
            if switches[y - 2 - i] == switches[y + i]:
                Turn(y - 1 - i)
                Turn(y + 1 + i)
            else:
                break

for i in range(1, total+1):
    print(switches[i], end = ' ')
    if i % 20 == 0:
        print()