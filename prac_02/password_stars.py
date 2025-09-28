"""
set variable
get password
while variable is too short keep on asking for password
print asterixes as long as the password
"""

def main():
    length_variable = 5
    password = get_password()
    print_asterisk(password)


def print_asterisk(password: str):
    print("*" * len(password))


def get_password() -> str:
    password = input("Password: ")
    while len(password) < 5:
        print("Your password must contain 5 or more characters")
        password = input("Password: ")
    return password


main()
