import random

quick_picks = int(input("How many quick picks? "))

for i in range(quick_picks):
    number_line = []
    while len(number_line) < 6:
        part = random.randint(1, 45)
        if part not in number_line:
            number_line.append(part)
    number_line.sort()
    print(" ".join(f"{part:2}" for part in number_line))