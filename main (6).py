import random
import string

print("Hi there!")
print("Welcome to the Password Generator.")
password_length = int(
    input("Enter the length of the password you'd like to generate: "))

if password_length < 4:
    print("Password length should be at least 4 characters.")
else:
    characters = string.ascii_letters + string.digits + string.punctuation
    password_list = [random.choice(characters) for _ in range(password_length)]
    random.shuffle(password_list)
    password = ''.join(password_list)
    print(f"Your password is: {password}")