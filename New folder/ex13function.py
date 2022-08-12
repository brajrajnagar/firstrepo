from sys import argv


# ' * ' in function definitions in python is used to pass a variable number 
# of arguments to a function. It is used to pass a non-key worded, 
# variable-length argument list. 
def fun_two(*args):
    arg = list(args)
    print(arg1[0], arg[2])

def fun_two2(arg1, arg2):
    print(arg1, arg2)

def add(num1, num2):
    sum = num1+num2
    return sum

fun_two("Apple", "Boy", "Cat")
fun_two2("Hp", "Desktop")
print(add(50,100))
