import os

# 2. Scrieti un script care primeste ca parametru de la linia de comanda un path si afiseaza primii 4096 bytes daca
# path-ul duce la un fisier, intrarile din acesta daca path-ul reprezinta un director si un mesaj de eroare daca path-ul
# nu este unul valid.
def exercitiul_2():
    path = input("Enter path: ")
    if os.path.exists(path) is True:
        if os.path.isfile(path):
            file = open(path,"r")
            print("The firsts 4096bytes from file are: ", file.read(4096) )

        elif os.path.isdir(path):
            x = [os.path.join(r, file) for r, d, f in os.walk(path) for file in f]
            for i in x:
                print(i)
            print("Some")
            print(os.listdir(path))
            print("####")
            for (root, directories, files) in os.walk(path):
                for fileName in files:
                    full_fileName = os.path.join(root, fileName)
                    print("File: ", full_fileName)
                for dirName in directories:
                    full_dirName = os.path.join(root,dirName)
                    print("Directory: ", full_dirName)
    else:
        print("Entered path it doesn't exist...")
print("\nRaspuns exercitiul 2:")
exercitiul_2()

#F:\PyCharm Workspace\PyhtonLabs\lab4\someFiles
#F:\PyCharm Workspace\PyhtonLabs\lab4\someFiles\test.txt