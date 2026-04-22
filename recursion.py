n = int(input("Enter the number for factorial:"))
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

print(factorial(n))
    
n = int(input("Enter a number :"))

def palidrome(n):
    temp = n
    reverse=0
    while temp > 0:
        digit = temp % 10
        reverse = reverse * 10 + digit
        temp = temp // 10
    return reverse

if palidrome(n) == n :
    print("It is the palidrome number")
else:
    print("It is not a palidrome number ")

# Using Recursion        
n = int(input("Enter a number :"))

def palidrome(n , rev=0):
    if n == 0:
        return rev
    digit = n % 10
    rev = rev * 10 + digit

    return palidrome(n // 10 , rev)



if palidrome(n) == n :
    print("It is the palidrome number")
else:
     print("It is not a palidrome number ")