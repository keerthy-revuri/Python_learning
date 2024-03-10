# for loops iterate through certain number of values

nums = [1,2,3,4,5]
for num in nums:
    if num == 3:
        print("Found!")
       # break
        #continue
    print(num)

for num in nums:
    for letter in "abc":
        print(num, letter)


#while loops iterate until a condition is met
x = 0
while x<10:
    if x == 5:
        break
    print(x)
    x+=1
