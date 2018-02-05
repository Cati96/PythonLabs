# 7. Creati-va un modul propriu in care sa implementati cel putin 3 functii. Utilizati aceste functii intr-un script.
import mathOps.simple.Arithmetic
import mathOps.simple.Bits
#import mathOps.complex.Series
from mathOps.complex import Series as s


def exercitiul_7():
    suma = mathOps.simple.Arithmetic.Add(2,3)
    print(suma)

    diferenta = mathOps.simple.Arithmetic.Sub(2,3)
    print(diferenta)

    shiftDreapta = mathOps.simple.Bits.SHR(2,3)
    print(shiftDreapta)

    shiftStanga = mathOps.simple.Bits.SHL(2, 3)
    print(shiftStanga)

    produs = s.Product(2,3)
    print(produs)

print("\nRaspuns exercitiul 7:")
exercitiul_7()