"""
print menu
"""
def main():
    score = get_valid_score()
    Menu = str("""
    (G)et a valid score
    (P)rint result
    (S)how stars
    (Q)uit
    """)
    print(Menu)
    choice = input(">>> ").upper()
    while choice != 'Q':
        if choice == 'G':
            score = get_valid_score()
            choice = input(">>> ").upper()
        elif choice == 'P':
            result = get_result(score)
            print(result)
            choice = input(">>> ").upper()
        elif choice == 'S':
            print("*" * score)
            choice = input(">>> ").upper()
    print("Farewell")

def get_valid_score():
    score = int(input("Score: "))
    while 100 < score or score < 0:
        print("Invalid score")
        score = int(input("Score: "))
    return score

def get_result(score):
    if score < 0 or score > 100:
       return "Invalid score"
    elif score >= 90:
       return"Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"



main()
