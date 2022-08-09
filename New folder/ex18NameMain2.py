# If you import this script as a module in another script, 
# the __name__ is set to the name of the script/module.

import ex17NameMain

if __name__ == '__main__':
    print('ex18 default var is', __name__)

# manually accessing the function of imported script.
ex17NameMain.main(10,15)