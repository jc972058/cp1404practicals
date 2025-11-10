# 1.
name = input("What is your name? ")
FILENAME = "name.txt"
out_file = open(FILENAME, "w")
print(name, file=out_file)
out_file.close()

#2.
FILENAME = "name.txt"
in_file = open(FILENAME, "r")
for line in in_file:
    name_in_file = line
print(f"Hello {name_in_file}")
in_file.close()