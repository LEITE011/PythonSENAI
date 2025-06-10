distancia = int(input("Digite qual foi a distancia percorrida: "))
peso = int(input("digite o peso: "))
taxa_fixa = 10

def calcular_o_frete():
    multi = peso * 0.5
    multi1 = distancia * 0.1
    soma = multi + multi1
    valor_do_frete = soma + taxa_fixa
    print("o valor do frete pago sera de: ", valor_do_frete,"reais")

calcular_o_frete()