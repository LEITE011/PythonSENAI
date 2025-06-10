velocidade = int(input("Digite qual foi a distancia percorrida: "))
distancia = int(input("digite aq velocidade: "))

def tempo_levado():
    final = distancia / velocidade
    print("o tempo levado para percorrer essa distancia foi de: ",final)
    
tempo_levado()