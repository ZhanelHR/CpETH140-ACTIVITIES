# Ramirez,Zhanel H., BAET 2101, Task 3 - Leap Year Test
year = int(input("Enter a year: "))
print((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0))
