def Rupesh(y):
    print("hi " +y)
    print(f"Hi - {y}")
    print(f"Hello , How are you {y}")
    return 1

def address(z):
    print(f"Rupesh stays at {z}")


if __name__ =="__main__":

    x = "Priyanka"
    z = Rupesh(x)
    print(z)
    address(78)


#passing return value of one function to another

def add(num1,num2):
    num3 = num1 +num2
    return num3

def mul(num3):
    res = num3*num3
    return res




if __name__ == '__main__':
    add (1,2)
    res = mul(3)
    print(res)
