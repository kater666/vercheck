import sys
import pip


class Mods(object):

    # Take module's name, version
    def __init__(self, name, req_version, version=None, exists=False, up_to_date=False):
        self.name = name
        self.req_version = req_version
        self.version = version
        self.exists = exists
        self.up_to_date = up_to_date

    def print_module(self):
        print("Name: %s\n" % self.name,
              "Required version: %s\n" % self.req_version,
              "Actual version: %s\n" % self.version,
              "Exists: %s\n" % str(self.exists),
              "Is up to date: %s" % str(self.up_to_date))


def vrs():
    ver = sys.version.split(" ")[0]
    return ver


def check_py2():
    if vrs()[0] == '2':
        print("You are using Python 2.")


def check_py3():
    if vrs()[0] == '3':
        print("You are using Python 3.")


required_modules = []
installed_modules = []


def read_requirements(file):
    # Read required modules from file.
    pass


def check_libs(mod_list=[]):
    # Check existence and version of required modules.

    # List required modules.
    for i in mod_list:
        name = i[0]
        ver = i[1]
        x = Mods(name, ver)
        required_modules.append(x)

    # Get installed modules.
    inst = pip.get_installed_distributions()
    for i in inst:
        installed_modules.append((i.key, i.version))
    installed_modules.sort()

    # Search if required module (i) is installed.
    for i in required_modules:
        for j in installed_modules:

            # If it's installed, set self.exists = True.
            if i.name == j[0]:
                i.exists = True

                # If the req_version is correct, set self.req_version = True.
                if i.req_version == j[1]:
                    i.up_to_date = True
                    i.version = j[1]
                else:
                    # set actual ver
                    i.version = j[1]


# I don't know why it's here.
#check_libs([('dt', '1.0.1'), ('django', '1.9.5')])
#for i in required_modules:
#    i.print_module()
#for i in required_modules:
#    print(i.name, i.req_version, i.exists, i.up_to_date)


# niech wypisze, ktory modul jest osrany,
# ktorego brakuje itd.
# zczytaj loga, wyszukaj potrzebne:
# - Python - wersja
# - libs - (nazwa, wersja)
