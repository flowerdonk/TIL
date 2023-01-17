# 메뉴 중복 체크 및 내림차순 정렬
orders = '아이스아메리카노,카라멜마키야또,에스프레소,아메리카노,아메리카노,아이스라떼,핫초코,아이스아메리카노,아메리카노,아이스카라멜마키야또,아이스라떼,라떼마키야또,카푸치노,라떼마키야또'

orders = list(set(orders.split(',')))
orders.sort(reverse=True)
print(orders)


# 메뉴 주문 수량 및 아이스 개수
orders = '아이스아메리카노,카라멜마키야또,에스프레소,아메리카노,아메리카노,아이스라떼,핫초코,아이스아메리카노,아메리카노,아이스카라멜마키야또,아이스라떼,라떼마키야또,카푸치노,라떼마키야또'
menu_number = dict()
ice_number = 0

orders = list(orders.split(','))

for menu in orders:
    if menu in menu_number:
        menu_number[menu] += 1
    else:
        menu_number[menu] = 1

for ice in orders:
    if '아이스' in ice:
        ice_number += 1

print(f'아이스음료는 {ice_number}개 입니다.')
print(menu_number)