# 1. Sa se scrie o functie care sa returneze o lista cu primele n numere din sirul lui Fibonacci.
def exercitiul_1(n):
    myList = list()
    if ( n == 0 ):
        print("n is zero...")
    elif( n == 1 ):
        myList.append(1)
    elif(n == 2):
        myList.append(1)
        myList.append(2)
    else:
        myList.append(1)
        myList.append(2)
        n -= 2
        while ( n > 0 ):
            x = myList[len(myList) - 1] + myList[len(myList)-2]
            myList.append(x)
            n -= 1
    print(myList)
print("\nRaspuns exercitiul 1:")
exercitiul_1(25)

# 2. Sa se scrie o functie care primeste o lista de numere si returneaza o lista cu numerele prime care se gasesc in ea.
def prime_number(number):
    divisors = 1
    for i in range ( 2, int(number/2) + 1):
        if number % i == 0:
            divisors += 1
    if ( divisors == 1 ):
        return True
    return False

def exercitiul_2(myList):
    prime_number_list = list(filter(lambda elem: prime_number(elem) == True, myList))
    return prime_number_list
print("\nRaspuns exercitiul 2:")
lets_see = exercitiul_2([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,19,20])
print(lets_see)

# 3. Fie un tuplu (x,y) reprezentarea unui punct intr-un sistem cartezian. Sa se scrie o functie care primeste ca
# parametru o lista de puncte si returneaza o lista de tuple (a,b,c) unice care reprezinta dreptele unice determinate
# de acele puncte ( (a,b,c) corespunde dreptei ax + by + c = 0).

#(y-yb)(xa-xb)= (ya-yb)(x-xb)
# y*xa - y*xb - xa*yb + yb*xb = x*ya - x*yb - ya*xb + xb*yb
# x(ya-yb) - y(xa-xb) + xa*xb - xb*yb - xb*ya + xb*yb = 0
# x(ya-yb) - y(xa-xb) + xa*xb - xb*ya = 0
# a = ya-yb
# b = xa-xb
# c = xa*xb - xb*ya

def exercitiul_3(listOfCoord):
    points = set()
    for i in range (0, len(listOfCoord )-1):
        xa = listOfCoord[i][0]
        ya = listOfCoord[i][1]
        for j in range(1, len(listOfCoord)):
            xb = listOfCoord[j][0]
            yb = listOfCoord[j][1]
            a= ya - yb
            b = xa - xb
            c = xa*xb - xb*ya
            points.add((a,b,c))
    points = list(points)
    print (points)
print("\nRaspuns exercitiul 3:")
exercitiul_3([(1,2), (2,3), (4,5), (5,6)])


# 4. Sa se scrie o functie care primeste ca parametri doua liste a si b si returneaza: (a intersectat cu b, a reunit cu
# b, a - b, b - a)
def exercitiul_4(a, b):
    a = set(a)
    b = set(b)
    c1= a.intersection(b)
    c2 = a.union(b)
    c3 = a.difference(b)
    c4 = b.difference(a)
    print(c1)
    print(c2)
    print(c3)
    print(c4)
print("\nRaspuns exercitiul 4:")
exercitiul_4([1,2,3,4], [2,3,4,5])

# 5. Sa se scrie o functie care primeste ca parametru o lista x, si un numar k. Sa se returneze o lista cu tuple care sa
# reprezinte combinari de len(x) luate cate k din lista x. Exemplu: pentru lista x = [1,2,3,4] si k = 3 se va returna
# [(1, 2, 3), (1, 2, 4), (1, 3, 4), (2, 3, 4)].
def exercitiul_5(x, k):
    n = len(x)

    results = list()
    for i in range(2 ** n):
        count = 0
        for j in range(n):
            if i & (1 << j) != 0:
                count += 1
        if count == k:
            comb = list()
            for j in range(n):
                if i & (1 << j) != 0:
                    comb.append(x[j])
            results.append(comb)

    print( results )
print("\nRaspuns exercitiul 5:")
exercitiul_5([1,2,3,4,5],2)

# 6. Sa se scrie o functie care primeste ca parametru un numar variabil de liste si un numar intreg x. Sa se returneze o
# lista care sa contina elementele care apar de exact x ori in listele primite.
# Exemplu: pentru listele [1,2,3], [2,3,4], [4,5,6], [4, 1, "test"] si x = 2 se va returna [1, 2, 3, 4]
# # 1 se afla in lista 1 si 4, 2 se afla in lista 1 si 2, 3 se afla in listele 1 si 2, 4 se afla in listele 2 si 3.
def exercitiul_6(x, *listArgs):
    result = list()
    frequencyArray = {i: 0 for i in range(0,1000)}

    for i in range (0, len(listArgs)):
        currentList = listArgs[i]
        for j in currentList:
            if isinstance(j,int):
                frequencyArray[j] += 1

    for i, j in frequencyArray.items():
        if j == x :
            print(i,j)
            result.append(i)
    print(frequencyArray)
    print(result)
print("\nRaspuns exercitiul 6:")
exercitiul_6(2, [1,2,3], [2,3,4], [4,5,6], [4, 1, "test"])

# 7. Sa se scrie o functie care primeste ca parametri un numar x default egal cu 1, un numar variabil de siruri de
# caractere si un flag boolean setat default pe True. Pentru fiecare sir de caractere, sa se genereze o lista care sa
# contina caracterele care au codul ASCII divizibil cu x in caz ca flag-ul este setat pe True, in caz contrar sa contina
# caracterele care au codul ASCII nedivizibil cu x. Exemplu: x=2, "test", "hello", "lab002", flag=False va returna
# (["e", "s"], ["e", "o"], ["a"]). Atentie: functia trebuie sa returneze un numar variabil de liste care sa corespunda
# cu numarul de siruri de caractere primite ca input.
def exercitiul_7( *strings, x = 1,flag = True):
    for string in strings:
        myList = list()
        if isinstance(string, str):
            for i in range(0, len(string)):
                if flag == True :
                    if (ord(string[i]) %  x == 0):
                        myList.append(string[i])
                else:
                    if (ord(string[i]) %  x != 0):
                        myList.append(string[i])
            print("Resulting list for: ", string, " is ", myList)
        else:
            print("The parameter", string, " is not a string...")
print("\nRaspuns exercitiul 7:")
exercitiul_7( "test", "hello", "lab002", x=2, flag=False)

# 8. Sa se scrie o functie care primeste un numar variabil de liste si returneaza o lista de tuple astfel: primul tuplu
# sa contina primele elemente din liste, al doilea element sa contina elementele de pe pozitia 2 din liste, etc.
# Ex: pentru listele [1,2,3], [5,6,7], ["a", "b", "c"] se va returna: [(1,5,"a"), (2,6,"b"), (3,7,"c")].
# Observatie: In cazul in care listele primite ca input nu au acelasi numar de elemente, elementele lipsa vor fi
# inlocuite cu None pentru a putea fi generate max([len(x) for x in input_lists]) tuple.
def exercitiul_8(*lists):
    listOfTuples = list()

    max = 0
    for i in lists:
        if len(i) > max:
            max = len(i)

    for i in range(0,max):
        temp = list()
        for j in range(0,len(lists)):
            if i >= len(lists[j]):
                temp.append(None)
            else:
                temp.append(lists[j][i])
        temp = tuple(temp)
        listOfTuples.append(temp)

    print(listOfTuples)
print("\nRaspuns exercitiul 8:")
exercitiul_8([1,2,3], [5,6,7], ["a", "b", "c"])
print("#########")
exercitiul_8([1,2,3], [5,6,7], ["a", "b", "c","d","f","g","h"],[])
