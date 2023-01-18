# sorted, get, join 활용
def group_anagrams():
    mid_result = []
    anas = list(input().split(','))
    result = {}

    for words in anas:
        mid_result.append(words.strip("'""[""]"" "))

    for str in mid_result:
        s = ''.join(sorted(str)) # join 문자열 합치기
        result[s] = result.get(s, []) + [str] # 정렬된 문자를 key, 값을 빈 리스트

    print(list(result.values()))

group_anagrams()
