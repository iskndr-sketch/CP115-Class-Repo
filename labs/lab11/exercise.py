# Complete sentinel pattern - all three parts labeled
grade = float(input("Enter grade (-1 to stop): "))  # Part 1: Prime input

while grade != -1:  # Part 2: Condition
    print(f"You entered: {grade}")
    grade = float(input("Enter grade (-1 to stop): "))  # Part 3: Update input

print("Done entering grades!")