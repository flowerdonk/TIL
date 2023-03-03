T = int(input())
for i in range(1, T + 1):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    student = []
    for n in range(1, N + 1):
        if n in arr:
            continue
        else:
            student.append(n)
    print(f'#{i}', *student)
