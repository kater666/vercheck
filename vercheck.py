import sys
import pip

from time import sleep
from subprocess import call
from main.get_current_time import get_current_time

sys.path.append('./')

required_modules = []
installed_modules = []
missing_outdated_modules = []


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
    return sorted(installed_modules)


def make_list(modules):
    """Appending global required_modules if the module doesn't appear in the list already."""
    for i in modules:
        name = i[0]
        ver = i[1]
        names = [j.name for j in required_modules]
        if name not in names:
            x = Mods(name, ver)
            required_modules.append(x)
            if not x.exists or not x.up_to_date:
                missing_outdated_modules.append(x)


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
                    "Is up to date: %s\n" % str(i.up_to_date) + '\n')
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


def create_install_script(filename, password=None, path='./'):
    """
    Creates a script that will install missing or update outdated modules
    using pip. Unfortunately requires user's password for sudo.
    """
    missing = []
    outdated = []

    for i in missing_outdated_modules:
        if not i.exists:
            missing.append(i.name)
        elif not i.up_to_date:
            outdated.append(i.name)

    if len(missing) == 0 and len(outdated) == 0:
        sys.exit()
    else:
        install_script = open(path + filename, 'w')

    try:
        time = get_current_time()
        install_script.write("#! /bin/bash\n" +
                             "%s\n" % time +
                             "# This script will install modules:\n" +
                             "# %s\n" % missing)
        if vrs()[0] == '2':
            for j in missing:
                install_script.write("sudo pip install %s\n" % j)
        elif vrs()[0] == '3':
            for j in missing:
                install_script.write("sudo pip3 install %s\n" % j)
                if password is None:
                    pass
                else:
                    install_script.write("%s" % password)

    finally:
        install_script.close()


def execute_install_script(filename, path='./'):
    """Execute previously created install script"""
    if path != './':
        call("chmod u+x %s" % path + filename)
        call("%s" % path + filename)
    else:
        call(["chmod", "u+x", "%s" % filename])
        call("./%s" % filename)


if __name__ == '__main__':
    list_installed_modules()
else:
    list_installed_modules()


# niech wypisze, ktory modul jest osrany,
# ktorego brakuje itd.
# zczytaj loga, wyszukaj potrzebne:
# - Python - wersja
# - libs - (nazwa, wersja)
# jezeli brak modulu stworz skrypt instalujacy

# do execute_install_script dodac zabezpieczenie gdy skrypt nie istnieje