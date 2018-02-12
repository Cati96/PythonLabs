import re

# 1. Sa se scrie o functie care extrage cuvintele dintr-un text dat ca parametru. Un cuvant este definit ca o secventa de
# caractere alfa-numerice.
def exercitiul_1(myString):
    result = re.findall('[a-zA-Z0-9]+', myString)
    print(result)
print("Raspuns exerctiul 1:")
exercitiul_1("Acest23a est1 un t43568549u4fhvuibvn98ry940bovhhri(&^(Y^(%^%)++_>:><o text cu numere23y87t8")

# 2. Sa se scrie o functie care primeste ca parametru un sir de caractere regex, un sir de caractere text si un numar
# intreg x si returneaza acele substring-uri de lungime maxim x care fac match pe expresia regulata data.
def exercitiul_2(regx, text, x):
    result = list(filter(lambda y: len(y) <= x, re.findall(regx, text)))
    print (result)
print("Raspuns exerctiul 2:")
exercitiul_2('[a-z.?!]+', 'Mine . Merg sa vad ? un pom', 3)

# 3. Sa se scrie o functie care primeste ca parametru un sir de caractere text si o lista de expresii regulate si
# returneaza o lista de siruri de caractere care fac match pe cel putin o expresie regulata data ca parametru.
def exercitiul_3(text, expr):
    print("------------- Version 1 --------------")
    result = '|'.join(expr)
    print(re.findall(result, text)) #aici da si cuvintele duplicate; se poate aplica un set pentru a returna multimea fara duplicate
    print("------------- Version 2 --------------")
    result = set()
    for ex in expr:
        for m in re.findall(ex, text):
            result.add(m)
    print(result)
print("Raspuns exerctiul 3:")
expr = ['[0-9]+', '[a-z0-9]+', '[A-Z]+']
text = "Maine merg la plaja la ora 12:30"
exercitiul_3(text, expr)

# 4. Sa se scrie o functie care primeste ca parametru path-ul catre un document xml si un dictionar attrs si returneaza
# acele elemente care au ca atribute toate cheile din dictionar si ca valoare valorile corespunzatoare.
# De exemplu, pentru dictionarul {"class": "url", "name": "url-form", "data-id": "item"} se vor selecta elementele care
# au atributele: class="url" si name="url-form" si data-id="item".
def exercitiul_4(xmlPath, attrs):
    with open(xmlPath, 'r') as f:
        content = f.read()

    tag = re.findall('<.+?>',content, re.DOTALL)
    for t in tag:
        s = t.replace("<","").replace("/","").replace(">","")
        if s in attrs.keys():
            print(s)
print("Raspuns exerctiul 4:")
xmlPath = "F:\PyCharm Workspace\PyhtonLabs\lab6\sample.xml"
attrs = {"class": "url", "name": "url-form", "data-id": "item", "note":"note"}
exercitiul_4(xmlPath, attrs)
print("I can't figure out what exactly I should do at fourth exercise...")

# 5. Sa se scrie o alta varianta a functiei de la exercitiul anterior care returneaza acele elemente care au cel putin
# un atribut care corespunde cu o pereche cheie-valoare din dictionar.
def exercitiul_5():
    print("Work in progress...")
print("Raspuns exerctiul 5:")
exercitiul_5()

# 6. Sa se scrie o functie care pentru un text dat ca parametru, cenzureaza cuvintele care incep si se termina cu vocale.
# Prin cenzurare se intelege inlocuirea caracterelor de pe pozitii impare cu caracterul * .
def exercitiul_6(text):
    splitInWords = re.findall('\w+',text)
    r = re.compile('^[aeiou]+\w*[$aeiou]', re.IGNORECASE)
    for i in splitInWords:
        if re.match(r, i):
            s = ""
            for j in range(0, len(i)):
                if j % 2 != 0:
                    s += '*'
                else:
                    s += i[j]
            text = text.replace(i,s)
    print(text)
print("Raspuns exerctiul 6:")
exercitiul_6("acesta este un text. Ca o apA cristalina.")

# 7. Sa se verifice, folosind o expresie regulata, daca un sir de caractere reprezinta un CNP valid.
def exercitiul_7(cnp):
    r = re.compile('([1]|[2])([0-9]{2})(([0]{1}[1-9]{1})|([1]{1}[0-2]{1}))(([0]{1}[1-9]{1})|([12]{1}[0-9]{1})|([3]{1}[01]{1}))([0-9]{6})$')
    if re.match(r,cnp) :
        print("Valid CNP")
    else:
        print("Invalid CNP")
print("Raspuns exerctiul 7:")
exercitiul_7("2980417226702")

# 8. Sa se scrie o functie care parcurge recursiv un director si afiseaza acele fisiere a caror nume face match pe o
# expresie regulata data ca parametru sau contine un sir de caractere care face match pe aceeasi expresie. Fisierele care
# satisfac ambele conditii vor fi afisate prefixate cu ">>"
def exercitiul_8():
    print("Work in progress...")
print("Raspuns exerctiul 8:")
exercitiul_8()