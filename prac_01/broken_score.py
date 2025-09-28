"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
score = float(input("Enter score: "))
while 100 <= score or score <= 0:
    print("Invalid score. Please enter another score")
    score = float(input("Enter score: "))
if score >= 90:
    print("Excellent score")
elif score >= 50:
    print("Pass")
else:
    print("Bad")
