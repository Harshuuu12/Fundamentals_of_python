# Write a Python program to get the Factorial number of given number.

number = int(input("ENTER THE NUMBER : "))
factorial = 1
for i in range(1, number + 1):
    factorial = factorial * i
print("THE FACTORIAL IS : ",factorial)