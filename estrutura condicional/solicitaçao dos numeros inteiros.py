num = int(input("digite um numero "))
num1 = int(input("digite um numero "))
num2 = int(input("digite um numero "))


if num > num1:
    if num > num2:
        print("o primeiro numero é maior que o segundo e o terceiro")
elif num1 > num2:
    if num1 > num:
        print("o segundo numero é maior que o primeiro e o terceiro")
elif num2 > num:
    if num2 > num1:
        print("o terceiro numero é maior que o primeiro e o segundo")
