# Write a Python program to get the Fibonacci series of given range.

number = int(input("ENTER THE NUMBER :"))
n1 = 0
n2 = 1
print("The Fibonacci series is:", n1, n2, end=" ")
for i in range(2, number):
    n3 = n1 + n2
    print(n3, end=" ")
    n1 = n2
    n2 = n3
