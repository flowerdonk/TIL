# sorted, get, join 활용
def group_anagrams():
    mid_result = []
    anas = list(input().split(','))
    result = {}

    # 입력받은 문자 리스트화
    for words in anas:
        mid_result.append(words.strip("'""[""]"" ")) # 띄어쓰기, [], '' 삭제

    for str in mid_result:
        s = ''.join(sorted(str)) # join 문자열 합치기
        result[s] = result.get(s, []) + [str] # 정렬된 문자를 key, 값을 빈 리스트

    print(list(result.values()))

group_anagrams()

# collections 사용
# def group_anagrams(strs: [str]) -> [[str]]:
#     anagrams = collections.defaultdict(list)
#     for word in strs:
#         anagrams[''.join(sorted(word))].append(word)
#     return anagrams.values()

# Str = ['eat','tea','tan','ate','nat','bat']
# print(group_anagrams(Str))

# 교수님 풀이
# word = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']

# def anagram(words):
#     anagrams = {}

#     for word in words:
#         key = ''.join(sorted(word))
#         anagrams.setdefault(key, []) # 각각의 키가 빈 리스트 값을 디폴트로 가지도록
#         anagrams[key].append(word)
#     result = list(anagrams.values())
#     return result

# print(anagram(word))