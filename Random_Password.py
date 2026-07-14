import random
import string

def generate_password(length):
    characters = (
        string.ascii_lowercase +
        string.ascii_uppercase +
        string.digits +
        string.punctuation
    )

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

try:
    length = int(input("Enter password length: "))

    if length < 4:
        print("Password length should be at least 4.")
    else:
        print("Generated Password:", generate_password(length))

except ValueError:
    print("Invalid Input!")