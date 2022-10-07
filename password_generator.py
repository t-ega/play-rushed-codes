import string
import random

letters = string.ascii_lowercase
password = []
special = '#$%^&*!@~'
length = int(input('How many characters long is the password?'))
uppercase = int(input('How many uppercase characters?'))
lowercase = int(input('How many lowercase characters'))
digits = int(input('How many digits?'))
special_char = int(input('How many special characters?'))


def generate_password():
    for i in range(uppercase):
        password.append(random.choice(letters.upper()))
    for i in range(lowercase):
        password.append(random.choice(letters))
    for i in range(digits):
        password.append(str(random.randint(0, 9)))
    for i in range(special_char):
        password.append(random.choice(special))


generate_password()
if len(password) > length:
    print(password[length:])
    del (password[length:])
random.shuffle(password)
password = ''.join(password)
print(password)
