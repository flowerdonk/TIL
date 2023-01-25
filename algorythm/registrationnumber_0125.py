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