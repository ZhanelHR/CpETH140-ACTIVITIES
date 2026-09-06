# Ramirez, Zhanel H., BAET 2101, Task 1 - Change Calculator
amount = int(input("Enter amount in peso:"))

hundreds = amount // 100
amount = amount % 100

twenties = amount // 20
amount = amount % 20

fives = amount // 5
amount = amount % 5

ones = amount
print("100 pesos", hundreds)
print("20 pesos:", twenties)
print("5 pesos:", fives)
print("1 peso:", ones)