#1 quantos litros serão necessarios, e qual o valor que sera gasto para completar a viagem

#2 informaçoes
# qual a distancia da viagem
# quantos quilometros ja percorremos
# qual a altonomia do carro por litro
# quantos litros ainda há no tanque
# qual o preço do combustivel

#3 passo a passo
# subtrair a distancia da viajem por quanto ja percorremos
# dividir a distancia pela autonomia do carro
# subtrair o combustivel necessario por quanto de combustivel ja temos
# multiplicar o valor obtido pelo preço do combustivel
# apresentar o valor que sera gasto em reais e o quanto de combustivel sera necessario

quilometro = 800 - 90
litro1 = quilometro / 7
litro2 = litro1 - 10
valor1 = litro2 * 6.90

print("o valor de combustivel gasto sera de " , valor1 , " reais")
print("serao necessarios " , litro2 , " litros")
