print("Program-starting.")

number = int(input("Insert a positive integer: "))

print()

sequence = [number]
steps = 0

while number != 1:
    if number % 2 == 0:
        number = number // 2
    else:
        number = 3 * number + 1

    sequence.append(number)
    steps += 1

print("Sequence:", " -> ".join(map(str, sequence)))
print(f"Sequence had total {steps} step(s).")

print()
print("Program-ending.")