import shutil
import sys
import os

# 6. Scrieti un script care primeste 3 parametri de la consola. Primul va fi un path catre un fisier, al doilea un path
# catre un director iar al treilea va fi dimensiunea unui buffer. Scriptul va copia fisierul dat ca parametru in directorul
# dat ca parametru, utilizand un buffer de marimea celui de-al treilea parametru, in bytes.
def exercitiul_6():
    if ( len(sys.argv) < 4 ):
        print("Few arguments... expected 3 arguments, received ", len(sys.argv) - 1 )
    else:
        pathToFile = sys.argv[1]
        pathToDir = sys.argv[2]
        bufferSize = int(sys.argv[3])

        if os.path.exists(pathToDir):
            if os.path.exists(pathToFile):
                if os.path.isdir(pathToDir):
                    if os.path.isfile(pathToFile):
                        try:
                            source = open(pathToFile,"rt")

                            pathToDir = os.path.join(pathToDir,pathToFile.split("\\")[-1])
                            dest = open(pathToDir,"wt")
                            while 1:
                                copy = source.read()
                                if not copy:
                                    break
                            dest.write(copy)

                            print("Succesful operation...")
                        except Exception as e:
                            print("Unsuccesful operation...")
                            print(e)
                    else:
                        print("The current path doesn't send to a file...")
                else:
                    print("The current path doesn't send to a directory...")
            else:
                print("The path of file it doesn't exists...")
        else:
            print("The path of directory it doesn't exists...")
print("\nRaspuns exercitiul 6:")
exercitiul_6()


#Arguments:
        #"F:\\PyCharm Workspace\\PyhtonLabs\\lab4\\someFiles\\output.txt"
        #"F:\\PyCharm Workspace\\PyhtonLabs\\lab4\\someFiles\\arhiva"
        #20