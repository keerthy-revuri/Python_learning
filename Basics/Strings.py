#to check if 2 strings are isomorphic

Profile = {'name':'Rupesh', 'age' : 29}
#Profile.update({'phone':'9803659852'})
temp ={'phone':'9803659852'}
Profile.update(temp)
#del Profile['age']
x = Profile.pop('age')

# print(Profile.items())
# Profilefor key in Profile.items():
#     print(key)

# for key, value in Profile.items():
#     print(f"key:{key}, value:{value}")

for d in Profile:
    print(Profile[d])


message = "Hello"
print(message[::-1])
n= len(message)
for m in range(n-1, -1 , -1):
    print(message[m])


