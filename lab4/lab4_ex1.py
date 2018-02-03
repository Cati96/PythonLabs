# 1. Scrieti un program python care sa primeasca de la linia de comanda doua numere (a si b) si care sa afiseze:
# a) a-b
# b) a+b
# c) a/b
# d) a*b
def exercitiul_1():
    a = input("Enter a: ")
    b = input("Enter b: ")
    try:
        a = float(a)
    except ValueError:
        print("a is not number...")
    else:
        try:
            b = float(b)
        except ValueError:
            print("b is not number...")
        else:
            print("a - b = ", a - b )
            print("a + b = ", a + b)
            print("a * b = ", a * b)
            try:
                print("a / b = ", a / b)
            except ZeroDivisionError:
                print("Division by 0...")

print("\nRaspuns exercitiul 1:")
exercitiul_1()