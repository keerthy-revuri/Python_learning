def intersection(l2,l1):
    l3 = []
    for i in l1:
        if i in l2:
            l3.append(i)
    return l3

if __name__ == "__main__":

    l1 = [1,2,3,4,"Rupesh"]
    l2 = [1,2,3,"keerthy", "Rupesh"]

    if len(l2)<len(l1):
        print(f"smaller list is - {l2}, larger list is - {l1}")
        print(intersection(l2,l1))
    else:
        print(f"smaller list is - {l2}, larger list is - {l1}")
        print(intersection(l1,l2))



#logic 2

#Find common elements in two lists
l1 = [1,2,3,4,5,'Rupesh','loka']
l2 = [1,2,7,8,9,'Rupesh']
for i in range(len(l1)):
        if l1[i] in l2:
            print(l1[i])


#logic 3

l1 = [1,2,3,4,5,'Rupesh','loka']
l2 = [1,2,7,8,9,'Rupesh']
l3 = []
l3 = l1 + l2
print(l3)
for i in range(len(l3)):
    if l3[i] in l3[i+1:]:
        print(l3[i])