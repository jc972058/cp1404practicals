# 1.
name = input("What is your name? ")
FILENAME = "name.txt"
out_file = open(FILENAME, "w")
print(name, file=out_file)
out_file.close()

#2.
FILENAME = "name.txt"
in_file = open(FILENAME, "r")
name_in_file = in_file.read()
print(f"Hello {name_in_file}")
in_file.close()

#3.
NUMBERFILE = "numbers.txt"
with open(NUMBERFILE, "r") as number_file:
    number1 = int(number_file.readline())
    number2 = int(number_file.readline())
    addition_result = number1 + number2
    print(addition_result)

#4.
with open(NUMBERFILE, "r") as number_file:
    result = 0
    for line in number_file:
        number = int(line)
        result += number
    print(result)

