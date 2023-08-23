# Write a python program to sum of the first n positive integers.

number = int(input("Enter The Postive Number :"))
if number <= 0:
    print("Enter The Postive Number")
else:
    sum = number * (number + 1) // 2
    print("The Sum Of n Postive Number is : ",sum)
