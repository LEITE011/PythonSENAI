def soma(num1,num2):
    return num1 + num2
def subtraçao(num1,num2):
    return num1 - num2
def divisao(num1,num2):
    return num1 / num2
def multiplicaçao(num1,num2):
    return num1 * num2

def menu_calculadora():
    print("escolha uma opçao ")
    print("1 - soma")
    print("2 - subtraçao")
    print("3 - divisao")
    print("4 - multiplicaçao")

    operaçao = int(input("digite uma operaçao "))

    if operaçao == 1:
        print(soma(num1,num2))
    elif operaçao == 2:
        print(subtraçao(num1,num2))
    elif operaçao == 3:
        print(divisao(num1,num2))
    elif operaçao == 4:
        print(multiplicaçao(num1,num2))

def operaçoes_em_geral():
    print("a soma é igual a", 1,)
    print("a subtraçao é igual a", 2,)
    print("a divisao é igual a", 3,)
    print("a multiplicaçao é igual a", 4,)
        
        
num1 = int(input("digite um numero "))
num2 = int(input("digite mais um numero "))

menu_calculadora()

operaçoes_em_geral()