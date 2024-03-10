# Given a string s consisting of words and spaces, return the length of the last word in the string.
# A word is a maximal
# substring consisting of non-space characters only

# Example 1:
# Input: s = "Hello World"Output: 5
# Explanation: The last word is "World" with length 5.

#logic 1 using while loop
s = "Hello mike "
len_s = len(s)-1
counter =0

while s[len_s]==' ':
    len_s = len_s - 1

while s[len_s]!=' ':
    counter = counter+1
    len_s = len_s -1
    print(counter)

print("solution")
print(counter)

#logic 2 - for loop

s = "Hello Worl   "
o_list =[]
o_list = s.split(' ')

n = len(o_list)

print(o_list)

for i in range(n-1, -1, -1):
    if o_list[i] == '':
        continue

    else:
        print(f"solution is {len(o_list[i])}")
        break








