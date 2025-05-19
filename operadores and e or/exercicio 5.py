peso = int(input("digite um peso "))
altura = float(input("digite uma altura "))

imc1 = altura * altura
imc2 = peso / imc1

if imc2 < 18.5:
    print("magreza ")
elif imc2 >= 18.5 and imc2 <= 24.9:
    print("normal ")
elif imc2 >= 25 and imc2 <= 29.9:
    print("sobrepeso ")
elif imc2 >= 30 and imc2 <= 34.9:
    print("obsidade grau 1")
elif imc2 >= 35 and imc2 <= 39.9:
    print("obsidade grau 2")
elif imc2 > 40:
    print("obsidade grau 3")
    