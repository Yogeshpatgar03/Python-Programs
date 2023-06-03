def is_palindrome(word):
    reversed_word = word[::-1]
    if word == reversed_word:
        return True
    else:
        return False

word = input("Enter a word: ")
if is_palindrome(word):
    print("It is a palindrome.")
else:
    print("It is not a palindrome.")