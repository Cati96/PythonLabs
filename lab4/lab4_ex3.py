import os
# 3. Scrieti o functie care primeste ca parametru un nume de fisier. Aceasta va scrie in fisier datele din os.environ,
# fiecare linie continand cate o intrare din acest dictionar, sub forma cheie [tab] valoare.
def exercitiul_3(path):
    if os.path.exists(path):
        if os.path.isfile(path):
            file = open(path,"w")
            zipped = zip(os.environ.keys(), os.environ.values())
            output = list(map(lambda x: str(x[0]) + "   " + str(x[1]), zipped))
            for line in output:
                file.write(line + "\n")
        else:
            print("Please select a file...")
    else:
        print("Entered path it doesn't exist...")
    print("ok")
print("\nRaspuns exercitiul 3:")
exercitiul_3("F:\\PyCharm Workspace\\PyhtonLabs\\lab4\\someFiles\\test2.txt")