a = [5,8,12,56]
b = [7,9,45,51]
c = []
i = j = 0
while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            c.append(a[i])
            print(f"i is - {i}, c is - {c}")
            i = i + 1
        else:
            c.append(b[j])
            print(f"j is - {j}, c is - {c}")
            j = j + 1
while i < len(a):
    c.append(a[i])
    i = i + 1
    print(f"separate while , i value - {i}, c - {c}")
while j < len(b):
    c.append(b[j])
    j = j + 1
    print(f"separate while , j value - {j}, c - {c}")
print(c)