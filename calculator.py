first_num = int(input("Enter the first number :"))
second_num =int(input("Enter the second number :"))
choice = input("Enter your choice :")
try:
   if choice == '+':
    print( "sum: ", first_num + second_num)
   elif choice == '-':
    print("sub:",first_num - second_num)
   elif choice == '*':
    print("mul:",first_num * second_num)

   elif choice == '/':
        print("Div:", first_num / second_num)
   else:
       print("Invalid operator")
except ZeroDivisionError:
    print("Denomenator cannot be zero")

except ValueError:
   print("Value Place Must not be Invalid")

