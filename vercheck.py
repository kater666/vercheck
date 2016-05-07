import sys
import pip

from get_current_time import get_current_time

required_modules = []
installed_modules = []


class Mods(object):

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


def read_requirements(file):
    """
    Reads requirements from file. Returns list of tuples.
     Example return: [('selenium', '2.53.1')]
    """
    f = open(file, 'r')
    try:
        requirements = []
        for i in f.readlines():
            line = i[:-1]
            if 'Required modules' in line:
                search = line.split(": ")
                modules = search[1].split(', ')
                for j in modules:
                    name = j.split(' - ')[0]
                    req_ver = j.split(' - ')[1]
                    requirements.append((name, req_ver))
        return requirements
    finally:
        f.close()


def list_installed_modules():
    """Appends installed_modules with installed distributions."""
    # Get installed modules.
    inst = pip.get_installed_distributions()
    for i in inst:
        installed_modules.append((i.key, i.version))
    installed_modules.sort()


def make_list(modules):
    """Appending global required_modules if the module doesn't appear in the list already."""
    for i in modules:
        name = i[0]
        ver = i[1]
        names = [j.name for j in required_modules]
        if name not in names:
            x = Mods(name, ver)
            required_modules.append(x)


def list_requirements(file):
    """Shortcut for appending required_modules."""
    make_list(read_requirements(file))


def print_required_modules():
    """Print modules in required_modules."""
    for i in required_modules:
        i.print_module()


def log_required_modules(filename, path='./'):
    """
    Creates log with installed, missing or outdated modules.
    Function will create a log with given filename and path.
    If path is not given, by default it will be currently working directory.
    Example use:
    log_required_modules('text_file', '/home/user/')
    """
    f = open(path + filename, 'w')
    try:
        f.write(get_current_time() + " " + filename + '\n\n')
        for i in required_modules:
            f.write("Module\n" +
                    "Name: %s\n" % i.name +
                    "Required version: %s\n" % i.req_version +
                    "Actual version: %s\n" % i.version +
                    "Exists: %s\n" % str(i.exists) +
                    "Is up to date %s\n" % str(i.up_to_date) + '\n')
    finally:
        f.close()


def check_libs(mod_list=[]):
    """Check existence and version of required modules."""
    global installed_modules
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


if __name__ == '__main__':
    list_installed_modules()
else:
    list_installed_modules()


"""
    list_installed_modules()
    list_requirements('text_file')
    check_libs(required_modules)
    print_required_modules()
    log_required_modules('file name')
"""

# niech wypisze, ktory modul jest osrany,
# ktorego brakuje itd.
# zczytaj loga, wyszukaj potrzebne:
# - Python - wersja
# - libs - (nazwa, wersja)
# jezeli brak modulu stworz skrypt instalujacy