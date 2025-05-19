ano = int(input("difite uma ano de nascimento "))
idade = 2025 - ano

if idade >= 18:
     pessoa = "maior de idade"
    
elif idade < 18:
    pessoa = "menor de idade"
    
print(idade ,"ele é", pessoa )