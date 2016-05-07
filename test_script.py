from sys import argv
from vercheck import *

list_requirements('text_file')
check_libs(required_modules)
print_required_modules()
log_required_modules('Test log.txt')
'''
script, file = argv
f = open(file, 'r')
try:
    lines = f.readlines()

    for i in lines:
        print(i)
except FileNotFoundError:
    print("File not found.")
finally:
    f.close()
'''