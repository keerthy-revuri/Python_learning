#1. matching patterns
import re

pattern = r"Keerthy"
str1 = "Rupesh is a dash"
is_match = re.match(pattern, str1)
print(is_match)
if is_match:
    print("Matched")
else:
    print("Not matched")


#2. Replacing patterns
pattern = r"\d+"  # Matches one or more digits
text = "There are 123 apples and 456 oranges."
new_text = re.sub(pattern, "X", text)
print(new_text)  # Output: "There are X apples and X oranges."


#3. Searching for patterns
pattern = r"world"
text = "hello world"
search_result = re.search(pattern, text)
if search_result:
    print("Pattern found!")
else:
    print("Pattern not found.")


#4. Finding all matches
pattern = r"\d+"  # Matches one or more digits
text = "There are 123 apples and 456 oranges."
matches = re.findall(pattern, text)
print(matches)  # Output: ['123', '456']

#5. Splitting groups
pattern = r"\s+"  # Matches one or more whitespace characters
text = "hello   world"
parts = re.split(pattern, text)
print(parts)  # Output: ['hello', 'world']


#6. Using Groups
pattern = r"(\d{3})-(\d{2})-(\d{4})"  # Matches dates in the format XXX-XX-XXXX
text = "Date of birth: 123-45-6789"
match = re.search(pattern, text)
if match:
    print("Full match:", match.group(0))  # Output: "123-45-6789"
    print("Month:", match.group(1))       # Output: "123"
    print("Day:", match.group(2))         # Output: "45"
    print("Year:", match.group(3))        # Output: "6789"





