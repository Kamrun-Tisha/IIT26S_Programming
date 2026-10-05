print("Program-starting.")
print("Testing-decision-structures.")

value = int(input("Insert-an-integer: "))

print("\nOptions:")
print("1...In-one-multi-branched-decision")
print("2...In-multiple-independent-if-statements")
print("0...Exit")

choice = int(input("Your-choice: "))

if choice == 1:
    result = value

    if value >= 400:
        result = result + 44
    elif value >= 200:
        result = result + 22
    elif value >= 100:
        result = result + 11

    print("Using-one-multi-branched-decision-structure.")
    print(f"Result-is-{result}")

elif choice == 2:
    result = value

    if value >= 400:
        result = result + 44

    if value >= 200:
        result = result + 22

    if value >= 100:
        result = result + 11

    print("Using-multiple-independent-if-statements.")
    print(f"Result-is-{result}")

elif choice == 0:
    print("Exiting...")

else:
    print("Unknown-option.")

print("Program-ending.")