"""
set variable
get password
while variable is too short keep on asking for password
print asterixes as long as the password
"""
length_variable = 5
password = input("Password: ")
while len(password) < 5:
    print("Your password must contain 5 or more characters")
    password = input("Password: ")
print("*" * len(password))
