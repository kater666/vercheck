import sys
sys.path.append(r'..')
from sys import argv
from vercheck import *

inst = list_installed_modules()
req_mods = list_requirements('text_file')
check_libs(req_mods)
#print_required_modules()
log_required_modules('log.txt')
create_install_script(filename='install_script', password='123')



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