T = int(input())

for k in range(T):
    N = input()
    save = []
    rst = ''
    for i in range(len(N)):
        save.append(ord(N[i]))

    for j in range(len(save)):
        rst += chr(save[j])

    print(f'#{k + 1}', rst, type(rst))