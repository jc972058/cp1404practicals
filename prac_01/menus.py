name = input("Hello, what is your name? ")
print("Press 'Q' to quit\n Press 'H' for a greeting\n Press 'G' for a Farewell")
choice = input(">>>>> ").lower()
while choice != "q":
    if choice == "h":
        print(f"Hello {name}")
    elif choice == "g":
        print(f"Goodbye {name}")
    else:
        print("Your input is invalid!!")
    choice = input(">>>>> ").lower()
print("Thank you for using greeter.co")
