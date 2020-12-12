#!/usr/bin/env python
"""
This is a python script that generates a random password or a password of your choice
"""

# IMPORTS
import random, string

__author__ = "Sven De Visscher"
__email__ = "sven.devisscher@student.kdg.be"
__status__ = "Finished"

# Variable
possible_characters = "abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ+=-!<>_?."


def main():
    while True:
        keuze = input("Do you want to choose your type of password? Yes of No :\n")
        # Asks if you want a random password or not

        if keuze in ('Yes', 'No'):

            if keuze == 'Yes':
                password_length = input("Type here the amount of characters of your password: ")
                # Asks the length of your password

                try:
                    yourchoice = input(
                        """1 - punctuation only \n2 - Numbers \n3 - Uppercase letters \n4 - Undercase only \n""")
                    # Gives you 4 choices

                    if yourchoice == '1':
                        characters = string.punctuation
                        pw = "".join(random.choice(characters) for i in range(int(password_length)))
                        print(pw)
                    # If you choose 1 then your password will exists only of characters with the chosen password length

                    elif yourchoice == '2':
                        numbers = string.digits
                        pw = ''.join(random.choice(numbers) for i in range(int(password_length)))
                        print(pw)
                    # If you choose 2 then your password will exists only of numbers with the chosen password length

                    elif yourchoice == '3':
                        capital_letters = string.ascii_uppercase
                        pw = "".join(random.choice(capital_letters) for i in range(int(password_length)))
                        print(pw)
                    # If you choose 2 then your password will exists only of capital letters with
                    # the chosen password length

                    elif yourchoice == '4':
                        lowercase = string.ascii_lowercase
                        pw = ''.join(random.choice(lowercase) for i in range(int(password_length)))
                        print(pw)
                    # If you choose 4 then your password will exists only of lowercase letters
                    # with the chosen password length

                    else:
                        print("ERROR choose a number from 1 to 4 ")
                    # If your input is not 1,2,3 or 4 then it will give an error

                except ValueError:
                    print(" Please enter a Number")
                # If your input is not a number then it will give an error

            elif keuze == 'No':
                password_length = 20
                random_character_list = [random.choice(possible_characters) for i in range(password_length)]
                random_password = "".join(random_character_list)
                print(random_password)
            # If your choice is No then it will give you a random password that has a password length of 20 characters

        else:
            print("ERROR : typ Yes of No")  # If you type something else then it will give you an error en shut down.
        break


if __name__ == '__main__':  # code to execute if called from command-line
    main()
