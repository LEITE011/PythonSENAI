ano1 = int(input("Digite um ano de nascimento: "))

idade = 2025 - ano1

if idade < 10:
    print("é uma criança")
    
elif idade >= 11 and idade < 17:
    print("é um adolescente")
    
elif idade >= 18 and idade < 59:
    print("é um adulto")
    
elif idade > 60:
    print("é um idoso")
