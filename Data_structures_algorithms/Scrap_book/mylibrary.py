def add(x, y):
    return x+y
def hello():
    print("Hello World")

print(__name__)


# The below code has to be written in other python file

import mylibrary

mylibrary.hello()
print(mylibrary.add(10, 20))

print(__name__)

