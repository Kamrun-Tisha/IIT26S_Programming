print("Program-starting.")

starting = int(input("Insert starting value: "))
stopping = int(input("Insert stopping value: "))

print()
print("Starting while-loop:")

number = starting

while number <= stopping:
    print(number, end=" ")
    number += 1

print()
print()
print("Program-ending.")