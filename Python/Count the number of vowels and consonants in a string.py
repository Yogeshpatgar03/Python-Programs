def count_vowels_consonants(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowel_count = 0
    consonant_count = 0
    for letter in word.lower():
        if letter in vowels:
            vowel_count += 1
        elif letter.isalpha():
            consonant_count += 1
    print("Number of vowels:", vowel_count)
    print("Number of consonants:", consonant_count)

word = input("Enter a word: ")
count_vowels_consonants(word)