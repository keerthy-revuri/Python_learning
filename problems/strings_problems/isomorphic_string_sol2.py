def are_isomorphic(str1, str2):
    # Check if the lengths of both strings are equal
    if len(str1) != len(str2):
        return False

    # Create dictionaries to store the mapping of characters from str1 to str2 and vice versa
    char_map_str1 = {}
    char_map_str2 = {}

    # Iterate through the characters of both strings
    for i in range(len(str1)):
        char1 = str1[i]
        char2 = str2[i]

        # If char1 is already mapped to a different character in str2, or vice versa, return False
        if char1 in char_map_str1 and char_map_str1[char1] != char2:
            return False
        if char2 in char_map_str2 and char_map_str2[char2] != char1:
            return False

        # Otherwise, create or update the mapping
        char_map_str1[char1] = char2
        char_map_str2[char2] = char1

    # If we reach this point, the strings are isomorphic
    return True

# Test cases
print(are_isomorphic("egg", "add"))  # True
print(are_isomorphic("foo", "bar"))  # False
print(are_isomorphic("paper", "title"))  # True
