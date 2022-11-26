import art

print(art.logo)

result = 0

def calculation(number1, operator, number2):
    global result
    if operator == '+':
        result = number1 + number2
        return result
    elif operator == '-':
        result = number1 - number2
        return result
    elif operator == '*':
        result = number1*number2
        return result
    elif operator == "/":
        result = number1/number2
        return result
    else:
        return "Invalid Operator"



def calculator():
 is_calculation_running = True
 number1 = float(input("What is the first number?: "))
 while is_calculation_running:
    print("+\n-\n*\n/")
    operator = input("Pick an operation: ")
    number2 = float(input("What is the next number?: "))
    final_result = calculation(number1, operator, number2)
    print(final_result)
    poll = input(f"Type 'y' to continue calculating with {final_result}, or type 'n' to start new calculation: ")
    if poll == 'n':
        is_calculation_running = False
        calculator()
    elif poll == 'y':
        number1 = final_result

calculator()



"""

from art import logo

def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

def calculator():
  print(logo)

  num1 = float(input("What's the first number?: "))
  for symbol in operations:
    print(symbol)
  should_continue = True
 
  while should_continue:
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What's the next number?: "))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")

    if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
      num1 = answer
    else:
      should_continue = False
      clear()
      calculator()

calculator()


"""