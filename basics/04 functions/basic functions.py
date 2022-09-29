

def addNumber(a,b):
    return a+b


def subNumber(a,b):
    return a-b


def multiplyNumber(a, b):
    return a*b


def add4Number(num1, num2, num3, num4):
    result = num1 + num2 + num3 + num4
    return result


print(addNumber(10,5))

number = subNumber(100, 56)
print(number)

number = multiplyNumber(33, 4)
print(number)

summ = add4Number(1, number, addNumber(10, 6), 9)
print(summ)
