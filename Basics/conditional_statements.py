language = "python"
if language == "python":
    print("it is a match")
elif language == "Java":
    print("language is Java")
elif language == "Java Script":
    print("language is Java Script")
else:
    print("it is not a match")



# Comparisons:
# Equal:            ==
# Not Equal:        !=
# Greater Than:     >
# Less Than:        <
# Greater or Equal: >=
# Less or Equal:    <=
# Object Identity:  is



a = [1,2,3]
b = [1,2,3]
print(id(a)) # address of memory block
print(id(b))
print(a==b)
print(a is b)

a =  [1,2,3]
b = a
print(id(a))
print(id(b))
print(a==b)
print(a is b)

# False Values:
    # False
    # None
    # Zero of any numeric type
    # Any empty sequence. For example, '', (), [].
    # Any empty mapping. For example, {}.

condition = ''
if condition:
    print("evaluated is True")
else:
    print("Evaluated is False")

