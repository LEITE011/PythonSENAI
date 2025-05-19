from datetime import datetime

nome = input("digite seu nome ")

def mostrar_nome(nome):
    hora = datetime.now().hour
    
    if hora > 00 and hora <= 5:
        print("boa madrugada")
        
    elif hora > 5 and hora <= 12:
        print("bom dia")
        
    elif hora > 12 and hora <= 19:
        print("boa tarde")
        
    elif hora > 19 and hora <= 00:
        print("boa noite")



print("olá" , nome ,),mostrar_nome(nome)