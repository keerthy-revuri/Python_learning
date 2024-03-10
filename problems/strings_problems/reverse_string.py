message = "Hello"
print(message[::-1])
n= len(message)

#logic2 - reverse string using for loop

str = 'heaven'
str2 = ''
n = len(str)
for letter in range(n-1, -1 , -1): # range can be used in strings also, here in strings as 2nd index is exclusive -1 is used
    str2 = str2 + str[letter]
print(str2)


#logic3 - reverse string using while loop

str = "happy"
str2 = ''
word_index = len(str) -1
while word_index >= 0:
    str2 = str2 + str[word_index]
    word_index = word_index - 1
print(str2)



