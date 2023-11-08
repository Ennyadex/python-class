def palindrome(word):
    rev_word = "".join(reversed(word))
    if word == rev_word:
        print("this is a palindrome")
    else:
        print("this is not a palindrome")
word = input("enter any word: ")
palindrome(word)