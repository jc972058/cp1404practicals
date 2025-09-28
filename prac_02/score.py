"""
CP1404/CP5632 - Practical
Program to determine score status
"""
from random import randint

def main():
    score = float(input("Enter score: "))
    grade = identify_score(score)
    print(grade)
    random_result = randint(0, 100)
    random_grade = identify_score(random_result)
    print(random_grade)


def identify_score(score: float):
    if score < 0 or score > 100:
       return "Invalid score"
    elif score >= 90:
       return"Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
