# ord() - returns ascii for only alphabets

def check_pangram(str):
    li = []
    for i in range(26):
        li.append(False)
    for c in str.lower():
        if c != " ":
            print(c)
            print(ord(c) - ord('a'))
            li[ord(c) - ord('a')] =  True

    for ch in li:
        if ch == False:
            return False
    return True

#logic 3 if pangram has numbers

str = "The quick brown fox jumps over the little lazy dog"
if check_pangram(str):
    print("pangram")
else:
    print("not a pangram")
import re
str = "The quick brown fox jumps over the lazy dog2"
str = re.sub('[^a-z]','', str.lower())
set_value = set(str)
print(set_value)
l = len(set_value)
print(l)

if l == 26:
    print("pangram")
else:
    print("not pangram")



#logic 2

import string
#str = "The quick brown fox jumps over the lazy dog"
str = "abcdefghijklmnopq2"
flag = ''
alphabet_set = set(string.ascii_lowercase)
# for i in str:
#     print(i)
for j in alphabet_set:
    if j not in str:
        print(j)
        flag = False
        break
    else:
        flag = True

if flag == True:
    print("pangram")
else:
    print("not a pangram")



# logic 4
# A Python3 Program to check if the given
# string is a pangram or not
# Returns true if the string is pangram else false
def checkPangram(string):
    # Initialize a set of characters
    char_set = set()

    for ch in string:
        # If the character is already
        # a lowercase character
        if ch >= 'a' and ch <= 'z':
            char_set.add(ch)

        # In case of a uppercase character
        if ch >= 'A' and ch <= 'Z':
            # convert to lowercase
            ch = ch.lower()
            char_set.add(ch)

    # check if the size is 26 or not
    return len(char_set) == 26


# Driver Program to test above functions
string = "The quick rown fox jumps over the lazy dog"
if checkPangram(string) == True:
    print("It is a Pangram")
else:
    print("It is Not a Pangram")






