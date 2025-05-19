import random
print("bem vindo ao jogo das adivinhaçoes ")
print("adivinhe o numero e vença o jogo ")
print("boa sorte ")

n_aleatorio = random.randint(1,100)

while True:
    num = int(input("digite um numero: "))
    if n_aleatorio > num:
        print("o numero é maior que", num)
    elif n_aleatorio > num:
        print("o numero é maior que", num)
        
    else:
        print("voce acertou ")
        print("deseja continuar o jogo? ")
        print("1- sim ")
        print("2- nao ")
        escolha = int(input("escolha uma opçao: "))
        if escolha == 1:
            print("vamos para uma nova rodada: ")
            n_aleatorio = random.randint(1,100)
        else:
            break
        
        
        