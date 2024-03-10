
# Lists are mutable

courses = ['Math', 'Physics', 'Comp sci', 'Biology']
print(courses[-1]) # -1 index gives last item from the list
print(courses[0:2]) # 1st index is inclusive , 2nd index is exclusive
print(courses[2:]) # prints till last

courses.append('Arts') # adds the item at the end of the list
courses.insert(0,'Science') # adds the item at a specific index
print(courses)

courses_2 = ['EEE', 'ECE']
courses.insert(0, courses_2)
print(courses[0]) # so output is ['EEE','ECE']as courses_2 list is appended at the start

#if output has to be only EEE/ ECE from other list, use extend
courses.extend(courses_2)
print(courses_2[-1])

# deleting items
courses.remove('Physics')
print(courses)

courses.pop() #pop removes last item from the list , it can be stored in some variable as well
print(courses)

courses.reverse() # reverses the string
print(courses)

courses.remove(courses_2)
courses.sort() #sorts the string
print(courses)

#to sort the string in descending order, sort then use reverse method, but instead of that pass arguments into sort
courses.sort(reverse = True)
print(courses)

# index() gives index value of an item in list
print(courses.index('Math'))

#in is used to find if item is present in list
print('Math' in courses)

#enumerate function is used to print index of the items in a list
for index, course in enumerate(courses, start = 1 ):
    print(index, course)

course_str = ' - '.join(courses)
print(course_str)

new_list = course_str.split(' - ')
print(new_list)

#empty list
empty_list = []
empty_list = list()



