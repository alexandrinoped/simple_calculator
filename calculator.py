# 1. Definir as operações básicas
def soma(x, y):
  return x + y

def sub(x, y):
  return x - y

def mult(x, y):
  return x * y

def div(x, y):
  if y == 0:
    return "Error! Division by zero is not allowed."
  return x / y

def potencia(x, y):
    return x ** y

def raiz_quadrada(x):
    if x < 0:
        return "Error! Cannot calculate the square root of a negative number."
    return x ** 0.5

# 2. Criar o menu para o usuário escolher a operação

historico = []

while True:
  print("\nSelect operation: ")
  print("1. Sum")
  print("2. Subtraction")
  print("3. Multiplication")
  print("4. Division")
  print("5. Power")
  print("6. Square root")
  print("7. Show transaction history")
  print("8. Close calculator")

  # 3. Receber a entrada do usuário
  choice = input("\nEnter the number of the desired operation: ")

  # Verificar se a escolha é válida
  if choice not in ['1', '2', '3', '4', '5', '6', '7', '8']:
    print("Invalid option! Please choose one of the available options")
    continue # Retorna ao início do loop

  if choice == '8':
    print("\nYou exit the application. See you soon!")
    break # Encerra o loop e o programa

  if choice == '7':
    print("\nOperations history:")
    for operation in historico:
      print(operation)
    continue

  # Pedir os números dependendo da operação escolhida
  if choice in ['1', '2', '3', '4', '5']:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
  
  elif choice == '6':
    num1 = float(input("Enter the number to calculate the square root:"))
    num2 = None # A raiz quadrada só precisa de um número

# Realizar a operação escolhida
  if choice == '1':
    result = soma(num1, num2)
    print(f"{num1} + {num2} = {result}")
    historico.append(f"{num1} + {num2} = {result}")

  elif choice == '2':
    result = sub(num1, num2)
    print(f"{num1} - {num2} = {result}")
    historico.append(f"{num1} - {num2} = {result}")

  elif choice == '3':
    result = mult(num1, num2)
    print(f"{num1} * {num2} = {result}")
    historico.append(f"{num1} * {num2} = {result}")

  elif choice == '4':
    result = div(num1, num2)
    print(f"{num1} / {num2} = {result}")
    historico.append(f"{num1} / {num2} = {result}")

  elif choice == '5':
    result = potencia(num1, num2)
    print(f"{num1} ** {num2} = {result}")
    historico.append(f"{num1} ** {num2} = {result}")

  elif choice == '6':
    result = raiz_quadrada(num1)
    print(f"√{num1} = {result}")
    historico.append(f"√{num1} = {result}")

