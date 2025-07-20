import random
password = []
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
chars = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=']
print("Welcome to the password generator")
nr_letters = int(input("Enter the number of letters you want\n"))
nr_digits = int(input("Enter the number of digits you want\n"))
nr_chars = int(input("Enter the number of chars you want\n"))

for i in range(nr_letters):
    pass_letter = random.choice(letters)
    password += [pass_letter]
for j in range(nr_digits):
    pass_digit = random.choice(digits)
    password += [pass_digit]
for k in range(nr_chars):
    pass_char = random.choice(chars)
    password += [pass_char]

random.shuffle(password)
pass_string = ''
for elem in password:
    pass_string += elem
print(f"Your password can be {pass_string}")
