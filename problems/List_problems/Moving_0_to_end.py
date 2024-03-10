a = [0,56,5,0,9]
n = len(a)
new_list = []
for i in a:
    if i == 0:
        a.remove(i)
        new_list.append(i)
#a.append(new_list)
a.extend(new_list)
print(a)

#logic2

a = [0,56,5,0 ,9,0,0,8]
n = len(a)
a1=[]
for i in a:
    if i != 0:
        a1.append(i)
for i in range(len(a) - len(a1)):
    a1.append(0)
print(a1)
