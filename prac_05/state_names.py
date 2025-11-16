"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

# TODO: Reformat this file so the dictionary code follows PEP 8 convention
CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania", "SA": "South Australia"}
print(CODE_TO_NAME)

state_code = input("Enter short state: ").upper()
state_list = []
while state_code != "":
    if state_code in CODE_TO_NAME:
        state_list.append(state_code)
    else:
        print("Invalid short state")
    state_code = input("Enter short state: ").upper()
for state in state_list:
    try:
        print(f"{state:3} is {CODE_TO_NAME[state]}")
    except KeyError:
        print("Invalid short state")