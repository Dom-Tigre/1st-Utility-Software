"""
This module contains a class of general purpose utilities
"""


class Utilities:
    """
    This class contains general purpose utilities
    """

    def password_generator(self):
        """
        This function generates a password moulded to the users desires
        """
        try:
            import random
            import string

            def generate(length, lowers, uppers, punctuation, digits):
                password = ""
                characters = []

                for _ in range(lowers):
                    characters.append(random.choice(string.ascii_lowercase))

                for _ in range(uppers):
                    characters.append(random.choice(string.ascii_uppercase))

                for _ in range(digits):
                    characters.append(random.choice(string.digits))

                for _ in range(punctuation):
                    characters.append(random.choice(string.punctuation))

                for i in range(length):
                    password += characters.pop(
                        random.randint(0, length - i - 1))

                return password

            # Used to cycle through variables
            list_of_variables = ["lowers", "uppers", "digits", "punctuation"]
            i = 0

            # Initialising Variables
            lowers = 0
            uppers = 0
            digits = 0
            punctuation = 0

            while True:

                try:
                    length = int(input('Password Length: '))

                    try:
                        while True:
                            query = int(
                                input(f'How many {list_of_variables[i]}? '))
                            if i == 0:
                                lowers = query
                            elif i == 1:
                                uppers = query
                            elif i == 2:
                                digits = query
                            elif i == 3:
                                punctuation = query
                            else:
                                i = 0
                                continue

                            total = lowers + uppers + digits + punctuation

                            if total < length:
                                i += 1
                                continue

                            elif total == length:
                                return generate(length, lowers, uppers, digits, punctuation)

                            else:
                                print(
                                    'Please enter a number less than the length of your password'
                                )

                    except ValueError:
                        print("Enter a number")

                    except Exception as e:
                        print("Unexpected Error, added to error log")
                        with open("error_log.txt", "a") as file:
                            file.write(str(e) + "\n")

                except ValueError:
                    print('Enter a number')

                except Exception as e:
                    print("Unexpected Error, added to error log")
                    with open("error_log.txt", "a") as file:
                        file.write(str(e) + "\n")

        except ImportError:
            print('Modules are not installed on your computer')
            exit()
