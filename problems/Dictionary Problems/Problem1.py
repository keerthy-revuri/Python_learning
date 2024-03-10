#take 2 dictionaries with same keys, combine the values of those 2 keys in dictionaries into lists respectively
# and print another dictionary with combined lists as values

d1 = {'a':1, 'b':3}
d2 = {'a':2, 'b':4}
d3 = {}
#l1 = []

for i in d1:
    l1 = []
    l1.append(d1[i])
    l1.append(d2[i])
    d3[i] = l1
print(d3)


#combine (sum up ) values in 2 dictionaries having same key
from collections import Counter
d1 = {'a':1,'b':2,'c':3}
d2 = {'a':4,'b':5}
d3 = Counter(d1) + Counter(d2)
print(d3)