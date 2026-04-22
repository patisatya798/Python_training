greet = "Hello Friend, "
greet1 = "Hello Student"

greet3 = greet + greet1 #concatenate of string

print(greet3)

for letter in greet:
    print(letter)

print(greet3.partition('Friend'))
print(greet.rstrip())