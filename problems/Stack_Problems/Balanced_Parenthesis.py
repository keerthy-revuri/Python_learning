#Given an expression string, write a python program to find whether a given string has balanced parentheses or not.

#string = "{[(])}"
string = ')'
dict = {'}':'{',']':'[',')':'('}
input_stack = []
flag = ""
for i in string:
    if i in '{[(':
        input_stack.append(i)
        print(f"input stack is - {input_stack}")
    else:
        last_ele = input_stack[len(input_stack)-1]
        print(f"last_element is - {last_ele}")
        if len(input_stack) > 0 and dict[i] == last_ele:
            print(f"dictionary elements of {i} is - {dict[i]}")
            x = input_stack.pop()
            print(f"popped element is - {x}")
            print(f"input stack after pop is - {input_stack}")
        else:
            print("unbalanced")
            break
if len(input_stack) == 0:
    print("balanced")
else:
    print("not balanced")






