import random

while True:
    print("Bem vindo ao menu do jogo ")
    print("[1] - impar ")
    print("[2] - par ")
    print("[3] - sair ")
    num = int(input("escolha uma das opçoes acima para prosseguir: "))
    if num == 1:
        print("A sua escolha foi impar, boa sorte novo jogador ")
        num1 = int(input("informe um numero de 1 a 10 para começarmos o jogo: "))
    elif num == 2:
        print("A sua escolha foi par, boa sorte novo jogador ")
        num1 = int(input("informe um numero de 1 a 10 para começarmos o jogo: "))
    elif num == 3:
        break
    n_aleatorio = random.randint(1,10)

    print("A sua oponente a temida maquina escolheu o numero:", n_aleatorio)
    soma = n_aleatorio + num1
    print("o resultado é ", soma)
   
   
    if soma % 2 == 0:
       
        if num == 1:
            print("o jogador perdeu ") 
        else:
            print("o jogador venceu ")
 
    else:
        print("")
       
        if num == 2:
            print("o jogador perdeu ")
           
        else:
            print("o jogador venceu ")

   
       