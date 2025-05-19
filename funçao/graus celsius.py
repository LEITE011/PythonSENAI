celsius = int(input("digite uma temperatura em graus celsius "))

def encontrar_temperatura_em_kelvin(celsius):
    return celsius + 273

def encontrar_temperatura_em_fahrenheit(celsius):
    return celsius * 1.8 + 32

print("seu valor em kelvin é" , encontrar_temperatura_em_kelvin(celsius),)

print("seu valor em fahrenheit é" , encontrar_temperatura_em_fahrenheit(celsius),)