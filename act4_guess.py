
secret_number = 27
tries = 0

while True:
    guess = int(input("Guess: "))
    tries += 1

    if guess > secret_number:
        print("Too high")
    elif guess < secret_number:
        print("Too low")
    else:
        print(f"Correct! You got it in {tries} tries.")
        break