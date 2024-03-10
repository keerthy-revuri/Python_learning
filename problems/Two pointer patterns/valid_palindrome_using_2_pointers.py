# string palindrome using 2 pointers

def str_palindrome(str):
    l = 0
    r = len(str) - 1
    while l < r:
        if str[l] != str[r]:
            return False
        l = l + 1
        r = r - 1
    return True

str = "radxr"
res = str_palindrome(str)
print(res)


#logic 2
def str_palindrome(word):
    l = 0
    r = len(word) - 1
    while word[l] == word[r]:
        if l >= r:
            print(f"{word}, l -{l} - {word[l]}, r- {r} - {word[r]}")
            return word
        l = l + 1
        r = r - 1
    return " "

word = "radar"
res = str_palindrome(word)
print(res)


