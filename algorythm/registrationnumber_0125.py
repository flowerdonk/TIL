def de_identify(numbers):
    numbers = ''.join(list(numbers.split('-')))
    if not numbers.isdigit():
        return '잘못된 입력'
    elif len(numbers) != 13:
        return '잘못된 입력'
    else:
        result = ''
        for num in range(len(numbers)):
            if num <= 5:
                result += numbers[num]
            else:
                result += '*'


    return result

final = de_identify(input("주민번호 입력 : "))
print(f'비식별화 결과 : {final}')

# 교수님 풀이

def de_identify(social_number):
    social_number = social_number.replace('-', '')
    # 문자열 슬라이싱 이용
    return social_number[:-7] + '****'

print(de_identify('970103-1234567'))

def de_identify_with_list(social_number, slicing_num):
    # '-'를 ''로 대체
    social_number = social_number.replace('-', '')
    str_list = list(social_number)
    str_list[-slicing_num:] = "****"
    return ''.join(str_list)

print(de_identify_with_list('970103-1234567', 7))