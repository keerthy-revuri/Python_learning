#reverse words in a given string
#Note - reverse words in a given string , then reverse the whole string
#str -> list -> reverse the individual words and store in another list - > str -> reverse the string

#reverse words in a given string

str = "i love to code"
temp = str.split(' ')
print(temp)
temp_1 = []
for word in temp:
    temp_string = ''
    word_index = len(word) - 1
    while word_index >=0:
        temp_string = temp_string + word[word_index]
        word_index = word_index -1
    temp_1.append(temp_string)
print(temp_1)

str = ' '.join(temp_1)
print(str)
str2 = ''
str_index = len(str) - 1
while str_index >= 0:
    str2 = str2 + str[str_index]
    str_index = str_index - 1
print(str2)






