#!/usr/bin/env python
"""
Met dit rekenmachine kan je optellen,aftrekken,vermenigvuldigen en delen door 2 getallen te kiezen
"""


__author__ = "Sven De Visscher"
__email__ = "sven.devisscher@student.kdg.be"
__status__ = "Finished"


# Deze functie telt 2 getallen op
def optellen(x, y):
    try:
        return(x + y)
    except Exception as s:
        print(s)
        return

# Deze functie trekt 2 getallen van elkaar af
def aftrekken(x, y):
    try:
        return(x - y)
    except Exception as s:
        print(s)
        return

# Deze functie vermenigvuldigt 2 getallen
def vermenigvuldigen(x, y):
    try:
        return(x * y)
    except Exception as s:
        print(s)
        return


# Deze functie deelt 2 getallen door elkaar
def delen(x, y):
    try:
        return(x / y)
    except Exception as s:
        print(s)
        return




def main():
    print("Select operation.")
    print("1.Optellen")
    print("2.Aftrekken")
    print("3.Vermenigvuldigen")
    print("4.Delen")
    try:

        keuze = input("Enter choice(1/2/3/4):\n")   # Vraagt input aan de gebruiker

        # Bekijkt of de keuze één van de 4 opties is

        num1 = float(input("Kies en typ het eerste getal: "))
        num2 = float(input("Kies en typ het 2de getal: "))

        if keuze == '1':
            print(num1, "+", num2, "=", optellen(num1, num2))   # Telt de 2 getallen op

        elif keuze == '2':
            print(num1, "-", num2, "=", aftrekken(num1, num2))   # Trekt de 2 getallen af

        elif keuze == '3':
            print(num1, "*", num2, "=", vermenigvuldigen(num1, num2))   # Vermenigvuldigd de 2 getallen

        elif keuze == '4':
            print(num1, "/", num2, "=", delen(num1, num2))  # Deelt de 2 getallen door elkaar

        else:
            raise Exception("ERROR geef een getal in")  # Zegt dat je een ongeldig getal hebt ingevoerd.


    except Exception as s:
        print(s)
        main()
if __name__ == '__main__':  # code to execute if called from command-line
    main()