# Write python program that swap two number without temp variable.

a = 10
b = 20

print("Before The Value Of a",a)
print("Before The Value Of b",b)

a = a + b
b = a - b
a = a - b 

print("After The Value Of a ",a)
print("After The Value Of b ",b)