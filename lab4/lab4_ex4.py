import os

# 4. Scrieti o functie care primeste ca parametru un path ce reprezinta un director de pe sistem, parcurge recursiv
# structura de fisiere si directoare pe care acesta le contine si afiseaza in consola toate path-urile pe care le-a
# parcurs. NU aveti voie sa folositi os.walk.
def exercitiul_4(path):
    global count
    count = 0
    if os.path.exists(path):
        x = os.listdir(path)
        for i in x:
            path2 = os.path.join(path, i)
            if os.path.isfile(path2):
                print(path2)
                continue
            elif os.path.isdir(path2):
                print(path2)
                exercitiul_4(path2)
    else:
        print("The path it doesn't exists")
print("\nRaspuns exercitiul 4:")
exercitiul_4("F:\\PyCharm Workspace\\PyhtonLabs\\lab4\\someFiles")

#F:\PyCharm Workspace\PyhtonLabs\lab4\someFiles