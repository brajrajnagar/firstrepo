print("ex17 default var is", __name__)

def main(num1, num2):
    num3 = num1 + num2
    print(num3)

def warn():
    print('You can\'t perform Addition outside the script \'NameMain\'.')

#  as we executed code directly __name__ variable will be __main__ by default. 
#  it implies that the module is being run standalone by the user
# if __name__ == “main”: is used to execute some code 
# only if the file was run directly, and not imported.
if __name__ == '__main__':
    main(15, 20)
else:
    warn()