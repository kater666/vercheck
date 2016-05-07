from sys import argv
import vercheck

req_libs = [('ddt', '1.0.1'), ('Kanae', '1')]
vercheck.check_libs(req_libs)
for i in vercheck.required_modules:
    i.print_module()


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
