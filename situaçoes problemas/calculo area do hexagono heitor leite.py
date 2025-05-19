#obter os numeros

#1 calcular a area do triangulo
# calcular quanto é lado vezes lado
# descobrir a raiz de 3
#2 calcular a area do hexagono
# multiplicar a area do triangulo vezes 6


lado = int(input("digite um valor para o valor do lado do triangulo "))

lado2 = lado * lado

raiz = round(3 ** 0.5 , 2)

lado3 = lado2 * raiz

area_triangulo = lado3 / 4

print("a area do triangulo é" , area_triangulo)

area_hexagono = area_triangulo * 6

print(" a area do hexagono é " , area_hexagono)

