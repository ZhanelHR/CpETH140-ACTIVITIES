
while True:
    size = int(input("Size: "))

    if 1 <= size <= 10:
        break

    print("Invalid size. Please enter 1 to 10.")

for row in range(1, size + 1):
    for column in range(1, size + 1):
        print(f"{row * column:>4}", end="")
    print()