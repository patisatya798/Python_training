# class InvalidAgeException(Exception):
#     pass

# number = 18

# try:
#     age = int(input("Enter a number:"))

#     if age < number:
#         raise InvalidAgeException("This is not valid age")
#     else:
#         print("You are not adult")
# except InvalidAgeException as e:
#     print(e)
# except ValueError:
#     print("Please enter valid number")

# class Myerror(Exception):
#     pass

# def withdraw(b , a):
#     if a > b:
#         raise Myerror("Not enough Balance")
#     return b - a

# try:
#     result = withdraw(10000 , 5000)
#     print(result)
    
# except Myerror as e:
#     print(e)
