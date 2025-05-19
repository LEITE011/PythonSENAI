#1 descobrir o valor que falta para completar o tanque
# subtrair a capacidade do tanque pela quantidade de litros ja colocados no tanque
#2 multiplicar o valor que falta para completar o tanque pelo preço do combustivel
#3 exibir o valor gasto para completar o tanque

nome1 = float(input("escreva um valor para a capacidade do tanque "))
nome2 = float(input("escreva o numero correspondente ao tanto de combustivel no tanque "))
nome3 = float(input("digite o valor do litro do combustivel "))


litros = nome1 - nome2
valor = litros * nome3

print("o valor gasto pra encher o tanque é " , valor)