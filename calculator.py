first_num = int(input("Enter the first number :"))
second_num =int(input("Enter the second number :"))
choice = input("Enter your choice :")

if choice == '+':
    print( "sum: ", first_num + second_num)
elif choice == '-':
    print("sub:",first_num - second_num)
elif choice == '*':
    print("mul:",first_num * second_num)
elif choice == '/':
    if second_num == 0 :
        print("Divide by Zero Was Not valid")
    else:
        print("Div:", first_num / second_num)
else:
    print("Invalid operator")


