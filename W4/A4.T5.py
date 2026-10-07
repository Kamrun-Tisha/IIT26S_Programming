print("Program-starting.")

starting = int(input("Insert starting point: "))
stopping = int(input("Insert stopping point: "))
inspection = int(input("Insert inspection point: "))

if starting >= stopping:
    print("Starting point value must be less than the stopping point value.")
elif inspection < starting or inspection > stopping:
    print("Inspection value must be within the range of start and stop.")
else:
    print()
    print("First loop -- inspection with break:")

    for number in range(starting, stopping):
        if number == inspection:
            break
        print(number, end=" ")

    print()
    print("Second loop -- inspection with continue:")

    for number in range(starting, stopping):
        if number == inspection:
            continue
        print(number, end=" ")

    print()
    print()
    print("Program-ending.")