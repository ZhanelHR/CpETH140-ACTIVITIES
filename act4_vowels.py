sentence = input("Sentence: ")

count = 0

for letter in sentence:
    if letter in "aeiouAEIOU":
        count += 1

print("Vowels:", count)