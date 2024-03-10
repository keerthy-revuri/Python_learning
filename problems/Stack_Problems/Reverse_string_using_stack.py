# Python program to reverse a string using stack

# Function to create an empty stack.
# It initializes size of stack as 0

class Reversestring:
    def createStack(self):
        stack = []
        return stack

    # Function to determine the size of the stack


    def size(self,stack):
        return len(stack)

    # Stack is empty if the size is 0


    def isEmpty(self,stack):
        if self.size(stack)== 0:
            return True

    # Function to add an item to stack .
    # It increases size by 1


    def push(self,stack, item):
        stack.append(item)

    # Function to remove an item from stack.
    # It decreases size by 1


    def pop(self,stack):
        if self.isEmpty(stack):
            return
        return stack.pop()

    # A stack based function to reverse a string


    def reverse(self,string):
        n = len(string)

        # Create a empty stack
        stack = self.createStack()

        # Push all characters of string to stack
        for i in range(0, n, 1):
            self.push(stack, string[i])

        # Making the string empty since all
        # characters are saved in stack
        string = ""

        # Pop all characters of string and
        # put them back to string
        for i in range(0, n, 1):
            string += self.pop(stack)

        return string


# Driver program to test above functions
string = "GeeksQuiz"
rs = Reversestring()
string = rs.reverse(string)

print("Reversed string is " + string)


#simple logic 2
#reverse of a string using stack

str = "Hello"
stack = []
for i in str:
    stack.append(i)
str = '' # as all elements are added to stack , make the string empty
print(stack)
while len(stack) > 0:
    str = str +  stack.pop()
print(str)
