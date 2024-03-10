# str1 = "madam"
#
# if str == str[::-1]:
#     print("palindrome")
# else:
#     print('not a palindrome')


#logic 2
str1 = "hello"
temp =[]
str2 =''
for i in range(len(str1)-1, -1, -1):
    temp.append(str1[i])
    str2 = ''.join(temp)
#print(str2)
if str1 == str2:
    print(f"{str1} and {str2} are palindromes")
else:
    print(f"{str1} and {str2} are not palindromes")

#logic3 - without using in built functions


str1 = "radar"
str2 = ''
for i in range(len(str1)-1,-1,-1):
    #print (str1[i])
    str2 = str2 + str1[i]
print (str2)
if str1 == str2 :
    print(f"{str1} is a palindrome")
else:
    print(f"{str1} is not a palindrome")


