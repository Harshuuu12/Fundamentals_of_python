# Write a Python program to count the number of characters (character frequency) in a string

string = input("Enter a string: ")

count = [0] * 256

for char in string:
    count[ord(char)] += 1

print("Character frequencies:")
for i in range(256):
    if count[i] > 0:
        print(count[i])
