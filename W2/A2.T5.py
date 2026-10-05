print("Program starting.")

word = input("Insert a closed compound word: ")

length = len(word)
first_character = word[0]
last_character = word[-1]
reversed_word = word[::-1]

print("The word you inserted is '" + word + "' and in reverse it is '" + reversed_word + "'.")
print("The inserted word length is", length)
print("First character is", first_character)
print("Last character is", last_character)

print()
print("Take substring from the inserted word by inserting...")

start = int(input("1) Starting point: "))
end = int(input("2) Ending point: "))
step = int(input("3) Step size: "))

substring = word[start:end:step]

print()
print("The word '" + word + "' sliced to the defined substring is '" + substring + "'.")

print("Program ending.")