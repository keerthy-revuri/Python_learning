def hello_function():
    return "Hello Function" #an executed function is equal to the RETURN value

res = hello_function()
print(res)
res = hello_function().upper()
print(res)



# passing arguments
def hello_function(greeting, name):
    return f"{greeting} {name}"

result = hello_function("hi", "Keerthy")
print(result)

#positional arguments

def student_info(*args, **kwargs): # *args is tuple, **kwargs is dictionary, holds the values passed during function call
    print(args)
    print(kwargs)
courses = ['Math', 'Art']
info = {'name': "Rupesh", 'age': 29}

student_info(courses , info) #doesn't pass the value as expeccted
student_info(*courses, **info) # unpacks the values and will pass list and dictionary individually
