# 1. Cel mai mare divizor comun a mai multor numere (definiti o functie cu numar variabil de parametri care sa rezolve
# acest lucru)
def exercitiul_1(*args):
    a = args[0]
    for i in range(1,len(args)):
        b = args[i]
        r = 1
        while( r is not 0 ):
            r = a % b
            a = b
            b = r
    print(" gcd for  ",args, " is: ", a)
print("Raspuns exercitiul 1:")
exercitiul_1(1,2,3,4,5,6)
print("#########")
exercitiul_1(15,3, 6, 9)
print("#########")
exercitiul_1(15,5, 6, 9)


# 2. Scrieti o functie care calculeaza cate vocale sunt intr-un sir de caractere
def exercitiul_2_v1(myString):
    num_vowels = 0
    for char in myString:
        if char in "aeiouAEIOU":
            num_vowels +=  1
    print("The number of vowels is: ", num_vowels)
print("Raspuns exercitiul 2:")
exercitiul_2_v1("This is myString")

def exercitiul_2_v2(myString):
    num_vowels = 0
    counts = {i: 0 for i in 'aeiouAEIOU'}
    for char in myString:
        if char in counts:
            counts[char] += 1
    print("Vowels:")
    for k, v in counts.items():
        print(k, v)
        num_vowels += v
    print("The number of vowels is: ", num_vowels)
print("#########")
exercitiul_2_v2("This is myString")

# 3. Scrieti o functie care returneaza numarul de cuvinte care exista intr-un string. Cuvintele sunt separate de spatii,
# semne de punctuatie (, ;, ? ! . )
def exercitiul_3(myString):
    y = myString.replace(' ', ' ').replace(';', ' ').replace('?', ' ').replace('!', ' ').replace('.', ' ').replace(',',' ').split()
    print( y, len(y))
print("\nRaspuns exercitiul 3:")
exercitiul_3("This is a text!   ??!,anca?!;1 ")

    # 4. Scrieti o functie care primeste ca parametri doua siruri de caractere si care returneaza numarul de aparitii ale
# primului sir de caractere in al doilea.
def exercitiul_4_v1(string1, string2):
    wordsNum = string2.count(string1,0,len(string2)) # nu e corect cu count intotdeauna
    print("The first string appears in second of: ", wordsNum, "time(s).")
print("\nRaspuns exercitiul 4:")
exercitiul_4_v1("ana", "ananaana are mere.")

def exercitiul_4_v2(string1, string2):
    wordsNum = 0
    for i in range(0, len(string2)):
        if ( string2.find(string1,i,len(string2))  is not -1 and string2.find(string1,i-1,len(string2)) is not string2.find(string1,i,len(string2)) ):
            wordsNum += 1
    print("The first string appears in second of: ", wordsNum, "time(s).")
print("#########")
exercitiul_4_v2("ana", "ananaana are mere.")



# 5. Scrieti o functie care verifica daca un sir de caractere contine caractere speciale (\r, \t, \n, \a, \b, \f, \v)
def exercitiul_5(myString):
    specialChars = ("\r","\t","\n","\a","\b", "\f","\v")
    counter = 0
    for char in specialChars:
        if ( myString.count(char, 0, len(myString)) is not 0 ):
            counter += 1
    if counter is not 0 :
        print("The string is containg special characters...")
    else:
        print("The string is not cointaing any special character...")
print("\nRaspuns exercitiul 5:")
exercitiul_5("\n\n\nCati\nFlorinCati love\b\a.")
print("#########")
exercitiul_5("CatilovesFlorinforever<3")


# 6. Scrieti o functie care converteste un sir de caractere scris UpperCamelCase in lowercase_with_underscores.
def exercitiul_6(myString):
    if(myString[0].isupper()):
        temp =  "_" + myString[0].lower() + myString[1:]
        myString = temp
    for i in range(1, len(myString)):
        if (myString[i].isupper() is True):
            temp = myString[:i] + "_" + myString[i].lower() + myString[i+1:]
            myString = temp
            i = i - 1
    print(myString)
print("\nRaspuns exercitiul 6:")
exercitiul_6("CatiLovesFlorin")


# 7. Scrieti o functie care primeste un integer char_len si un numar variabil de parametri (siruri de caractere) si
# verifica daca fiecare doua string-uri vecine respecta urmatoarea regula: al doilea string incepe cu ultimile char_len
# caractere a primului string (ca la fazan).
def exercitiul_7(char_len, *args):
    ok = 1
    for i in range ( 0, len(args)-1):
        if ( args[i][len(args[i]) - char_len:len(args[i])] != args[i+1][0:char_len] ):
            ok = 0
            print("The strings are not respecting the rule...")
            break
    if ( ok == 1):
        print("The strings are respecting the rule...")
print("\nRaspuns exercitiul 7:")
exercitiul_7(2, "cati", "tiara", "ramuri", "rinoceri", "rigla", "lautar", "harpagic")
print("#########")
exercitiul_7(2, "cati", "tiara", "ramuri", "rinoceri", "rigla", "lautar")

# 8. Se da un sir de caractere care reprezinta un polinom (Ex: "3x^3 + 5x^2 - 2x - 5") si un numar (intreg sau float).
# Sa se evalueze polinomul respectiv pentru valoarea data.
def exercitiul_8(polynomial, x):
    y  = polynomial.replace('+', '|').replace('-','|').split('|')
    print(y)
    sign = []
    for char in polynomial:
        if char == '+' or char == '-' :
            sign.append(char)
    print(sign)
    for i in range(0,len(y)):
        if y[i].find('x') != -1 :
            y[i] = y[i][0:y[i].find('x')]
    print(y)
    compute = int(y[0]) * pow(x,len(y) - 1)
    print(compute)
    for s in range(0,len(sign)):
        if sign[s] == '+' and s != len(sign):
            compute += int(y[s + 1 ]) * pow(x,len(y) - s  - 2)
        elif sign[s] == '+' and s == len(sign):
            compute += int(y[s + 1 ])
        elif sign[s] == '-' and s != len(sign):
            compute -= int(y[s + 1 ]) * pow(x,len(y) - s  - 2)
        elif sign[s] == '-' and s == len(sign):
            compute -= int(y[s + 1 ])
        print(compute)
    print("The result is: ", compute)
print("\nRaspuns exercitiul 8:")
exercitiul_8("3x^3 + 5x^2 - 2x - 5",2)
print("#########")
exercitiul_8("3x^6 + 5x^5 - 2x^4 - 5x^3 + 2x^2 - 7x + 9",2)


# 9. Scrieti o functie care sa returneze cel mai mare numar prim dintr-un sir de caractere dat ca parametru sau -1 daca
# sirul de caractere nu contine nici un numar prim. Ex: input: 'ahsfaisd35biaishai23isisvdshcbsi271cidsbfsd97sidsda'; output: 271
def prime_number(number):
    divisors = 1
    for i in range ( 2, int(number/2) + 1):
        if number % i == 0:
            divisors += 1
    if ( divisors == 1 ):
        return True
    return False

def exercitiul_9(myString):
    for i in range(0, len(myString)):
        if  ( myString[i] < '0' or myString[i] >  '9' ):
            myString = myString.replace(myString[i], ' ')
    y = myString.split()
    max = -1
    for number in y:
        if ( prime_number(int(number)) ):
            if int(number) > max:
                max = int(number)
    print( max )
print("\nRaspuns exercitiul 9:")
exercitiul_9("ahsfaisd35biaishai23isisvdshcbsi271cidsbfsd97sidsda")
print("#########")
exercitiul_9("ahsfaisdbiaishaiisisvdshcbsicidsbfsdsidsda")
print("#########")
exercitiul_9("ahsfaisdbiaishaiisisvdshcbs8icidsbfsdsidsda")