COLOUR_TO_CODE = {"absolute zero": "#0048ba", "amber": "#ffbf00", "apricot": "#fbceb1", "aqua": "#00ffff", "bronze": "#cd7f32",
                  "charcoal": "#36454f", "chocolate": "#d2691e", "emerald": "#50c878", "ginger": "#b06500", "gray": "#bebebe"}
print(COLOUR_TO_CODE)

colour_name = input("What is the name of your colour? ").lower()
while colour_name != "":
    if colour_name in COLOUR_TO_CODE:
        print(f"{colour_name}'s colour code is {COLOUR_TO_CODE[colour_name]}")
    else:
        print("Invalid short state")
    colour_name = input("Enter short state: ").lower()
