# Write a Python program that will return true if the two given integer values are equal or their sum or difference is 5. 

a = int(input("Enter The Value Of A"))
b = int(input("Enter The Value Of B"))

if a == b or (a + b) == 5 or abs(a - b) == 5:
    print("True")
else:
    print("False")