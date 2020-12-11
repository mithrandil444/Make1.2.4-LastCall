#!/usr/bin/env python
"""
Info about our project comes here
"""

# IMPORTS
import random, string

__author__ = "Sven De Visscher"
__email__ = "sven.devisscher@student.kdg.be"
__status__ = "Development"


#var
possible_characters = "abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ+=-!<>_?."


def main():
    while True:
        keuze = input("Wil je inspraak op je wachtwoord? Ja of Nee :\n")

        if keuze in ('Ja', 'Nee'):

            if keuze == 'Ja':
                password_length = input("Type here the amount of characters of your password: ")
                try:
                    yourchoice = input(
                        """1 - punctuation only \n2 - Numbers \n3 - Uppercase letters \n4 - Undercase only \n""")
                    if yourchoice == '1':
                        pw = "".join(string.punctuation)
                        print(pw)

                    elif yourchoice == '2':
                        pw = "".join(string.digits)
                        print(pw)

                    elif yourchoice == '3':

                        pw = "".join(string.ascii_uppercase)
                        print(pw)
                        print(password_length)
                        character_list = [random.choice(pw) for i in range(int(password_length))]
                        print(character_list)

                    elif yourchoice == '4':

                        pw = ''.join(string.ascii_lowercase)
                        print(pw)
                        print(password_length)
                        character_list = [random.choice(pw) for i in range(int(password_length))]
                        print(character_list)
                        for x in character_list:
                            print(x)
                    else:
                        print("Choose a number from 1 to 4 please")

                except ValueError:
                    print(" Please enter a Number")


            elif keuze == 'Nee':
                password_length = 20
                random_character_list = [random.choice(possible_characters) for i in range(password_length)]
                random_password = "".join(random_character_list)
                print(random_password)

        else:
            print("ERROR : typ Ja of Nee")
        break
if __name__ == '__main__':  # code to execute if called from command-line
    main()
