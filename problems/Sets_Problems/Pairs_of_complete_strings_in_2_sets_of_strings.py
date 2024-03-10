import string
s1 = {"abcdefgh", "geeksforgeeks", "lmnopqrst", "abc"}
s2 = {"ijklmnopqrstuvwxyz","abcdefghijklmnopqrstuvwxyz", "defghijklmnopqrstuvwxyz"}
n = len(s1)
m = len(s2)
#print(n,m)
#concatenated_set = set(list(s1) + list(s2))
#print(concatenated_set)
concatenated_list = []
count = 0
for i in s1:
    for j in s2:
        print(i+j)
        concatenated_list.append(i + j)

print(concatenated_list)
print(len(concatenated_list))

# alphabet_set = set(string.ascii_lowercase)
# print(alphabet_set)

count = 0

for str in concatenated_list:
    set1 = {}
    set1 = set(str)
    print(str)
    print(set1)
    print(len(set1))
    if len(set1) == 26:
        count = count +1

print(f"count is - {count}")


