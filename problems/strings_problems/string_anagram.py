# string anagram using list

s = 'anagram'
t = 'nagara'
li_t = []
for i in range(len(t)):
    li_t.append(t[i])
print(li_t)
for i in range(len(s)):
    if s[i] in li_t :
        flag = True
    else:
        flag = False
        break
print(flag)


# string panagrams - using sorted()-

s = 'listen'
t = 'silent'
if sorted(s) == sorted(t):
    print("anagrams")
else:
    print("not anagrams")

#string panagram using dictionary and check if the frequencies are same

s = 'car'
t = 'rat'
dict_s = {}
dict_t = {}
for i in s:
    if i in dict_s:
        dict_s[i] = dict_s[i] + 1
    else:
        dict_s[i] = 1
print(dict_s)

for j in t:
    if j in dict_t:
        dict_t[j] = dict_t[j] + 1
    else:
        dict_t[j] = 1
print(dict_t)

if dict_s == dict_t:
    print("anagrams")
else:
    print("not anagrams")
