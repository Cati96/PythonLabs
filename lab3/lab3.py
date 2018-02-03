import re
# 1. Sa se scrie o functie care primeste ca parametri doua liste a si b si returneaza un tuplu de seturi care sa contina:
# (a intersectat cu b, a reunit cu b, a - b, b - a)
def exercitiul_1(a, b):
    myList = list()
    myList.append(set(set(a) & set(b)))
    myList.append(set(set(a) | set(b)))
    myList.append(set(set(a) - set(b)))
    myList.append(set(set(b) - set(a)))
    myList = tuple(myList)
    print(myList)

print("\nRaspuns exercitiul 1:")
exercitiul_1([1,2,3], [4,5,6])
# 2. Scrieti o functie care primeste ca parametru un sir de caractere si returneaza un dictionar in care cheile sunt
# caracterele dn componenta sirului de caractere iar valorile sunt reprezentate de numarul de aparitii ale caracterului
# respectiv in textul dat.
# Exemplu: Pentru sirul "Ana are mere." dat ca parametru functia va returna dictionarul:
# {'A': 1, ' ': 2, 'n': 1, 'a': 2, 'r': 2, 'e': 3, 'm': 1, '.': 1}.
def exercitiul_2(string):
    counts = {i: 0 for i in string}
    for char in string:
        counts[char] += 1
    print(counts)
print("\nRaspuns exercitiul 2:")
exercitiul_2("Ana are mere.")

# 3. Sa se compare doua dictionare fara a folosi operatorul "==" si sa se returneze un tuplu de liste de diferente
# astfel: (cheile_comune_dar_cu_valori_diferite, cheile_care_se_gasesc_doar_in_primul_dict, cheile_care_se_gasesc_
# doar_in_al_doilea_dict). (Atentie, dictionarele trebuiesc parcurse recursiv deoarece la randul lor pot contine alte
# containere, cum ar fi dictionare, liste, set-uri, etc)
def exercitiul_3(dict1, dict2):
    myList = list()
    list1 = list()
    list2 = list()
    list3 = list()
    all = {}

print("\nRaspuns exercitiul 3:")
exercitiul_3({"A":1, "C":1},{"B":2})

# 4. Fie functia build_xml_element care primeste urmatorii parametri: tag, content si elemente cheie-valoare date ca
# parametri cu nume. Sa se construiasca si sa se returneze un string care reprezinta elementul XML aferent.
# Exemplu: build_xml_element("a", "Hello there", href="http://python.org", _class="my-link", id="someid")
# => "<a href=\"http://python.org\" _class=\"my-link\" id=\"someid\">Hello there</a>"
def build_xml_element(tag, content, **kwargs):
    response = '<{tag}{}>{content}</{tag}>'.format(' '.join(['='.join([x, y]) for x, y in kwargs.items()]),
                                                    content=content, tag=tag)
    print(response)
print("\nRaspuns exercitiul 4:")
build_xml_element("a", "Hello there", href="http://python.org", _class="my-link", id="someid")

# 5. Fie functia validate_dict care primeste ca parametru un set de tuple care reprezinta reguli de validare pentru un
# dictionar cu chei de tipul string si valori tot de tipul string si un dictionare. O regula este definita astfel:
# (cheie, "prefix", "middle", "sufix"). O valoare este considerata valida daca incepe cu "prefix", "middle" se gaseste
# in interiorul valorii (nu la inceput sau sfarsit) si se sfarsete cu "sufix". Functia va returna True daca dictionarul
# dat ca parametru respecta toate regulile, False in caz contrar.
# Exemplu: regulile [("key1", "", "inside", ""), ("key2", "start", "middle", "winter")] si dictionarul
# {"key2": "starting the engine in the middle of the winter", "key1": "come inside, it's too cold outside",
# : "this is not valid"} => False deoarece desi regulile sunt respectate pentru "key1" si "key2", apare "key3"
# care nu apare in reguli.

def exercitiul_5(rules, dictionary):
    def create_regex(*k):
        regex = re.compile("(.)+".join(k))
        return regex

    def is_regex_valid(regex, string):
        return re.search(regex, string) is not None

    def is_valid(rules, pair):
        valid = True

        for rule in rules:
            if rule[0] == pair[0]:
                if not is_regex_valid(create_regex(rule[1], rule[2], rule[3]), pair[1]):
                    valid = False

        return valid

    for a in dictionary:
        if not is_valid(rules, (a, dictionary[a])):
            return False

    return True
print("\nRaspuns exercitiul 5:")
print(str(exercitiul_5([("key1", "", "inside", ""), ("key2", "start", "middle", "winter")],
                                   {"key2": "starting the engine in the middle of the winter",
                                    "key1": "come inside, it's too cold outside", "key3": "this is not valid"}
                                   )) + "\n\n")

# 6. Fie un dictionar global
# {
#     "+": lambda a, b: a + b,
#     "*": lambda a, b: a * b,
#     "/": lambda a, b: a / b,
#     "%": lambda a, b: a % b
# }
#  Sa se construiasca o functie apply_operator(operator, a, b) care va aplica peste a si b regula specificata de
# dictionarul global. Sa se implementeze astfel incat, in cazul adaugarii unui operator nou, sa nu fie necesara
# modificarea functiei.

global_dict = {
    "+": lambda a, b: a + b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b,
    "%": lambda a, b: a % b
}
def exercitiul_6(operator,a,b):
    print(global_dict[operator](a, b))
print("\nRaspuns exercitiul 6:")
exercitiul_6("+",1,2)

# 7. Fie un dictionar global definit asemanator cu cel de mai sus, cu deosebirea ca functiile date ca valori ale
# dictionarului poate primi orice combinatie de parametri. Sa se scrie o functie apply_function care primeste ca
# parametru numele unei operatii si aplica functia corespunzatoare peste argumentele primite. Sa se implementeze astfel
# incat, in cazul adaugarii unei functii noi, sa nu fie necesara modificarea functiei apply_function.
#
# Un exemplu de dictionar global ar putea fi urmatorul:
#
# {
#     "print_all": lambda *a, **k: print(a, k),
#     "print_args_commas": lambda *a, **k: print(a, k, sep=", "),
#     "print_only_args": lambda *a, **k: print(a),
#     "print_only_kwargs": lambda *a, **k: print(k)
# }

global_dict2 = {
    "print_all": lambda *a, **k: print(a, k),
    "print_args_commas": lambda *a, **k: print(a, k, sep=", "),
    "print_only_args": lambda *a, **k: print(a),
    "print_only_kwargs": lambda *a, **k: print(k)
}

def exercitiul_7(function, *args, **kwargs):
    print(global_dict2[function](*args, **kwargs))
print("\nRaspuns exercitiul 7:")
args = [[1,2,3,"a"] , "b" ,True ]
kwargs = {"A":1, "B":2, "C":3, "D":4, "E":5,"F":None}
exercitiul_7("print_all",*args, **kwargs)
print("#########")
exercitiul_7("print_args_commas",*args)
print("#########")
exercitiul_7("print_only_args", *args)
print("#########")
exercitiul_7("print_only_kwargs",**kwargs)

# 8. Sa se scrie o functie care primeste ca parametru un set si returneaza un tuplu (a, b), a reprezentand numarul de
# elemente unice din set iar b reprezentand numarul de elemente duplicate din set.
def exercitiul_8(param):
    count = list(map(lambda x: param.count(x), param))
    zipper = set(zip(param, count))

    unique = list(filter(lambda x: x[1] == 1, zipper))
    duplicates = list(filter(lambda x: x[1] != 1, zipper))

    print("Unique values: ", unique, "\nDuplicates values: ", duplicates)
print("\nRaspuns exercitiul 8:")
exercitiul_8([1, 2, 3, 1, 2, 3, 1, 33])

# lista de elemente duplicate din set => ...un set nu are elemente duplicate

# 9. Sa se scrie o functie care primeste un numar variabil de seturi si returneaza un dictionar cu urmatoarele operatii
# dintre toate seturile doua cate doua: reuniune, intersectie, a-b, b-a. Cheia va avea urmatoarea forma: "a op b", unde
# a si b sunt doua seturi, iar op este operatorul aplicat: |, &, -.
# Ex: {1,2}, {2, 3} =>
# {
#     "{1, 2} | {2, 3}": 3,
#     "{1, 2} & {2, 3}": 1,
#     "{1, 2} - {2, 3}": 1,
#     ...
# }
def exercitiul_9(*sets):
    myDict = dict()
    for i in range(0, len(sets) - 1):
        for j in range(i, len(sets)):
            reun = sets[i] | sets[j]
            inters = sets[i] | sets[j]
            diff1 = sets[i] - sets[j]
            diff2 = sets[j] - sets[i]
            myDict['{} | {}'.format(sets[i], sets[j])] = reun
            myDict['{} & {}'.format(sets[i], sets[j])] = inters
            myDict['{} - {}'.format(sets[i], sets[j])] = diff1
            myDict['{} - {}'.format(sets[j], sets[i])] = diff2
    for i in myDict.items():
        print(i)
print("\nRaspuns exercitiul 9:")
exercitiul_9({1,2}, {2, 3},{3,4},{5,6})