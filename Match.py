class InvalidNumberException(Exception):
  pass
try:
  day = int(input("Enter a number : "))
  if day <= 0:
    raise InvalidNumberException("Number Must be greate than 0")

  match day:
    case 1:
      print("Monday")
    case 2:
      print("Tuesday")
    case 3:
      print("Wednesday")
    case 4:
      print("Thursday")
    case 5:
      print("Friday")
    case 6:
      print("Saturday")
    case 7:
      print("Sunday")
except InvalidNumberException as e:
  print(e)