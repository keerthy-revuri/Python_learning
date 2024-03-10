#sets removes duplicate items
#output prints in different order everytime
CSE_courses = {'History', 'Math', 'English','English', 'CSE'}
ECE_courses = {'ECE', 'English'}
print(CSE_courses)
print('English' in CSE_courses)

print(CSE_courses.intersection(ECE_courses))
print(ECE_courses.difference(CSE_courses))
print(CSE_courses.union(ECE_courses))


#empty sets
empty_set = {} # This is not right, it is a dictionary
empty_set = set()