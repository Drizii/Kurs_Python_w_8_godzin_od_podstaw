
num = 0
operation = None
reset = True
result = None
calcOperations = ["+", "-", "*", "/", "**"]

while True:
    if reset == True:
        num = int(input("Podaj liczbe startowa: "))
        reset = False

    operation = input("Podaj operacje operacje jak np.: " + str(calcOperations) + " lub exit jeśli koniec lub reset: ")
    if operation == "exit":
        break
    if operation == "reset":
        reset= True
        continue

    if not operation in calcOperations:
        print("wprowadzona zostala bledna operacja")
        continue

    secondNun = int(input("Podaj druga liczbe: "))

    if operation == "+":
        result = num + secondNun

    if operation == "-":
        result = num - secondNun

    if operation == "*":
        result = num * secondNun

    if operation == "/":
        result = num / secondNun

    if operation == "**":
        result = num ** secondNun

    print("wynik operacji: ", str(num), " ", operation, " ", str(secondNun), " = ", str(result) )

    num = result
    result = None

