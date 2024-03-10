
def palindrome_num(n):
    rev = 0
    while n>0:
        rem = n%10
        rev = rev*10 + rem
        n = n//10
    if rev == num:
        return "is a palindrome"
    else:
        return "is not a palindrome"

num = 132
res = palindrome_num(num)
print(res)