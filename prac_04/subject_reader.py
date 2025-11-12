"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = load_data(FILENAME)
    display_subject_details(data)


def load_data(filename=FILENAME):
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(filename)
    loaded_data = []
    for line in input_file:
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        loaded_data.append(parts)
    input_file.close()
    return loaded_data

def display_subject_details(details):
    for detail in details:
        print(f"{detail[0]} is taught by {detail[1]} and has {detail[2]} students")

main()