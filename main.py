# passwdgen

import random
import sys
import string
print()
print("*********************************************************")
print("         Welcome to Password Generator ver 1.0")
print("*********************************************************")

generator_mode = input("""Choose password generator mode:
1 - BASIC: creates password with random characters,
2 - ADVANCED: You can create full customized password,
3 - QUIT: escape the program
*********************************************************
Enter 1,2 or 3: 
""")

characters = list(string.ascii_letters + string.digits + string.punctuation)

if generator_mode == "1":
    def generate_random_pass():
        passw_lenght = int(input("Enter password length: "))
        if passw_lenght < 5:
            print("Password lenght must be at least 5 characters!")
            sys.exit()
        else:
            random.shuffle(characters)
        password = []
        for i in range(passw_lenght):
            password.append(random.choice(characters))

        random.shuffle(password)

        print("Generated password: ","".join(password))
        DefaultPassword = ("".join(password))
        saveTxt = input("Would You like to save current password to txt file? y/n ")
        if saveTxt == "y":
            with open('password.txt', 'w') as f:
                for password in DefaultPassword:
                    f.write(password)

            print("Your password has been saved! Check file password.txt")

        else:
            print("\nGoodbye!")
    generate_random_pass()

if generator_mode == "2":

    password = []
    characters_left = -1


    def update_characters_left(number_of_characters):
        global characters_left

        if number_of_characters < 0 or number_of_characters > characters_left:
            print("Characters out of range from 0 to", password_length)
            sys.exit(0)
        else:
            characters_left -= number_of_characters
            print(characters_left,"characters left.")


    password_length = int(input("Enter advanced password lenght: "))

    if password_length < 5:
        print("Password lenght must be at least 5 characters!")
        sys.exit(0)
    else:
        characters_left = password_length

    lowercase_letters = int(input("How many lower case letters? "))
    update_characters_left(lowercase_letters)

    uppercase_letters = int(input("How many uppercase letters? "))
    update_characters_left(uppercase_letters)

    special_characters = int(input("How Many special characters? "))
    update_characters_left(special_characters)

    digits = int(input("How many digits? "))
    update_characters_left(digits)

    if characters_left > 0:
        print("All characters have to be used. The program fill all empty spaces with random numbers.")
        digits += characters_left

    for _ in range(password_length):
        if lowercase_letters > 0:
            password.append(random.choice(string.ascii_lowercase))
            lowercase_letters -= 1
        if uppercase_letters > 0:
            password.append(random.choice(string.ascii_uppercase))
            uppercase_letters -= 1
        if special_characters > 0:
            password.append(random.choice(string.punctuation))
            special_characters -= 1
        if digits > 0:
            password.append(random.choice(string.digits))
            digits -= 1

    random.shuffle(password)
    print()
    print("Generated password:", "".join(password))
    print()

    AdvancedPassword = ("".join(password))

    saveFile = input("Would You like to save current password to txt file? y/n ")
    if saveFile == "y":
        with open('Advpassword.txt', 'w') as f:
            for password in AdvancedPassword:
                f.write(password)
        print("Your password has been saved! Check file Advpassword.txt")
    else:
        print("Goodbye!!!")
        sys.exit()

if generator_mode == "3":
    print("Goodbye!")
    sys.exit()