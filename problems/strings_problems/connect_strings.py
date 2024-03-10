str1 = "hello. I live at valley forge suites"

list_of_strings =  ["together", "with", "my", "husband", "located", "at", "kop"]

output = "hello. I live at valley forge suites together with my husband located at kop"

str2 = ' '.join(list_of_strings)
print(str2)

print(str1 + str2)

str3 = ''
for word in list_of_strings:
    str3 = str3+' '+ word
print(str1 + str3)




