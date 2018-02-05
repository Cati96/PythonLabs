import sys
import getpass
import os
import platform
import multiprocessing

# 9. Sa se creeze un script care afiseaza urmatoarele informatii despre sistem:
#
#     versiunea de python folosita. Daca se foloseste Python 2 va afisa in plus mesajul "=== Python 2 ==="
#     iar daca se foloseste Python 3 va afisa in plus mesajul "Running under Py3" (hint: sys.version_info)
#     numele user-ului care a executat scriptul,
#     path-ul complet al scriptului.
#     path-ul directorului in care se afla scriptul,
#     tipul sistemului de operare,
#     numarul de core-uri,
#     directoarele din PATH-ul procesului cate unul pe linie,
def exercitiul_9():
    python_version = sys.version_info
    if python_version[0] == 3:
        print("Running under Py3")
    elif python_version[0] == 2:
        print("=== Python 2 ===")
    else:
        print("Python")

    print("User " + getpass.getuser())

    script_path = os.path.realpath(__file__)
    directory = "\\".join(script_path.split("\\")[0:-1])

    print(script_path)
    print(directory)
    print(platform.system() + " " + platform.release())
    print(platform.processor())
    print(multiprocessing.cpu_count())
print("\nRaspuns exercitiul 9:")
exercitiul_9()