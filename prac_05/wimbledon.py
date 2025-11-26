"""
Estimate: 30min
Actual:
"""
filename = "wimbledon.csv"
with open(filename, "r", encoding="utf-8-sig") as in_file:
    CHAMPION_TO_WINS = {}
    countries = []
    number_of_countries = 0
    next(in_file)
    for line in in_file:
        parts = line.strip().split(",")
        champion = parts[2]
        country = parts[1]
        if country not in countries:
            countries.append(country)
            number_of_countries += 1
        CHAMPION_TO_WINS[champion] = CHAMPION_TO_WINS.get(champion, 0) + 1
    print("Wimbledon Champions:")
    for champion, win in CHAMPION_TO_WINS.items():
        print(f"{champion} {win}")
    countries.sort()
    countries_string = ", ".join(countries)
    print(f"These {number_of_countries} countries have won Wimbledon:")
    print(countries_string)

