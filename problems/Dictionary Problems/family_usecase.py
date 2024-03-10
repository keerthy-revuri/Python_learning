people_dict = {}

#add below name as key and value as age for loka and family
# Rupesh 30
# Keerthy 24
# Bhupathi 60
# Sreelatha 55
people_dict['Rupesh'] = 30
people_dict['Keerthy'] = 24
people_dict['Bhupathi'] = 60
people_dict['Sreelatha'] = 55
print(people_dict)


# Print names in dictionary with people name in list above 50 years of age
names = []
for name in people_dict:
	if people_dict[name] > 50:
		names.append(name)
print(f"names above 50 years - {names}")

# print keys from the orginal dictionary
print(people_dict.keys())
for name in people_dict.keys():
	print(f"keys from original dictionary - {name}")

#calculate the total age of all people from above dictionary
final = 0
for age in people_dict.values():
	final = final + age
print(f" total age of all people - {final}")

# who has the smallest age from above dictionary
ages = []
for age in people_dict.values():
	ages.append(age)
print(ages)
min_age = ages[0]
for i in range(len(ages)):
	if ages[i]<min_age:
		min_age = ages[i]

print(f"the smallest age is - {min_age}")


#who is the eldest from above dictionary
max_age = ages[0]
for i in range(len(ages)):
	if ages[i] > max_age:
		max_age = ages[i]
print(f"the eldest is - {max_age}")


#print the output in below format
# The person Rupesh has age 30
#The person Keerthy has age 24
for i in people_dict:
	print(f"The person {i} has age {people_dict[i]}")

# Now add keerthy family to the orginal dictionary

# Prakash Reddy 50
# Manjula 43
people_dict.update({'Prakash Reddy':50, 'Manjula' : 45})
print(f"after adding Keerthy family to dictionary - {people_dict}")

#print the whole dictionary - loka and revuri family


# count the number of people in the final dictionary
print(f"The number of people are - {len(people_dict)}")

family = {'Rupesh': {'age': 30, 'gender':'M'}, 'Keerthy': {'age':24, 'gender':'F'}, 'Sreelatha':{'age':55, 'gender':'F'}}

# I want to know total number of females in the above dict
count = 0
print(family['Rupesh']['gender'])
for i in family.values():
	if i['gender'] == 'F':
		count = count + 1
print(f"The number of females are - {count}")

#which person has more no. of mobile numbers, here list indicates numbers
family = {'Rupesh': [1,2,7], 'Keerthy': [3,4,5], 'Sreelatha':[6]}

family_dict = {}
for name, phone_numbers in family.items():
	family_dict[name] = len(phone_numbers)
print(family_dict)

max_number = -1
max_names = []
for name, number in family_dict.items():
	if number>=max_number:
		max_number = number
		max_names.append(name)

print(max_names)

#solve the above problem using below dict

family = {'Rupesh': {'age': 30, 'gender':'M', 'phone_numbers': [1,2,3]}, 'Keerthy': {'age':24, 'gender':'F', 'phone_numbers': [5,2,3]}, 'Sreelatha':{'age':55, 'gender':'F', 'phone_numbers': [1,3]}}
family_dict_2 = {}
for name, name_details_dict in family.items():
	#print(len(name_details_dict['phone_numbers']))
	family_dict_2[name] = len(name_details_dict['phone_numbers'])
print(family_dict_2)

max_number = -1
max_names = []
for name, phone_number in family_dict_2.items():
	if phone_number >= max_number:
		max_number = phone_number
		max_names.append(name)
print(max_names)




