def find_first_palindrome(word_list):
    for word in word_list:
        l = 0
        r = len(word) - 1
        while word[l] == word[r]:
            if l >= r:
                #print(f"{word}, l -{l} - {word[l]}, r- {r} - {word[r]}")
                return word
            l = l + 1
            r = r - 1
    return " "

word_list = ['fgkf','adkda','radar','def']
res = find_first_palindrome(word_list)
print(res)