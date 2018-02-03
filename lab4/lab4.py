# 1. Scrieti un program python care sa primeasca de la linia de comanda doua numere (a si b) si care sa afiseze:
# a) a-b
# b) a+b
# c) a/b
# d) a*b
def exercitiul_1():
    print("ok")
print("\nRaspuns exercitiul 1:")
exercitiul_1()

# 3. Scrieti o functie care primeste ca parametru un nume de fisier. Aceasta va scrie in fisier datele din os.environ,
# fiecare linie continand cate o intrare din acest dictionar, sub forma cheie [tab] valoare.
def exercitiul_3():
    print("ok")
print("\nRaspuns exercitiul 3:")
exercitiul_3()

# 4. Scrieti o functie care primeste ca parametru un path ce reprezinta un director de pe sistem, parcurge recursiv
# structura de fisiere si directoare pe care acesta le contine si afiseaza in consola toate path-urile pe care le-a
# parcurs. NU aveti voie sa folositi os.walk.
def exercitiul_4():
    print("ok")
print("\nRaspuns exercitiul 4:")
exercitiul_4()

# 10. Sa se scrie o functie search_by_content care primeste ca parametru doua siruri de caractere target si to_search
# si returneaza o lista de fisiere care contin to_search. Fisierele se vor cauta astfel: daca target este un fisier,
# se cauta doar in fisierul respectiv iar daca este un director se va cauta recursiv in toate fisierele din acel director.
# Daca target nu este nici fisier nici director, se va arunca o exceptie de tipul ValueError cu un mesaj corespunzator.
def exercitiul_10():
    print("ok")
print("\nRaspuns exercitiul 10:")
exercitiul_10()

# 11. Sa se scrie o functie get_file_info care primeste ca parametru un sir de caractere care reprezinta calea catre un
# fisier si returneaza un dictionar cu urmatoarele campuri:
# full_path = calea absoluta catre fisier,
# file_size = dimensiunea fisierului in octeti,
# file_extension = extensia fisierului (daca are) sau "",
# can_read si can_write = True/False daca se poate citi din/scrie in fisier.
def exercitiul_11():
    print("ok")
print("\nRaspuns exercitiul 11:")
exercitiul_11()

# 12. Sa se scrie o functie get_dirs_info care primeste ca parametru un sir de caractere care reprezinta calea catre un
# director si returneaza un dictionar cu urmatoarele informatii:
# full_path = calea absoluta catre director,
# total_size = dimensiunea tuturor fisierelor din acel director,
# files = calea relativa catre toate fisierele din acel director, grupate dupa adancime.
# dirs = calea absoluta catre toate directoarele din acel director cu toate informatiile corespunzatoare.
# Sa se scrie intr-un fisier output.txt numele directoarelor returnate de functia get_dirs_info sortate descrescator dupa
# numarul de fisiere cu adancimea 2.
# Sa se scrie intr-un fisier size.txt numele directoarelor returnate de functia get_dirs_info sortate descrescator dupa
# total_size.
# Sa se scrie intr-un fisier lungime.txt numele directoarelor returnate de functia get_dirs_info sortate descrescator dupa
# numarul maxim de caractere din numele fișierelor.
def exercitiul_12():
    print("ok")
print("\nRaspuns exercitiul 12:")
exercitiul_12()

# 13. Sa se scrie o funcție ce returnează o lista cu toate fisierele dintr-un director(primit ca parametru), ce au o
# anumita extensie (primita ca parametru).
# Sa se scrie o functie clasifica ce va copia fisierele returnate de la funcția anterioară în felul următor:
#  - în 5 directoare cu nume specific, in functie de size - (0-10KB, 10KB-1MB, 1MB-2MB, 2MB-5MB, 5MB-)
#  - în 5 directoare cu nume specific, in functie de size - (diferență de maxim 1 fișier între 2 directoare)
#  - în directoare cu nume specific, in functie de primul caracter din nume
#  - în 2 directoare cu nume specific - numele format doar din litere sau nu
def exercitiul_13():
    print("ok")
print("\nRaspuns exercitiul 13:")
exercitiul_13()
