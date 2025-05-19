nomes = []

while True :
    print("menu")
    print("")
    print("[1]-cadastrar nomes")
    print("[2]-Exibir o total de inscritos")
    print("[3]-Exibir a lista de nomes em ordem alfabética")
    print("[4]-Permitir a consulta de um nome")
    print("[0]-sair")
    es = int(input("Faça sua escolha: "))
    
    if es == 0:
        break
    
    elif es == 1:
        nome = input("digite seu nome desejado: ")
        if nome in nomes:
            print("Este nome já está na lista")
        else:
            nomes.append(nomes)
            
    elif es == 2:
        print(len(nomes))
        
        
    elif es == 3:
        nomes.sort()
        print(nomes)
        
    elif es == 4:
        nome1 = input("digite um nome: ")
        if nome1 in nomes:
            print("menu")
            print(" nome ")
            print("[1]-sim")
            print("[2]-nao")
            nome2 = int(input("escolha um numero: "))
            retirar = int(input(''))
            if retirar == 1:
                nomes.remove(nome1)
                print("nome nao esta na lista")
            else:
                nomes.append(nome1)
                print("o nome esta na lista")
        else:
            print('Sair')
            
    
            
            
            
            
                
    
        