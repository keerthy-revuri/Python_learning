def replace_char_in_list(a, repl_char,given_char):
    b = []
    for i in a:
        if i == given_char:
            b.append(i)
        else:
            b.append(repl_char)
    return b
a = ['G','R','G','P','S']
repl_char = '*'
given_char = 'G'
res = replace_char_in_list(a,repl_char,given_char)
print(res)



#logic 2

input_list = ['G', 'R', 'G', 'P', 'S']
given_char = 'G'
repl_char = '*'
for i in range(len(input_list)):
    if input_list[i] != 'G':
        input_list[i] = '*'

print(input_list)


