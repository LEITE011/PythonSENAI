num = int(input("digite um numero "))

n = 0

quantidade = 0

while True:
    if n % 2 == 0:
        print(n)
        quantidade += 1
        n = n + 2
        
    if n > num:
        break

print("o total de numeros pares sao: ",quantidade,)
    
    