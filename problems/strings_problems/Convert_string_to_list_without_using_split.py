str = "i love to code"
start = 0
word_list = []
while start < len(str):
    end = str.find(' ',start) # string.find(value, start, end) - finds first occurence of value between start to end indexes
    if end == -1:
        end = len(str)
    word_list.append(str[start:end])
    start = end + 1
print(word_list)