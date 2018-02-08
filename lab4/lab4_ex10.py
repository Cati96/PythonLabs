import os

# 10. Sa se scrie o functie search_by_content care primeste ca parametru doua siruri de caractere target si to_search
# si returneaza o lista de fisiere care contin to_search. Fisierele se vor cauta astfel: daca target este un fisier,
# se cauta doar in fisierul respectiv iar daca este un director se va cauta recursiv in toate fisierele din acel director.
# Daca target nu este nici fisier nici director, se va arunca o exceptie de tipul ValueError cu un mesaj corespunzator.
def exercitiul_10(target, to_search):
    listOfFiles = list()
    #if os.path.exists(target) :
    if os.path.isfile(target):
        print("The target is a file...")
        path = target.rsplit("\\",1)[0]
        os.chdir(path)
        curDir = os.getcwd()
        fileList = os.listdir(curDir)
        if to_search in fileList:
            listOfFiles.append(os.path.join(path, to_search))
        print(listOfFiles)
    elif os.path.isdir(target) :
        print("The target is a directory...")
        path = target
        for root, dirs, files in os.walk(path):
            if to_search in files:
                listOfFiles.append(os.path.join(root, to_search))
        print(listOfFiles)
    else:
        raise ValueError ("The target is nor file nor directory...")
    # else:
    #     print("The target it doesn't exists in file structures...")

print("\nRaspuns exercitiul 10:")
exercitiul_10("C:\Program Files (x86)\Python36-32\LICENSE.txt","LICENSE.txt")
print("\n#########")
exercitiul_10("C:\Program Files (x86)\Python36-32","LICENSE.txt")
print("\n#########")
#exercitiul_10("0","ceva")
