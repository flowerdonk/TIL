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