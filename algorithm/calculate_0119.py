def add(n, *m):
    return n + sum(list(m))

def sub(n, *m):
    return n - sum(list(m))

def mul(n, m):
    return n * m

def div(n, m):
    try:
       return n / m

    except ZeroDivisionError:
        print('0으로는 나눌 수 없습니다.')