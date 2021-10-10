while True:
  print ("Welcome to the calculator!")
  num1 = float(input("What is your first number?: "))
  num2 = float(input("What is your second number?"))
  operation = input("Choose one of the following options: Add / Subtract / Multiply / Divide!")
  if operation == "Add":
    answer = num1 + num2
    print(str(num1) + " + " + str(num2) + " = " + str(answer))
  elif operation == "Subtract":
    answer = num1 - num2
    print(str(num1) + " - " + str(num2) + " = " + str(answer))
  elif operation == "Multiply":
    answer = num1 * num2
    print(str(num1) + " x " + str(num2) + " = " + str(answer))
  elif operation == "Divide":
    answer = num1 / num2
    print(str(num1) + " / " + str(num2) + " = " + str(answer))
  else:
    print("I did not understand you, please try again.")