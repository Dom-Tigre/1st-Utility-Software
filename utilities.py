"""
This module contains utilities 
"""

from string import digits


class Utilities:

    def password_generator(self) -> str:
        try:
            import random
            import string

            def generate(lowers, uppers, punctuation, digits):

                characters = ""

                if lowers > 0:
                    characters += string.ascii_lowercase

                if uppers > 0:
                    characters += string.ascii_uppercase

                if digits > 0:
                    characters += string.digits

                if punctuation > 0:
                    characters += string.punctuation

                password = ""

                for _ in range(length):
                    password += random.choice(characters)

                return password

            while True:

                try:
                    length = int(input('Password Length: '))

                    try:
                        while True:
                            lowers = int(input('How many lowers? '))
                            if lowers < length:
                                break
                            elif lowers == length:
                                generate(lowers, 0, 0, 0)
                            print(
                                'Please enter a number less than the length of your password'
                            )
                            continue

                    except ValueError:
                        print("Enter a number")

                    try:
                        while True:
                            uppers = int(input('How many uppers? '))
                            if uppers + lowers < length:
                                break
                            print('Please enter a smaller number')
                            continue

                    except ValueError:
                        print('Enter a number')
                    if length > 5:
                        break
                    print('Please enter a value greater than 5')
                    continue

                except ValueError:
                    print('Enter a number')

                except Exception as e:
                    print("Unexpected Error, added to error log")
                    with open("error_log.txt", "a") as file:
                        file.write(str(e) + "\n")

        except ImportError:
            print('Modules are not installed on your computer')
            exit()


print(Utilities.password_generator())
