# fn_d(91), 101의 제너레이터

'''
def is_selfnumber(n):
    # 주어진 범위 내에서 반복, 제너레이터를 하나 이상 가지고 있는 경우 False 반환
    for m in range(1, n + 1):
        fn_d = lambda n : sum([int(i) for i in str(n)] + [n])
        # def fn_d(n): # 람다 함수와 동일한 함수
        #     n_list = [int(i) for i in str(n)]
        #     n_list.append(n)
        #     return sum(n_list)
        if fn_d(m) == n:
            return False
    return True
'''

def is_selfnumber(n):
    for m in range(1, n + 1):
        fn_d = lambda n : sum([int(i) for i in str(n)] + [n])
        if fn_d(m) == n:
            return False
    return True