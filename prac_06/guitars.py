from prac_06.guitar import Guitar
print("My guitars!")
guitars = []
name = input("Name: ")
while name != '':
    year = int(input("Year: "))
    cost = float(input("Cost: "))
    new_guitar_values = Guitar(name, year, cost)
    guitars.append(new_guitar_values)
    print(f"{new_guitar_values} added")
    name = input("Name: ")

guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

print("These are my guitars:")
for i, guitar in enumerate(guitars, 1): # do something with i (the index) and guitar (the element)
    vintage_string = " (vintage)" if guitar.is_vintage() else ""
    print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")