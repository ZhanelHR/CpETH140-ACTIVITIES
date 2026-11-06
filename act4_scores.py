n = int(input("Students: "))
total = 0
highest = 0
passed = 0
for i in range(1, n + 1):
    score = int(input(f"Score {i}: "))
    while score < 0 or score > 100:
        score = int(input("Invalid. Re-enter: "))
    total += score
    if score > highest:
        highest = score
    if score >= 75:
        passed += 1
print("Total:", total)
print("Avg:", format(total / n, ".2f"))
print("Highest:", highest)