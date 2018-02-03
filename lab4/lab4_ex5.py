import sys
import os

# 5. Scrieti un script care primeste 2 parametri de la consola reprezentand un path catre un director de pe sistem si
# un nume de fisier. Scriptul va parcurge recursiv structura de fisiere si directoare din directorul dat ca parametru,
# utilizand os.walk si va scrie in fisierul dat ca parametru toate path-urile pe care le-a parcurs si tipul acestuia
# (FILE, DIRECTORY, UNKNOWN), separate de |. Fiecare path va fi scris pe cate o linie.

def exercitiul_5():
    if ( len(sys.argv) < 3 ):
        print("Few arguments... expected 2 arguments, received ", len(sys.argv) - 1 )
    else:
        pathToDir = sys.argv[1]
        filename = sys.argv[2]

        if os.path.exists(pathToDir):
            if os.path.isdir(pathToDir):
                try:
                    file = open(filename,"w")
                    for (root, directories, files) in os.walk(pathToDir):
                        for fileName in files:
                            full_fileName = os.path.join(root, fileName)
                            file.write("FILE | " + full_fileName + "\n")
                        for dirName in directories:
                            full_dirName = os.path.join(root, dirName)
                            file.write("DIRECTORY | " + full_dirName + "\n")
                    file.close()
                    print("Succesful operation...")
                except IOError:
                    print("File not found")
            else:
                print("The current path doesn't send to a directory...")
        else:
            print("The path it doesn't exists")
print("\nRaspuns exercitiul 5:")
exercitiul_5()

#command line arguments:
        #"F:\\PyCharm Workspace\\PyhtonLabs\\lab4\\someFiles" " F:\\PyCharm Workspace\\PyhtonLabs\\lab4\\someFiles\\output.txt"