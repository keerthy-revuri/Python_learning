#Key - Value pair

Student = {'name' : 'John' , 'age' : 24 , 'courses' :['science' , 'math']}
print(Student['name'])
print(Student.get('phone')) #get method gives a default value to the not existing record instead of throwing error

Student['phone'] = 44789

print(Student.get('phone'))

Student.update({'name' : 'Jane' , 'result' : 'pass'})
print(Student)

del Student['age']
print(Student)
print (Student.items())
print(Student.keys())
print(Student.values())

for key, value in Student.items():
    print(key, value)

for key in Student.keys():
    print(f"key:{key}")

for value in Student.values():
    print(f"value:{value}")

for d in Student:
    print(d)
    print(Student[d])