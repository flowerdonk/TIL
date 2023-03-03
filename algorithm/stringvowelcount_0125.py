def count_vowels(word):
    count = 0
    vowels = ['a', 'e', 'i', 'o', 'u']

    for letter in word:
        for vowel in vowels:
            if letter == vowel:
                count += 1
    
    return count


print(count_vowels('apple')) #=> 2
print(count_vowels('banana')) #=> 3

# 교수님 풀이

def count_vowels2(word):
    """
    모음의 갯수를 반환
    """
    vowels = 'aeiou' # 문자열도 iterable -> 인덱스로 요소 접근 가능
    result = 0

    for vowel in vowels: # 모음의 한 글자씩 비교
        result += word.count(vowel)
    
    return result

print(count_vowels2('apple')) #=> 2
print(count_vowels2('banana')) #=> 3