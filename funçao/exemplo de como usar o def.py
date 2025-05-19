from datetime import datetime

def calcular_idade(ano_nascimento):
    ano_atual = datetime.now().year
    idade = ano_atual - ano_nascimento
    return idade

def mostra_idade(idade):
    print("voce tem" , idade,"anos de idade")

print("dia" , datetime.now().day)

print("hora" , datetime.now().hour)

print("mes" , datetime.now().month)

print("data" , datetime.now())



print("voce tem" , calcular_idade(2000),"anos de idade")

print("voce tem" , calcular_idade(2020),"anos de idade")

print("voce tem" , calcular_idade(2010),"anos de idade")
