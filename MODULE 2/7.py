# Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.

a = int(input("Enter The Value Of A"))
b = int(input("Enter The Value Of B"))
c = int(input("Enter The Value Of C"))

if a == b or b == c or c == a:
    print("The Sum Is :0")
else:       
    d = a + b + c
    print("The Sum Is :",d)
