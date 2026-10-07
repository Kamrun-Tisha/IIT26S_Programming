print("Program-starting.")

words = []

while True:
    word = input("Insert word (empty stops): ")

    if word == "":
        break

    words.append(word)

print()
print("You inserted:")
print(f"- {len(words)} words")
print(f"- {sum(len(word) for word in words)} characters")

print()
print("Program-ending.")