
total = 0
items = 0

price = float(input("Price (0 to stop): "))

while price != 0:
    total += price
    items += 1

    price = float(input("Price (0 to stop): "))

if items > 0:
    average = total / items
else:
    average = 0

print(f"Items: {items} Total: {total:.2f}")
print(f"Average: {average:.2f}")