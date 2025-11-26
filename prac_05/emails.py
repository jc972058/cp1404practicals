
EMAIL_TO_NAME = {}

email = str(input("Email: "))
while email != "":
    if email not in EMAIL_TO_NAME:
        username = email.split("@")[0]
        parts = username.split(".")
        capitalised_name = " ".join(parts).title()
        is_name_or_not = str(input(f"Is your name {capitalised_name}? (Y/n) ")).lower()
        is_name_or_not.split()
        if is_name_or_not[0] == "y":
            EMAIL_TO_NAME[email] = capitalised_name
        elif is_name_or_not[0] == "n":
            name = str(input("Name: "))
            EMAIL_TO_NAME[email] = name.title()
    email = str(input("Email: "))
print("")
for email in EMAIL_TO_NAME:
    print(f"{EMAIL_TO_NAME[email]} ({email})")
