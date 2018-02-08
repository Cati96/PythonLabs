import os
# 11. Sa se scrie o functie get_file_info care primeste ca parametru un sir de caractere care reprezinta calea catre un
# fisier si returneaza un dictionar cu urmatoarele campuri:
# full_path = calea absoluta catre fisier,
# file_size = dimensiunea fisierului in octeti,
# file_extension = extensia fisierului (daca are) sau "",
# can_read si can_write = True/False daca se poate citi din/scrie in fisier.
def exercitiul_11(path):
    myDict = {}
    myDict.setdefault("full_path")
    myDict.setdefault("file_size")
    myDict.setdefault("file_extension")
    myDict.setdefault("can_read")
    myDict.setdefault("can_write")

    if os.path.exists(path):
        myDict.update({"full_path" : os.path.abspath(path)})
        myDict.update({"file_size" : os.path.getsize(path)})
        if os.path.splitext(path)[1][1:] != "" :
            x = os.path.splitext(path)[1][1:]
        else:
            x = ""
        if os.access( path, os.R_OK) == True :
            y = True
        else:
            y = False
        if os.access(path, os.W_OK) == True :
            z = True
        else:
            z = False
        myDict.update({"file_extension" : x})
        myDict.update({"can_read" : y})
        myDict.update({"can_write": z})

        for i in myDict.items():
            print(i)
    else:
        print("The entered path it doesn't exists...")

print("\nRaspuns exercitiul 11:")
exercitiul_11("C:\Program Files (x86)\Python36-32\\LICENSE.txt")
print("\n#########")
exercitiul_11("C:\Program Files (x86)\Python36-32")